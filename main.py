import requests
import os
from twilio.rest import Client

account_sid = "AC70fe3c07976d241a3c834a134914a8df"
auth_token = "05476cae1ab8a92d5b0b67e1f402e561"

api_key = "496365319bffc9a779f25afdbcd5de4f"

WORKING_OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
weather_parameter = {
    "lat": 22.572645,
    "lon": 88.363892,
    "appid": api_key,
}

response = requests.get(url=WORKING_OWN_ENDPOINT, params=weather_parameter)
response.raise_for_status()
data = response.json()
weather_condition = data["weather"][0]['id']

if weather_condition < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Weather is Haze",
        from_='+13862726990',
        to='+919007045010'
    )
    print(message.status)



