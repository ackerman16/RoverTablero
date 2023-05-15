from microbit import *
from Maqueen import *

robot = Maqueen()

for i in range(0,2):
    robot.mover_celda()
robot.girar_izquierda()
robot.mover_celda()
robot.girar_derecha()
for i in range(0,6):
    robot.mover_celda()
robot.girar_derecha()
robot.mover_celda()
robot.girar_izquierda
robot.motor_stop_all()
