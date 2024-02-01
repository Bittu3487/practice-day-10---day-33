import requests
from twilio.rest import Client
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "85a723c131eeb90185a13799e983ddab"
account_sid = "ACd86d8e9d84273f4eff4f92d18d21a7ed"
auth_token = "e173a0b689181ce4afeb2aa116ec1c0e"
weather_params = {
    "lat":46.947975,
    "lon":7.447447,
    "appid":api_key,
}
response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="baris ayne wala hai kripa kar chata upne sath lijiye",
                     from_='+12019926805',
                     to='+918101355806'
                 )

print(message.status)