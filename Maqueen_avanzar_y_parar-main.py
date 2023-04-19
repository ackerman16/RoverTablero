from microbit import *
from Maqueen import *
robot = Maqueen()

while True:
    distancia = robot.read_distance()
    if distancia <= 10:
        robot.motor_stop_all()
        sleep(1000)
    else:
        robot.forward()