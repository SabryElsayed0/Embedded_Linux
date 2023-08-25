import requests
Response = requests.get("https://www.boredapi.com/api/activity")
# if Response.status_code == 1:

data = Response.json()
print(data["activity"])
    
