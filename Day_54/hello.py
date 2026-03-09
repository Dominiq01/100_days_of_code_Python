from flask import Flask
import time
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello, World!"
#
# if __name__ == "__main__":
#     app.run()


def delay_decorator(func):
    def wrapper_function():
        time.sleep(2)
        func()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello, World!")

def say_bye():
    print("Bye, World!")

decorated_function = delay_decorator(say_bye)


say_hello()
decorated_function()