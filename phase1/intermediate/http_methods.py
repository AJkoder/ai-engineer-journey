import requests

url = "https://jsonplaceholder.typicode.com/posts"

# GET: Retrieve a post
response = requests.get(f"{url}/1")
print("GET:", response.status_code)

print("\nResponse Header:")

for key, value in response.headers.items():
    print(f"{key}: {value}")

# POST: Create a new post
new_post = {
    "title": "HeartTalk",
    "body": "Communication matters!",
    "userId": 1
}

response = requests.post(url, json=new_post)
print("POST:", response.status_code)
print("Created post:", response.json())

updated_post = {
    "id": 1,
    "title": "HeartTalk Updated",
    "body": "Communication matters even more!",
    "userId": 1
}

response = requests.put(f"{url}/1", json=updated_post)
print("PUT:", response.status_code)
print("Updated post:", response.json())

# PATCH: Update a post
changed_data = {
    "title": "HeartTalk Patched"
}

response = requests.patch(f"{url}/1", json=changed_data)
print("PATCH:", response.status_code)
print("Patched post:", response.json())

# DELETE: Remove a post
response= requests.delete(f"{url}/1")
print("\nDELETE:", response.status_code)  
print(" Response:", response.text)