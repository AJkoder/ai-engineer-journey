
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
