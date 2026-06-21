import requests

url = "https://eventpulse-gridlock.onrender.com"

response = requests.get(url)

print(response.json())