import requests
import json


def get_price(na):
    url = f"https://api.cryptorank.io/v1/currencies/{na}?api_key=3f249f403056c48cb04d6d011f59c696d6479d64d113d41d8b3d3346c619"
    prev_price = 0
    j = requests.get(url)
    print(j)
    data = json.loads(j.text)
    print(data)
    price = data['data']['values']['USD']['price']
    print(price)
    return price
    #if price != prev_price:
    #    return int(float(price) * float(self.usd_cost) // float(self.valut_cost))
print(get_price(1))