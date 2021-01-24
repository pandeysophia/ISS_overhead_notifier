import requests
from datetime import datetime

MY_LAT = 40.387878
MY_LONG = -111.849167

PARAMETER = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
             }
response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETER)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

today = datetime.now()

print(today.hour)
