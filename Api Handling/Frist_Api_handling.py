import requests

def Fetch_freeApi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)  #hamay kisy request karna hy wo ulr dena hoga ...
    # now all the data are present in string 
    # now we change this reponse to jason
    data = response.json()
    

Fetch_freeApi()