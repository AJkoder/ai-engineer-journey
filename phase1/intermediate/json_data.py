import json

try:
    with open("phase1/intermediate/messages.json", "r") as file:
        saved_data = json.load(file)

    print("Conversation loaded successfully!")
    print(saved_data)

except json.JSONDecodeError:
    print("Oops! The JSON file contains invalid data.")

except FileNotFoundError:
    print("Conversation file was not found.")