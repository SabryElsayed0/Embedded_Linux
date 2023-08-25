import requests
Response = requests.get("https://api.ipify.org/?format=json")
# if Response.status_code == 1:

data = Response.json()
print("your Ip is : {}".format(data["ip"]))
    
Response = requests.get("https://ipinfo.io/"+data["ip"]+"/geo")

location = Response.json()
print("your location is :  ")
print("country : {} , region : {} , City : {}".format(location["country"],location["region"],location["city"]))