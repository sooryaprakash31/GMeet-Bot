from functools import wraps
from time import sleep

def operation(func):
     @wraps(func)
     def preventCrash(*args, **kwargs):
          sleep(2)
          func(*args, **kwargs)
          sleep(2)
     return preventCrash