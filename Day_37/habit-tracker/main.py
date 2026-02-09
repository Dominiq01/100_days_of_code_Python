import requests

# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}
api = "https://pixe.la/v1"

USERNAME= "dominikwedzina"
TOKEN = ""

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
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

res = requests.post(f"{api}/users/{USERNAME}/graphs", json=graph_params)
res.raise_for_status()