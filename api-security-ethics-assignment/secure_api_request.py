import requests
import os 

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")

#print(api_key)

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        print("Success:")
        print(response.json())

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

    else:
        print("Request failed:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)