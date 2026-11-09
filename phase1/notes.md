
# Python - OOP Notes

## 1. Class and Object
- Class: A blueprint for creating objects.
- Object: An instance of a class.

## 2. Constructor and self
- `__init__()` initializes an object's data.
- `self` refers to the current object.

## 3. Encapsulation
- Keeps data and related methods together.
- Controls how data is accessed or modified.
- Double underscore (`__`) enables name mangling.

## 4. Inheritance
- A child class reuses features of a parent class.
- Example: `class RelationshipBot(Chatbot):`

## 5. Polymorphism
- Same method name can have different behaviours.
- Example: Different chatbot classes implement `reply()`.

## 6. Method Overriding
- A child class provides its own implementation of a parent method.

## 7. super()
- Calls functionality from the parent class.
- Example: `super().__init__(bot_name)`

## Real-world application
Our HeartTalk chatbot uses OOP to organize different
chatbot types and their behaviours.

# Exception Handling

## What is exception handling?
It prevents a program from crashing unexpectedly
by handling errors during execution.

## Important keywords

- try: Code that may cause an error.
- except: Handles an exception.
- else: Runs when no exception occurs.
- finally: Always executes.
- raise: Manually raises an exception.

## Common exceptions

- ValueError: Invalid value or conversion.
- ZeroDivisionError: Division by zero.
- TypeError: Operation on an incompatible type.

## Real-world application
HeartTalk can use exception handling to validate
user input and handle unexpected situations.