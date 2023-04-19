# Imports go at the top
from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    if distancia <= 10:
        robot.motor(0,0)
    else:
        robot.move_forward(3)
        robot.girarDerecha()
        robot.move_forward(2)
        robot.girarIzquierda()
        robot.move_forward(2)
        robot.girarIzquierda()
        robot.move_forward(2)
        robot.girarDerecha()
        robot.move_forward(4)
