import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    user = response.json()

    print("User name:", user["name"])
    print("Email:", user["email"])

except requests.exceptions.Timeout:
    print("HeartTalk: The server is taking too long to respond!")

except requests.exceptions.ConnectionError:
    print("HeartTalk: Unable to connect. Check your internet connection.")

except requests.exceptions.HTTPError as error:
    print("HeartTalk: The API returned an error:", error)

except requests.exceptions.RequestException as error:
    print("HeartTalk: Something went wrong:", error)