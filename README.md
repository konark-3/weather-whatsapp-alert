# Weather Alert via Twilio WhatsApp

This Python script uses the **OpenWeatherMap API** to fetch weather forecasts and sends notifications via **Twilio WhatsApp API**.  
It demonstrates API integration, authentication via environment variables, and automated alert delivery.

---

## Tech Stack

- **Language:** Python 3.x  
- **Libraries:** `requests`, `twilio`, `os`  
- **APIs:**  
  - [OpenWeatherMap API](https://openweathermap.org/forecast5) – for weather data  
  - [Twilio API](https://www.twilio.com/) – for WhatsApp notifications  

---

## Setup

Set your environment variables for API credentials:

`'export API_KEY="your_openweather_api_key"
export ACCOUNT_SID="your_twilio_account_sid"
export AUTH_TOKEN="your_twilio_auth_token"`

Replace the coordinates and city name if needed:

`CITY = "Edmonton"
LAT = -33.307041
LON = 116.003113`

Install dependencies:

`pip install requests twilio`

* * * * *

How It Works
------------

1.  **Weather Data Fetch:**\
    Sends a request to OpenWeatherMap API using latitude and longitude.

2.  **Parse Response:**\
    Reads JSON forecast data for the next few hours.

3.  **Send WhatsApp Message:**\
    Uses Twilio API to send an automated message through WhatsApp.

* * * * *

Example Usage
-------------

Run the script:

`python weather_whatsapp_alert.py`

Example output:

- Hello this is a new message from Sunny
- Message status: queued

* * * * *

Notes
-----

-   You must have a **Twilio Sandbox** for WhatsApp configured.

-   Replace phone numbers in the format:

    `to='whatsapp:+<your_number>'
    from_='whatsapp:+14155238886'`

-   Ensure all credentials are stored securely (e.g., environment variables).
