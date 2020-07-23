import requests
import json
import pprint
from elasticsearch import Elasticsearch

url = "https://www.blibli.com/backend/content/pages/home2019/sections/main_section/blocks/BEST_PRICE_PRODUCTS?display=normal"

payload = {}
headers = {
  'Cookie': '__cfduid=d507082c9c200e126f4f269c74bc379c81595414252'
}

response = requests.request("GET", url, headers=headers, data = payload)

new=[];
data = response.json()
# print(response.text.encode('utf8'))
print(data["data"])
for dataa in data["data"]:

    name = dataa["name"]
    price = dataa["price"]
    stock = dataa["stock"]
    new.append(name)
    new.append(price)
    new.append(stock)

jsonData = json.dumps(new)
pprint.pprint(jsonData)
#
# es = Elasticsearch([{'host':'localhost','port':9200}])
# es.index(index='my_index', doc_type='json',body=jsonData)

