Weather-Chatbot
This is an implementation of Weather Chatbot using RASA framework. To fetch the weather details, I am using OpenWeathermap Api

If you want to use it, you need to specify your API key in the Action.py file


rasa train
To run, first run the action using

rasa run actions
and after it

rasa shell --endpoints endpoints.yml 
To run it in interactive mode, run

rasa shell --endpoints endpoints.yml 
