from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper_func():
        return f"<b>{func()}</b>"
    return wrapper_func

def make_emphasis(func):
    def wrapper_func():
        return f"<em>{func()}</em>"
    return wrapper_func

def make_underlined(func):
    def wrapper_func():
        return f"<u>{func()}</u>"
    return wrapper_func

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "<h1>Hello, World!</h1>" \
            "<p>This is a paragraph</p>"\
            "<img width=500 src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGQzdHl2cDdtbTRqY2lqNTZteTZzNjNrejAzNmw1c29scXNuY3M2aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wXJpp6RG6BQwDUl5je/giphy.gif'>"

@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
