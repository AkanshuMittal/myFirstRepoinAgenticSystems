import requests
import json

params = {
    "q" : "python",
    "sort" : "stars",
    "order" : "desc",
    "per_page" : 10
}

response = requests.get("https://api.github.com/search/repositories", params=params)

data = response.json()

for repo in data["items"]:
    print(f"Repository Name: {repo['name']}")
    print(f"Stars: {repo['stargazers_count']}")