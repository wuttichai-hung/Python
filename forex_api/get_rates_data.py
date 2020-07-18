import requests

url = "https://www.freeforexapi.com/api/live?pairs=EURUSD,USDJPY"
res = requests.get(url).json()
print(res["rates"])