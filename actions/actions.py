
# loc=input("Enter the City")

# url = "https://api.openweathermap.org/data/2.5/weather?q="+loc+"&appid=7a44fd3905797e09557b2adb97e703da"


# print(url)

# from tkinter import Place
# from types import CoroutineType
# from urllib import request, response
# import requests
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class ActionGetWeather(Action):
#     """ Return today's weather forecast"""
#     def name(self):
#       return "action_get_weather"


#     def run(self, dispatcher, tracker, domain):
#         city = tracker.get_slot('location')
#         #api_key = '7a44fd3905797e09557b2adb97e703da'
#         url = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=7a44fd3905797e09557b2adb97e703da"
#         response = requests.get(url)
#         data = response.json()

#         x = data['main']
#         temp = round(x['temp']-273.12,2)
#         place = data['weather']
#         desc = x[0]['main']

#         weather_data = "It's {}*C currently in {}. The weather can be described as {}".format(temp,place,desc)
#         #weather_data = "It's {}*C currently in {}.".format(temp,place)

#         dispatcher.utter_message(weather_data)
#         return[SlotSet("location",city)]

        






import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionGetWeather(Action):
    """ Return today's weather forecast"""

    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):

        city = tracker.get_slot('location')
        api_token = '7a44fd3905797e09557b2adb97e703da'
        url = "https://api.openweathermap.org/data/2.5/weather"
        payload = {"q": city, "appid": api_token, "units": "metric", "lang": "en"}
        response = requests.get(url, params=payload)
        if response.ok:
            description = response.json()["weather"][0]["description"]
            temp = round(response.json()["main"]["temp"])
            cityGR = response.json()["name"]

            msg = f"The current temperature in {cityGR} is {temp} degree Celsius. Today's forecast is {description}"
        else:
            msg= "I'm sorry, an error with the requested city as occured."

        dispatcher.utter_message(msg)
        return [SlotSet("location", None)]















# loc=input("Enter the City")

# url = "https://api.openweathermap.org/data/2.5/weather?q="+loc+"&appid=7a44fd3905797e09557b2adb97e703da"


# print(url)


# from tkinter import Place
# from types import CoroutineType
# from urllib import request, response
# import requests
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class ActionGetWeather(Action):
#     #""" Return today's weather forecast"""
#     def name(self):
#       return "action_get_weather"


#     def run(self, dispatcher, tracker, domain):
#         city = tracker.get_slot('location')
#         #api_key = '7a44fd3905797e09557b2adb97e703da'
#         url = "https://api.openweathermap.org/data/2.5/weather?q="+ str(city) +"&appid=7a44fd3905797e09557b2adb97e703da"
#         response = requests.get(url)
#         data = response.json()
#         x = data['main']
#         temp = round(x['temp']-273.12,2)
#         place = data['weather']
#         desc = x[0]['main']

#         weather_data = "It's {}*C currently in {}. The weather can be described as {}".format(temp,place,desc)
#         dispatcher.utter_message(weather_data)
#         return[SlotSet("location",city)]

        