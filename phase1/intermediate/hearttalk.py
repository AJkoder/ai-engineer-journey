
def generate_reply(message: str) -> str:
    if not message:
        return "Please share something with me so I can help you."

    return f"I hear you. You said: {message}"
