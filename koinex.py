#!/Users/tomvictor/github/koinex-price-ticker/myenv/bin/python

import requests
import json
import os

API = "https://koinex.in/api/ticker"

print("-----Koinex-----")

r = requests.get(API)

# print(r.text)


data = r.json()
# print(data)


print("XRP : " + data["prices"]["XRP"])

read_string = ""

read_string += "Ripple coin"
read_string += data["prices"]["XRP"]
read_string += "INR"

cml = "say " + read_string

os.system(cml)


# print()