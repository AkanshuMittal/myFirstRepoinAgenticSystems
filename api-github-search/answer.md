1. Role of Query Parameters
Query parameter plays a importanr role because it helps to customize the API request and based upon the different parameters we will find the repositories.
In this request:
q=python → searches repositories related to "python"
sort=stars → sorts results based on star count
order=desc → shows highest starred repos first
per_page=5 → limits results to only 5 repositories

Without query parameters, the API would return generic or unwanted data.

2. response.json() converts the API response directly into a Python dictionary.
response.text gives raw string data (JSON format as text), which is harder to work with because you would need to manually parse it.
So, response.json() is used because it is clean, structured, and easier to handle.