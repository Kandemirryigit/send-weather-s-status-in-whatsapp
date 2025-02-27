 # To send HTTP/HTTPS requests to servers 
import requests 
# To send message in whatsaap web 
import pywhatkit as kit

# The program should know which city are you living because program is going to tell you the weather's status
place_name=input("Which city are you living? ") 


api_key_location = # your own location API key should be here
url_location = f"https://api-v2.distancematrix.ai/maps/api/geocode/json?address={place_name}&key={api_key_location}"

response_location=requests.get(url_location)  # To send requests to this specific url
location_data=response_location.json()  # To convert response to json type
# To find lat and long
lat=location_data["result"][0]["geometry"]["location"]["lat"]  
long=location_data["result"][0]["geometry"]["location"]["lng"]



api_key= # your own weather API key should be here
weather_url="https://api.openweathermap.org/data/2.5/forecast"

weather_params={
    "lat":lat,
    "lon":long,
    "appid":api_key,
    "cnt":4

}



response_weather=requests.get(weather_url,params=weather_params)  # To send requests
weather_data=response_weather.json()  # To convert response to json type

# To learn weather status
weather_status=weather_data["list"][1]["weather"][0]["id"]

# The conditions and messages
# You should write the phone number that you want to send message
# your whatsapp web gotta be open in your computer 
if weather_status<=804 and weather_status>=801:
      kit.sendwhatmsg_instantly("+123456789","Today the weather is cool just a little bit cloud.")
elif weather_status==800:
      kit.sendwhatmsg_instantly("+123456789","Today the weather is cool.")
elif weather_status<=699 and weather_status>=600:
    kit.sendwhatmsg_instantly("+123456789","I see snow in the weather.I recommend you to take your umbrella.")
elif weather_status<=599 and weather_status>=500:
     kit.sendwhatmsg_instantly("+123456789","I see rain in the weather.I recommend you to take your umbrella.")
elif weather_status<=399 and weather_status>=300:
      kit.sendwhatmsg_instantly("+123456789","I see light rain in the weather.You don't have to take your umbrealla if you wanna feel the rain.")
elif weather_status<=299 and weather_status>=200:
      kit.sendwhatmsg_instantly("+123456789","I see Thunderstorm in the weather.I recommend that you not go outside.")
