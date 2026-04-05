import requests
import os 

response = requests.get('https://api.example.com/data')

print(response.json())