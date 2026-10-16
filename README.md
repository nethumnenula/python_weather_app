# Weather App - Python

# Installation
- `pip install PyQt5`
- `pip install requests`
- `pip install python-dotenv`

# Environmental Variables
Create a .env file.  
`WEATHER_API_KEY=`your weather api key

# Exception Handling
- **HTTPError**
  - `400` : Bad Request! Please check your input!
  - `401` : Unauthorized! Invalid API key!
  - `403` : Forbidden! Access is denied!
  - `404` : Not Found! City not found!
  - `500` : Internal Server Error! Please try again later!
  - `502` : Bad Gateway! Invalid response from the server!
  - `503` : Service Unavailable! Server is down!
  - `504` : Gateway Timeout! No response from the server!
- **ConnectionError**
  - Connection Error! Check your internet connection!
- **Timeout**
  - Timeout Error! The request timed out!
- **TooManyRedirects**
  - Too Many Redirects! Check the URL! 
- **RequestException**
  - Request Error! {req_error} 
