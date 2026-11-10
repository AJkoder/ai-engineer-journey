import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 5
}

response = requests.get(url, params=params)

print("Final URL:", response.url)
print("Status code:", response.status_code)

posts = response.json()

for post in posts:
    print(post["title"])