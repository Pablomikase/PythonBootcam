from turtle import Turtle, Screen

tortu = Turtle()
myScreen = Screen()

def move():
    tortu.forward(15)

myScreen.listen()
myScreen.onkey(key="space", fun=move)
print(tortu.ycor())
print(tortu.fillcolor())
myScreen.exitonclick()
