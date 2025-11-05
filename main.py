import requests
from twilio.rest import Client
import os


API = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
CITY = "Edmonton"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

LAT = -33.307041
LON = 116.003113

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(API, params=parameters)
response.raise_for_status()

data = response.json()

client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello this is a new message from Sunny',
    to='whatsapp:+15879372064'
)
print(message.status)


