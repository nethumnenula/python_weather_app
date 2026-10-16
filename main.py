import sys
import os
from urllib.error import HTTPError

from dotenv import load_dotenv
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from requests import RequestException

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")


# print(api_key)


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        # Layout Manager
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        # Alignment
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Assign unique IDs
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # CSS styling
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Comic Sans MS;
            }
            QLabel#city_label{
                font-size: 40px;
                font-weight: bold;
            }
            QLineEdit#city_input{
                font-size: 40px;
                font-family: Comic Sans MS;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-family: Comic Sans MS;
                font-weight: bold;
                color: white;
                background-color: orange;
                border: none;
                border-radius: 5px;
                padding: 5px
            }
            QPushButton#get_weather_button:hover{
                background-color: #FFB040 ;
            }
            
            QLabel#temperature_label{
                font-size: 75px;
                font-family: Comic Sans MS;
                font-weight: bold;
            }
            QLabel#emoji_label{
                font-size: 100px;
            }
            QLabel#description_label{
                font-size: 50px;
                font-family: Comic Sans MS;
            }
        """)

        # Connect button to the function
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        # print("You get the weather")
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # raise an exception if there is an HTTP Error
            data = response.json()

            # print(data)
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            # print(response.status_code)
            match response.status_code:
                case 400:
                    self.display_error("Bad Request!\nPlease check your input!")
                case 401:
                    self.display_error("Unauthorized!\nInvalid API key!")
                case 403:
                    self.display_error("Forbidden!\nAccess is denied!")
                case 404:
                    self.display_error(f"Not Found:\n{self.city_input.text()} not found!")
                    self.city_input.setText(" ")
                case 500:
                    self.display_error("Internal Server Error!\nPlease try again later!")
                case 502:
                    self.display_error("Bad Gateway!\nInvalid response from the server!")
                case 503:
                    self.display_error("Service Unavailable!\nServer is down!")
                case 504:
                    self.display_error("Gateway Timeout!\nNo response from the server!")
                case _:
                    self.display_error(f"HTTP error occurred!\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error!\nCheck your internet connection!")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error!\nThe request timed out!")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects!\nCheck the URL!")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error!\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;"
                                             "font-weight: normal;")
        self.temperature_label.setText(message)

    def display_weather(self, data):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
