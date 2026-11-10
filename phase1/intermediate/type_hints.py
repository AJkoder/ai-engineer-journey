
# HeartTalk - Learning Type Hints

# 1. Type hints for variables
bot_name: str = "HeartTalk"
user_age: int = 22
is_active: bool = True

# 2. Type hints for a list
messages: list[str] = [
    "I feel confused.",
    "I need some advice.",
    "Everything will be okay!"
]

# 3. Type hints for a dictionary
user: dict[str, int] = {
    "age": 22,
    "experience": 2
}

# 4. Optional value: string or None
user_name: str | None = "Priya"

# 5. Function with input and return type hints
def greet_user(name: str) -> str:
    return f"Hello {name}! Welcome to {bot_name}."

# 6. Function with multiple parameters
def create_reply(message: str, age: int) -> str:
    return f"You said: {message}. Your age is {age}."

# 7. Function with an optional parameter
def personal_greeting(name: str | None = None) -> str:
    if name is None:
        return "Hello! What should I call you?"
    
    return f"Hello {name}! I'm here to listen."

# 8. Function that may return a string or None
def find_message(index: int) -> str | None:
    if 0 <= index < len(messages):
        return messages[index]
    
    return None


# Testing our functions
print(greet_user("Priya"))
print(create_reply("I feel confused.", 22))
print(personal_greeting("Priya"))
print(personal_greeting())

print(find_message(0))
print(find_message(10))
