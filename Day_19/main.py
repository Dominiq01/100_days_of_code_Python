import random
from turtle import Turtle, Screen

# sam = Turtle()
# screen = Screen()
#
# def move_forwards():
#     sam.forward(10)
#
# def move_backwards():
#     sam.backward(10)
#
# def turn_left():
#     sam.left(10)
#
# def turn_right():
#     sam.right(10)
#
# def clear_all():
#     sam.reset()
#
#
# screen.listen()
# screen.onkeypress(move_forwards, "w")
# screen.onkeypress(move_backwards, "s")
# screen.onkeypress(turn_right, "d")
# screen.onkeypress(turn_left, "a")
# screen.onkey(fun=clear_all, key="c")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
pos_y = -130
pos_x = -220
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
winner = ""
for n in range(len(colors)):
    new_Turtle = Turtle(shape="turtle")
    new_Turtle.color(colors[n])
    turtles.append(new_Turtle)

for turtle in turtles:
    turtle.penup()
    turtle.goto(x=pos_x,y=pos_y)
    pos_y += 50

user_bet = screen.textinput("Choose turtle", "Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_num = random.randint(0, 10)
        turtle.forward(rand_num)
        pos_x = int(turtle.xcor())
        print(pos_x)
        if pos_x >= 230:
            winner = turtle.pencolor()
            is_race_on = False

if user_bet == winner:
    print("You win!")
else:
    print("You lost :(")
print(user_bet)
print(winner)

screen.exitonclick()