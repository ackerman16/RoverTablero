from microbit import *
from Maqueen import *

robot = Maqueen()

while True:
    left_line = robot.read_patrol(0)
    right_line = robot.read_patrol(1)
    
    if left_line == 0 and right_line == 0:
        robot.forward()
    elif left_line == 1 and right_line == 0:
        robot.turn_right()     
    elif left_line == 0 and right_line == 1:
        robot.turn_left()
    elif left_line == 1 and right_line == 1:
        robot.set_motor(0,-50)
        robot.set_motor(1,-50) 
