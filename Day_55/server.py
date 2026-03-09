import random

from flask import Flask

app = Flask(__name__)

random_num = random.randint(0, 9)


@app.route("/")
def hello():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img width=500 src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


def display_result(text, link, color):
    return f"<h1 style='color: {color};'>{text}</h1>" \
           f"<img width=500 src={link}>"


@app.route("/<int:number>")
def guess_number(number):
    if random_num == number:
        return display_result("You found me!",
                              'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjViMXdtdXhmYW9rOGdveHJxd3Brc3pqcHNia2U0NGVub3k0YnVrdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/elsol3P5Jt2ASsxLva/giphy.gif',
                              "green")
    elif number > random_num:
        return display_result("Too high!",
                              'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnV2M3JwcGR4am93YWkzY2t5bmNqODQwZXZhZGVwNWQwcXVnMjl3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LKTTAzGboJGzC/giphy.gif',
                              "blue")
    elif number < random_num:
        return display_result("Too low!",
                              'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGw1Y3JzNjhhOG5yNHp2bDh4MjJrdzBnc2F0NTBuemVrNm1kYmpkNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QrxxIHDiuwZVePLCTO/giphy.gif',
                              "red")


if __name__ == "__main__":
    print(random_num)
    app.run(debug=True)
