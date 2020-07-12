from bs4 import BeautifulSoup as bs
import requests
from flask import jsonify
url = "https://www.goldtraders.or.th/"
r = requests.get(url)
c = r.content
soup = bs(c,"html.parser")
goldPrice = soup.find_all("td",{"style":"text-align:right;vertical-align:middle;"})
updating_time = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblAsTime"})
BLSell = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblBLSell"})
BLBuy = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblBLBuy"})
OMSell = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblOMSell"})
OMBuy = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblOMBuy"})
goldPrice_dict = {}
goldPrice_dict['updating_time'] = updating_time.text.replace(" เวลา", "").split(" น.")[0]
goldPrice_dict['gold_bricks_buy_str'] = BLSell.text.strip()
goldPrice_dict['gold_bricks_sell_str'] = BLBuy.text.strip()
goldPrice_dict['gold_jewelry_buy_str'] = OMSell.text.strip()
goldPrice_dict['gold_jewelry_sell_str'] = OMBuy.text.strip()
goldPrice_dict['gold_bricks_buy_float'] = float(goldPrice_dict['gold_bricks_buy_str'].replace(",", ""))
goldPrice_dict['gold_bricks_sell_float'] = float(goldPrice_dict['gold_bricks_sell_str'].replace(",", ""))
goldPrice_dict['gold_jewelry_buy_float'] = float(goldPrice_dict['gold_jewelry_buy_str'].replace(",", ""))
goldPrice_dict['gold_jewelry_sell_float'] = float(goldPrice_dict['gold_jewelry_sell_str'].replace(",", ""))
print(goldPrice_dict)