import requests
Response = requests.get("https://api.ipify.org/?format=json")
# if Response.status_code == 1:

data = Response.json()
print("your Ip is : {}".format(data["ip"]))
    


