import requests
import os 

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")

#print(api_key)

url = "https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success:")
    print(response.json())

elif response.status_code == 429:
    print("Rate limit reached. Try again later.")

else:
    print("Request failed:", response.status_code)