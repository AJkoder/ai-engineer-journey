message=input("Enter your message: ")

with open("messages.txt", "a") as file:
    file.write(message + "\n")

content=open("messages.txt", "r").read()
print("Messages in the file:")
print(content)