messages = [
    "I believe in myself!",
    "Everything is going wrong.",
    "Today is going to be amazing!",
    "Nobody understands me.",
    "I am stronger than my problems."
]


def positive_messages(messages):
    for message in messages:
        if "believe" in message or "amazing" in message or "stronger" in message:
            yield message


for message in positive_messages(messages):
    print(message)