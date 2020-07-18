import requests

url = "https://www.freeforexapi.com/api/live"
res = requests.get(url).json()
param = ",".join(res["supportedPairs"])

url = "https://www.freeforexapi.com/api/live?pairs=" + param
res = requests.get(url).json()
print(res["rates"])