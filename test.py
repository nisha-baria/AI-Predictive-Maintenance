import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "temperature": 85,
    "vibration": 4.5,
    "current": 12
}

response = requests.post(url, json=data)

print(response.json())