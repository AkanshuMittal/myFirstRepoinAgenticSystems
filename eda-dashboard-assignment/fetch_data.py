import requests

url = requests.get('https://jsonplaceholder.typicode.com/posts')

print(url.json())