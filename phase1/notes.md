
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

# File Handling

## What is File Handling?
File handling allows Python programs to create,
read, write and update files.

## File Modes
- r: Read an existing file.
- w: Write and overwrite existing content.
- a: Append content without deleting existing data.

## Important Methods
- read(): Reads the complete file.
- write(): Writes a string.
- writelines(): Writes multiple strings.
- close(): Closes an opened file.

## with open()
Automatically closes files after use.

## File Paths
- Relative path: chat.txt
- Absolute path: Complete file location.

## Exception
- FileNotFoundError: Raised when a requested file
  does not exist.

## Real-world Application
HeartTalk can save conversations in files
and retrieve them later.

# Iterators and Generators

## Iteration
Going through items one by one.

## Iterable
An object whose elements can be accessed one by one.
Examples: list, tuple, string.

## Iterator
An object that remembers its current position and returns the next item.

- iter() creates an iterator.
- next() retrieves the next item.
- StopIteration occurs when no items remain.

## Generator
A special iterator created using a function with yield.

- yield produces a value and pauses the function.
- The function resumes when the next value is requested.
- Generators help process large data without storing all results together.

## Generator Expression
A shorter way to create a generator.

Example:
(length for length in [5, 10, 15])

## Real-world uses
- Processing large datasets.
- Reading large files line by line.
- Streaming AI responses.
- Machine learning data pipelines.

# Decorators

## What is a decorator?
A decorator adds extra functionality to an existing function without changing its original code.

## Basic structure

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

## @ syntax
@my_decorator is equivalent to:
function_name = my_decorator(function_name)

## *args and **kwargs
- *args accepts multiple positional arguments and stores them in a tuple.
- **kwargs accepts multiple keyword arguments and stores them in a dictionary.

## functools.wraps
Preserves the original function's metadata, such as its name and documentation.

## Execution time decorator
Can measure how long a function takes using:
- time.time()
- end_time - start_time

## Real-world applications
- Logging
- Authentication
- Measuring execution time
- Access control
- FastAPI and Flask routes

# Working with JSON

## What is JSON?
JSON (JavaScript Object Notation) is a lightweight format used to store and exchange structured data between applications.

## JSON and Python data types

- JSON Object `{}` → Python Dictionary
- JSON Array `[]` → Python List
- JSON String → Python String
- JSON Number → Python Integer / Float
- JSON `true` → Python `True`
- JSON `false` → Python `False`
- JSON `null` → Python `None`

## Important JSON functions

- `json.dumps()` – Converts Python data into a JSON string.
- `json.loads()` – Converts a JSON string into Python data.
- `json.dump()` – Writes Python data into a JSON file.
- `json.load()` – Reads a JSON file and converts it into Python data.

## Formatting
- `indent=4` makes JSON files easier to read.

## Error handling
- `JSONDecodeError` handles invalid JSON formatting.
- `FileNotFoundError` handles missing files.

## Real-world applications
- Storing chatbot conversations.
- Exchanging data between applications.
- Working with APIs.
- Saving structured application data.


## Working with APIs

### 1. What is an API?
API (Application Programming Interface) allows two applications to communicate with each other.

Example: HeartTalk communicates with a backend server to retrieve or send messages.

- Endpoint: A specific URL path used to access an API operation.
- Request: Information sent to the server.
- Response: Information returned by the server.
- JSON: A common format for exchanging data.

### 2. Python Requests Library

Install:
```bash
python -m pip install requests
```

Import:
```python
import requests
```

GET request:
```python
response = requests.get(url)
data = response.json()
```

POST request:
```python
response = requests.post(url, json=data)
```

Useful response properties:
- `response.status_code` – HTTP status code.
- `response.json()` – Converts JSON response into Python data.
- `response.text` – Returns response body as text.
- `response.url` – Shows the final request URL.
- `response.headers` – Shows response headers.

### 3. API Error Handling

```python
response = requests.get(url, timeout=5)
response.raise_for_status()
```

- `timeout=5`: Limits how long the request waits.
- `raise_for_status()`: Raises HTTPError for unsuccessful HTTP responses (4xx and 5xx).

Important exceptions:
- `Timeout`
- `ConnectionError`
- `HTTPError`
- `RequestException`

Use `try` and `except` to handle errors gracefully.

---

## HTTP Requests

HTTP (HyperText Transfer Protocol) defines rules for communication between clients and servers.

### 1. HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create a resource |
| PUT | Replace a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

### 2. Query Parameters

Used to pass filters or additional instructions through the URL.

Example:
```python
params = {"userId": 5}
response = requests.get(url, params=params)
```

Requests constructs the URL automatically:
`?userId=5`

### 3. Request Headers

Additional information sent with a request.

Example:
```python
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_api_token"
}
```

### 4. Request Body

Contains data sent to the server, commonly with POST, PUT and PATCH.

Example:
```python
response = requests.post(url, json=data)
```

### 5. Response Headers

Additional information returned by the server.

Example:
```python
print(response.headers)
```

`Content-Type: application/json` means the response body contains JSON.

### 6. Important HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 429 | Too Many Requests |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

### Practice API

JSONPlaceholder: https://jsonplaceholder.typicode.com/

Used for practising API and HTTP requests. It simulates data creation, updates and deletion without permanently changing its stored data.
