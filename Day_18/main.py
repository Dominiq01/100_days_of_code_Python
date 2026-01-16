import random
from random import randint
from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("cyan3")
#
#
# def change_color():
#     color_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
#     timmy.pencolor(color_tuple)
#
#
# def draw_square():
#     for _ in range(4):
#         timmy.fd(100)
#         timmy.left(90)
#
#
# def draw_dashed_line():
#     for _ in range(15):
#         timmy.fd(10)
#         timmy.penup()
#         timmy.fd(10)
#         timmy.pendown()
#
#
# def draw_shape(n_borders, angle):
#     change_color()
#     for _ in range(n_borders):
#         timmy.fd(100)
#         timmy.left(angle)
#
#
# def draw_different_shapes():
#     for n in range(3, 11):
#         angle = 360 / n
#         draw_shape(n, angle)
#
# def random_walk():
#     face_path = [0, 90, 180, 270]
#     timmy.speed(8)
#     timmy.pensize(10)
#     while True:
#         change_color()
#         timmy.seth(random.choice(face_path))
#         timmy.fd(20)
#
# def draw_spirograph(size):
#     timmy.speed("fastest")
#     calc_range = int(360 / size)
#     for _ in range(calc_range):
#         change_color()
#         timmy.circle(100)
#         timmy.left(size)



painting_colors = [(242, 117, 31), (240, 79, 94), (240, 95, 34), (154, 113, 8), (128, 215, 206), (212, 153, 163), (150, 186, 224), (167, 45, 137)]

sammy = Turtle()
sammy.shape("turtle")
sammy.color("cyan3")
sammy.speed("fastest")
sammy.penup()

initial_y = -200
initial_x = -200
sammy.setx(initial_x)
sammy.sety(initial_y)

def change_color():
    rand_color = random.choice(painting_colors)
    sammy.pencolor(rand_color)

def paint_line(dots_number):
    for _ in range(dots_number):
        change_color()
        sammy.dot(20)
        sammy.forward(50)
def paint_lines(lines_number):
    pos_y = initial_y
    for _ in range(lines_number):
        pos_y += 50
        paint_line(10)
        sammy.setx(initial_x)
        sammy.sety(pos_y)

screen = Screen()
screen.colormode(255)


# draw_spirograph(3)
# draw_different_shapes()
paint_lines(10)
screen.exitonclick()
