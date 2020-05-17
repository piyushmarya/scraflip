import json
import requests
import httplib2
from bs4 import BeautifulSoup


def read_json(self):
    with open("database/db.json", "r") as fd:
        json_data = json.load(fd)
    return json_data


def dump_to_json(data):
    json_data = read_json()
    json_data.update(data)
    with open("database/db.json", "w") as fd:
        json.dump(json_data,fd,indent = 4)


def dump_price_to_json(email, price):
    json_data = read_json()
    json_data[email]["price"].append(price)
    dump_to_json(json_data)


def read_json():
    with open("database/db.json", "r") as fd:
        json_data = json.load(fd)
    return json_data


def get_price(link):
    request_content = requests.get(link).content
    parser = BeautifulSoup(request_content, "html.parser")
    if "flipkart" in link:
        price = parser.find_all("div", class_="_1vC4OE _3qQ9m1")[0].contents[0]
    return int(price[1::])


def validate_link(link):
    h = httplib2.Http()
    resp = h.request(link, 'HEAD')
    if resp[0]['status'] != "200":
        return {"message":"Invalid link"}
    request_content = requests.get(link).content
    parser = BeautifulSoup(request_content, "html.parser")
    if "flipkart" in link:
        name = parser.find_all("span", class_="_35KyD6")[0].contents[0]
    return {"name":name, "message":"valid_link", "link":link, "price":[]}
