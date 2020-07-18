import requests

url = "https://www.freeforexapi.com/api/live"
res = requests.get(url).json()
print(res["supportedPairs"])