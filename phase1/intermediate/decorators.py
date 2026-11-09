import time
from functools import wraps


def calculate_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Time taken: {end - start:.4f} seconds")

        return result

    return wrapper


@calculate_time
def give_advice(name):
    print(f"Hey {name}, relax! Not every problem needs a 3 AM analysis. 😂")

    time.sleep(2)


give_advice("Anshika")