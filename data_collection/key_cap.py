# Citation: Box Of Hats (https://github.com/Box-Of-Hats)

"""
Module for reading keys from a keyboard
"""

import win32api as wapi

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789,.'£$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

while(True):
	if win32api.GetAsyncKeyState(ord('Q')):
		sys.exit()
	current = win32api.GetCursorPos()
	cx = current[0]
	cy = current[1]	
	print(cx + ', ' + cy)
	for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
        	print(key)
# import sys
# import time
# import win32api

# if (len(sys.argv) < 4):
# 	print "Usage: python mousemove.py dx dy speed"
# 	sys.exit()

# current = win32api.GetCursorPos()
# cx = sx = current[0]
# cy = sy = current[1]

# mx = int(sys.argv[1])
# my = int(sys.argv[2])
# vx = vy = int(sys.argv[3])

# print "Moving", mx, my, "with", vx, "pixels per second"
# print "Press 'q' to quit"

# last = time.time()

# while(True):
# 	if win32api.GetAsyncKeyState(ord('Q')):
# 		sys.exit()
		
# 	current = time.time()
# 	tick = current - last
# 	last = current
	
# 	if mx > 0:
# 		cx += vx * tick;
# 		if cx > mx + sx or cx < sx:
# 			vx = -vx;
# 			cx = max( sx, min( mx + sx, cx ) )
# 	if( my > 0 ):
# 		cy += vy * tick;
# 		if cy > my + sy or cy < sy:
# 			vy = -vy;
# 			cy = max( sy, min( my + sy, cy ) )
	
# 	win32api.SetCursorPos((int(cx),int(cy)))
# 	time.sleep(0.001)