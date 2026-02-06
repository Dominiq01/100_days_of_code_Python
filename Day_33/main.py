import time

import requests
from datetime import datetime as dt
import smtplib

my_email = "dominik.wedzina1245@gmail.com"
smtp = "smtp.gmail.com"
password = "zzopgmrdgaaptlhg"
LAT = 41.820562
LNG = 12.583235

def is_iss_close(iss_lat, iss_lng):
    if LNG - 5 <= iss_lng <= LNG + 5 and LAT - 5 <= iss_lat <= LAT + 5:
        return True
    return False

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

res_sunrise = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
res_sunrise.raise_for_status()
data_sunrise = res_sunrise.json()

results = data_sunrise["results"]

sunrise = int(results["sunrise"].split("T")[1].split(":")[0])
sunset = int(results["sunset"].split("T")[1].split(":")[0])

while True:
    time_now = dt.now().hour
    res_iss = requests.get("http://api.open-notify.org/iss-now.json")
    res_iss.raise_for_status()

    iss_data = res_iss.json()

    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])

    is_iss_close_to_me = is_iss_close(iss_latitude, iss_longitude)

    if is_iss_close_to_me and (sunset <= time_now or time_now <= sunrise):
        print("mail sent")
        with smtplib.SMTP(smtp) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="dominik.wedzina@onet.pl",
                                msg=f"Subject:ISS is close to you!\n\nISS is in range try to sport it on the sky!")
    time.sleep(60)

