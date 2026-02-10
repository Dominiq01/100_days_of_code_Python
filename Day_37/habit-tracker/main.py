import requests
from datetime import datetime as dt

from dateutil.relativedelta import relativedelta

api = "https://pixe.la/v1"

USERNAME= "dominikwedzina"
TOKEN = "gshe78rht873ehuh3twert"

headers = {
    "X-USER-TOKEN": TOKEN
}

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor":"yes"
# }
#
# res = requests.post(f"{api}/users", json=user_params)
# res.raise_for_status()
# print(res.text)

graph_params = {
    "id": "graph1",
    "name": "Books Pages Graph",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}
# res = requests.post(f"{api}/users/{USERNAME}/graphs", json=graph_params, headers=headers)
# res.raise_for_status()
# print(res.text)
first_day = dt.today() - relativedelta(months=1, days=21)


# pixel_list = []
today = dt.today().strftime('%Y%m%d')
# while first_day.strftime('%Y%m%d') != today:
#     pixel_list.append({"date": first_day.strftime('%Y%m%d'), "quantity": "10"})
#     first_day = first_day + relativedelta(days=1)


# post_pixel_params = {
#     "date": today,
#     "quantity": "10",
# }

post_pixel_params = {
    "date": first_day.strftime('%Y%m%d'),
    "quantity": "10",
}

# res = requests.post(f"{api}/users/{USERNAME}/graphs/graph1", json=post_pixel_params, headers=headers)
# res.raise_for_status()
# print(res.text)

res = requests.delete(f"{api}/users/{USERNAME}/graphs/graph1/{first_day.strftime('%Y%m%d')}", headers=headers)
res.raise_for_status()
print(res.text)