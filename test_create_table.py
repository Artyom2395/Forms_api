import requests

BASE_URL = "http://127.0.0.1:8000"

template = {
    "name": "OrderForm",
    "fields": {
        "order_id": "text",
        "phone_user": "phone"
    }
}

response = requests.post(f"{BASE_URL}/add_template", json=template)
print("Status Code:", response.status_code)