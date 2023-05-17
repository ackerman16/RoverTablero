from microbit import *
from Maqueen import *

robot = Maqueen()

while True:
    if button_a.is_pressed():
        robot.mover_celda()
    if button_b.is_pressed():
        robot.mover_celda()
        robot.mover_celda()      