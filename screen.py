import win32gui
import sys
import time
import numpy as np

from PIL import ImageGrab


def rgb_to_grayscale(pixel):
	return pixel[0] * 0.299 + pixel[1] * 0.587 + pixel[2] * 0.114

def get_window_pixels(rect):
	count = 0
	pixels = ImageGrab.grab().load()
	print(pixels[0,0])
	x_range, y_range = rect[2] - rect[0], rect[3] - rect[1]
	start_x, start_y = rect[0], rect[1]
	export_pixels = [[0 for y in range(y_range)] for x in range(x_range)]
	for y in range(rect[1], rect[3]):
		for x in range(rect[0], rect[2]):
			export_pixels[x-start_x][y-start_y] = rgb_to_grayscale(pixels[x,y])
	return np.array(export_pixels)

#Gets hwnd list
def _get_windows_by_title(title_text, exact = False):
	def _window_callback(hwnd, all_windows):
		all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
	windows = []
	win32gui.EnumWindows(_window_callback, windows)
	if exact:
		return [hwnd for hwnd, title in windows if title_text == title]
	else:
		return [hwnd for hwnd, title in windows if title_text in title]

"""
Brings the desired window denoted by the hwnd to the front of the screen.
Parameters:
 - hwnd: A windows hwnd object that represents the 
"""
def _bring_to_front(hwnd):
	try:
		win32gui.SetForegroundWindow(hwnd)
	except:
		print("Unexpected error, please restart Tetris and retry")
		sys.exit()

def get_window_rect():
	hwndList = _get_windows_by_title("NullpoMino version7.5.0")
	try:
		hwnd = hwndList[0]
	except(IndexError):
		print("Error: Window not found. Please make sure game is launched.")
		sys.exit()

	_bring_to_front(hwnd)
	rect = win32gui.GetWindowRect(hwnd)

	negatives = 0
	for element in rect:
		if element < 0:
			negatives += 1
	if negatives == 4:
		print("Unexpected error, please restart game retry")
		sys.exit()
	return rect

def grab_frame():
	rect = get_window_rect()
