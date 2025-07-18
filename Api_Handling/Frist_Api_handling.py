import requests

def Fetch_freeApi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    responce = requests.get(url)
    data = responce.json()
    # now first work on the simple simple task here... how it work
    # Access the keys with their values in the "name" dictionary
    for key, value in data["data"]["name"].items():
        print(f"{key}: {value}")
    print(("Address:") , data["data"]["location"]["street"])
    for key, value in data["data"]["location"]["street"].items():
        print(f"{key}: {value}")
Fetch_freeApi()
