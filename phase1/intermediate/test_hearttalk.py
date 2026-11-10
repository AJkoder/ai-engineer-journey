
from hearttalk import generate_reply


def test_sad_message():
    result = generate_reply("I feel sad.")

    assert result == "I hear you. You said: I feel sad."


def test_confused_message():
    result = generate_reply("I am confused.")

    assert result == "I hear you. You said: I am confused."


def test_empty_message():
    result = generate_reply("")

    assert result == "Please share something with me so I can help you."
