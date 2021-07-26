import turtle
from turtle import Turtle
import pandas

# Variables
total_adivinadas = 0

# Logica de la pantalla
screen = turtle.Screen()
screen.title("Juego de Povincias del Ecuador")
image = "Ecuador_mapa.gif"
screen.addshape(image)
turtle.shape(image)

# Logica de los datos
row_data = pandas.read_csv("provincias.csv")
list_of_provincias = row_data["provincia"].to_list()
total_provincias = len(row_data)

# Logica del juego
is_the_game_on = True


def verify_if_imput_is_correct(user_input):
    #print(row_data["provincia"])
    print(user_input)
    if user_input in list_of_provincias:
        return True


def create_turtle_with_name_and_position(name, x, y):
    provincia_name = Turtle()
    provincia_name.hideturtle()
    provincia_name.penup()
    provincia_name.goto(x, y)
    provincia_name.write(name)


while is_the_game_on:
    answer_provincia = screen.textinput(title=f"Adivina la provincia {total_adivinadas}/{total_provincias}",
                                        prompt="¿Dime qué provincia falta?")
    if verify_if_imput_is_correct(answer_provincia):
        provincia_adivinada = row_data[row_data["provincia"] == answer_provincia]
        print("Nombre" + provincia_adivinada["provincia"])
        print(f"x:  {int(provincia_adivinada.x)}")
        print(f"y:  {int(provincia_adivinada.y)}")
        create_turtle_with_name_and_position(name=provincia_adivinada.provincia.item(), x=int(provincia_adivinada["x"]),
                                             y=int(provincia_adivinada["y"]))
        total_adivinadas +=1

    if total_adivinadas >23:
        is_the_game_on = False
        print("GAME OVER")

turtle.mainloop()
