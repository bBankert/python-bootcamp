import functools
from random import randint

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        # run before func
        print("Starting!")
        func(*args,**kwargs);
        # run after func
        print("Finished!")
    return wrapper

@start_end_decorator
def print_name(name=""):
    if not name:
        raise ValueError("Need a name!")

    print(f"Hello! {name}")

# Build universal decorator that can be used to retry on exception
def universal_retry(max_attempts):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args,**kwargs)
                except Exception:
                    attempt += 1
                    print(f"Retrying, current attempt {attempt}")
            print("Reached max retry attempts, not retrying again")
        return wrapper
    return decorator




@universal_retry(max_attempts=3)
def sporadic_failure():
    rand_value = randint(1,10)
    if(rand_value > 0):
        raise Exception(f"Sporadic Failure! got value: {rand_value}")
    print(f"Worked! Got value: {rand_value}")

#print_name("Tommy")

sporadic_failure()
