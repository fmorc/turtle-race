import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False
turtles = []

for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-225, y=-50 + (30 * i))
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            color = turtle.color()[0]
            is_race_on = False
            if color == user_bet.lower():
                print(f"You won! The winner is {color}")
            else:
                print(f"You lost! The winner is {color}, you chose {user_bet}")


screen.exitonclick()
