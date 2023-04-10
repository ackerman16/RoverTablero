# Imports go at the top
from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    if distancia <= 10:
        robot.motor(0,0)
        sleep(1000)
        robot.motor(0,225)
        sleep(1000)
        robot.motor(225,225)
        sleep(1000)
        robot.motor(225,0)
    else:
        robot.motor(225,255)