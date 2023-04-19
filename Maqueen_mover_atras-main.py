from microbit import *
from Maqueen import *
robot = Maqueen()

while True:
    distancia = robot.read_distance()
    if distancia <= 10:
        robot.backwards()
        sleep(1000)
        robot.girar_derecha()
        sleep(1000)
    else:
        robot.forward()