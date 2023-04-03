# Importing all necessary libraries
import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look out the window, I can't tell what the weather is like!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Weather in the city: {city}\nTemperature: {cur_weather}C° {wd}\n"
              f"Humidity: {humidity}%\nPressure: {pressure} mmHg\nWind: {wind} m/s\n"
              f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nDuration of the day: {length_of_the_day}\n"
              f"Have a good day!"
              )

    except Exception as ex:
        print(ex)
        print("Check the city name")

# Main function to start to get the weather
def main():
    city = input("Enter a city: ")
    get_weather(city, open_weather_token)

# Driver Code
if __name__ == '__main__':
    main()
