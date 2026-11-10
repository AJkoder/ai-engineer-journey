
# HeartTalk - Clean and Reusable Code

# Constants
BOT_NAME = "HeartTalk"

# Greet the user
def greet_user(name: str) -> str:
    """Create a personalized greeting."""
    return f"Hello {name}! Welcome to {BOT_NAME}."


# Generate a supportive reply
def generate_reply(message: str) -> str:
    """Generate a simple supportive response."""
    return f"I hear you. You said: {message}"


# Display the response
def display_reply(reply: str) -> None:
    """Display HeartTalk's response."""
    print(f"{BOT_NAME}: {reply}")


# Main application function
def main() -> None:
    """Run the HeartTalk application."""

    user_name = "Priya"
    user_message = "I am feeling confused."

    greeting = greet_user(user_name)
    print(greeting)

    reply = generate_reply(user_message)
    display_reply(reply)


# Run the application
if __name__ == "__main__":
    main()
