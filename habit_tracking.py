import requests
from datetime import datetime
pixela_end_point = "https://pixe.la/v1/users"
TOKEN = "gsdfjngosfpsdpofmpsdmfiksdnfgdsnfiodnfiodsfkpdsfpkosdfndisonfgiosdnfidsf"
USERNAME = "debashis"
graph_id = "graph1"
users_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response = requests.post(url=pixela_end_point,json=users_params)
# print(response.text)
graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"
today = datetime(year=2024,month=1,day=11)

graph_config = {
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
response = requests.post(url=graph_end_point,json=graph_config,headers=headers)
print(response.text)
pixela_creation_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{graph_id}"
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"15",
}
# response = requests.post(url=pixela_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)
update_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity":"4.5"
}
response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
print(response.text)