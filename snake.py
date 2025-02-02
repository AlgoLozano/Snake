from random import randrange
from turtle import *
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colores = ["cyan", "blue", "orange", "purple", "yellow", "green", "brown", "gray"] #Lista de colores para escoger
colorSnake = random.choice(colores) #Selecciona un color aleatorio de la lista para la vibora
colorFood = random.choice(colores) #Selecciona un color aleatorio de la lista para la comida
if colorFood == colorSnake:
    colorSnake = random.choice(colores) #Si el color es el mismo, seleccionar un nuevo color

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
    
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)

def moveFood():
    # Genera una posicion al azar para la comida
    food.x = + randrange(-10, 11, 10)
    food.y = + randrange(-10, 11, 10)
    # la comiga se mueve hasta que no llegue al limite
    if not inside(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    ontimer(moveFood, 500)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood() # linea que permite que se mueva la comida
done()
