import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70°F", self)
        self.emoji_label = QLabel("😊", self)
        self.description_label = QLabel("Sunny", self)
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
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
                font-family: Comic Sans MS;
            }
        """)

    def get_weather(self):
        pass

    def display_error(self, message):
        pass

    def display_weather(self, date):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
