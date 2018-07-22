# Citation: Box Of Hats (https://github.com/Box-Of-Hats)

"""
Module for reading keys from a keyboard
"""

import win32api as wapi
import time
import win32gui

# Done by Frannecklp
def grab_screen(winName: str = "Grand Theft Auto V"):
    desktop = win32gui.GetDesktopWindow()

    # get area by a window name
    gtawin = win32gui.FindWindow(None, winName)
    # get the bounding box of the window
    left, top, x2, y2 = win32gui.GetWindowRect(gtawin)
    # cut window boarders
    top += 32
    left += 3
    y2 -= 4
    x2 -= 4
    width = x2 - left + 1
    height = y2 - top + 1

    # the device context(DC) for the entire window (title bar, menus, scroll bars, etc.)
    hwindc = win32gui.GetWindowDC(desktop)
    # Create a DC object from an integer handle
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    # Create a memory device context that is compatible with the source DC
    memdc = srcdc.CreateCompatibleDC()
    # Create a bitmap object
    bmp = win32ui.CreateBitmap()
    # Create a bitmap compatible with the specified device context
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    # Select an object into the device context.
    memdc.SelectObject(bmp)
    # Copy a bitmap from the source device context to this device context
    # parameters: destPos, size, dc, srcPos, rop(the raster operation))
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    # the bitmap bits
    signedIntsArray = bmp.GetBitmapBits(True)
    # form a 1-D array initialized from text data in a string.
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)

    # Delete all resources associated with the device context
    srcdc.DeleteDC()
    memdc.DeleteDC()
    # Releases the device context
    win32gui.ReleaseDC(desktop, hwindc)
    # Delete the bitmap and freeing all system resources associated with the object.
    # After the object is deleted, the specified handle is no longer valid.
    win32gui.DeleteObject(bmp.GetHandle())

    return cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)


keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789,.'£$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

control_tick_per_second = 15
cx_last = 0
cy_last = 0
keys_list = []
mouse_last = time.time()
keys_last_sent = time.time()

while(True):

	mouse_change = False

	if wapi.GetAsyncKeyState(ord('Q')):
		sys.exit()
	current = wapi.GetCursorPos()
	cx = current[0]
	cy = current[1]

	# handle deltas in mouse controls 
	if (cx_last != cx):
		cx_last = cx
		mouse_change = True
	if (cy_last != cy):
		cy_last = cy
		mouse_change = True

	if mouse_change == True:
		current = time.time()
		tick = current - mouse_last
		print(str(current) + ' : ' + str(cx) + ', ' + str(cy) + ' ' + str(tick))
		mouse_last = current

	# handle deltas in keyboard controls
	keys_current = key_check()
	#if len(set(keys_current).intersection(keys_list)) != len(keys_current):
	current = time.time()
	tick = current - keys_last_sent
	keys_list = keys_current
	key_change = True
	if (len(keys_current) > 0) & (tick > (1/15)):
		print(str(current) + ' : ' + ','.join(str(x) for x in keys_current) + ' ' + str(tick))
		keys_last_sent = current

	# get an image of the desktop
	file = grab_screen()
		
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