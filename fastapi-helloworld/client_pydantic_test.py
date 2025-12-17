import requests


body = {
    "name": "rahul",
    "price": 10,
    "address": "Gurgaon"
}

resp = requests.post("http://127.0.0.1:8000/items",
                     json=body)
print(resp.json())