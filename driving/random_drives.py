# devcon.exe install ScpVBus.inf Root\ScpVBus
# https://github.com/shauleiz/vXboxInterface/releases
from gamepad import AXIS_MIN, AXIS_MAX, TRIGGER_MAX, XInputDevice
import os
import time
gamepad = None
import random

def set_gamepad(controls):
    # trigger value
    trigger = int(round(controls[0][1] * TRIGGER_MAX))
    if trigger >= 0:
        # set left trigger to zero
        gamepad.SetTrigger('L', 0)
        gamepad.SetTrigger('R', trigger)
    else:
        # inverse value
        trigger = -trigger
        # set right trigger to zero
        gamepad.SetTrigger('L', trigger)
        gamepad.SetTrigger('R', 0)

    # axis value
    axis = 0
    if controls[0][0] >= 0:
        axis = int(round(controls[0][0] * AXIS_MAX))
    else:
        axis = int(round(controls[0][0] * (-AXIS_MIN)))
    gamepad.SetAxis('X', axis)

def drive():
	global gamepad
	gamepad = XInputDevice(1)
	gamepad.PlugIn()

	while True:
		drive_angle = float(random.randrange(-1000, 1000)/1000)
		throttle = float(random.randrange(-1000, 1000)/1000)

        # set the gamepad values
		set_gamepad([[drive_angle, throttle]])
		print(str(drive_angle) + " " + str(throttle))
		time.sleep(1)
		set_gamepad([[0, 0]])
		
		#pause = True
		# release gamepad keys
		#set_gamepad([[0, 0]])
		#print('Paused. To exit the program press Z.')

		# keys = key_check()
		# if 'T' in keys:
		#     pause = False
		#     stop = False
		#     close = True
	gamepad.UnPlug()


def main():
    # control a car
    drive()

if __name__ == '__main__':
	main()