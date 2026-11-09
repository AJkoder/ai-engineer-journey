
# HEARTTALK - Relationship Advice Chatbot
# Python OOP Revision

# 1. Parent Class
class Chatbot:

    def __init__(self, bot_name):
        self.bot_name = bot_name

    def greet(self):
        print(f"Hello! I am {self.bot_name}.")


# 2. Child Class - Inheritance
class RelationshipBot(Chatbot):

    def __init__(self, bot_name, user_name):
        super().__init__(bot_name)

        # Encapsulation: private-style attribute
        self.__user_name = user_name

    # Encapsulation: controlled access
    def show_user(self):
        print(f"Talking with {self.__user_name}")

    def change_user(self, new_name):
        self.__user_name = new_name

    # Method Overriding
    def greet(self):
        super().greet()
        print("I'm here to listen and help you.")

    # Instance Method
    def reply(self):
        print("Let's understand your relationship situation.")


# 3. Another Child Class
class FriendshipBot(Chatbot):

    def reply(self):
        print("Let's understand your friendship situation.")


# 4. Creating Objects
relationship_bot = RelationshipBot("HeartTalk", "Anshika")
friendship_bot = FriendshipBot("HeartTalk Friends")


# 5. Using Inherited and Overridden Methods
relationship_bot.greet()
relationship_bot.show_user()

# Changing private-style data through a method
relationship_bot.change_user("Priya")
relationship_bot.show_user()


# 6. Polymorphism
bots = [relationship_bot, friendship_bot]

for bot in bots:
    bot.reply()
