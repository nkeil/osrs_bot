import pyautogui
import math
import sys
import time

unmined = (130, 120, 120)
mined = (78, 73, 72)


pyautogui.PAUSE = 1

def color_distance(r1, g1, b1, r2, g2, b2):
	return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)

def is_mined(rockcolor):
	unmined_dist = color_distance(*rockcolor, *unmined)
	mined_dist   = color_distance(*rockcolor, *mined)
	return mined_dist < unmined_dist
coord_x = [411, 525]
coord_y = [423, 433]
i = 0
while(True):
	rock1color = pyautogui.pixel(400, 450)
	rock2color = pyautogui.pixel(500, 450)
	rock = [rock1color, rock2color]

	pyautogui.leftClick(coord_x[i], coord_y[i])
    while not is_mined(rock[i]):
        rock1color = pyautogui.pixel(400, 450)
        rock2color = pyautogui.pixel(500, 450)
        rock = [rock1color, rock2color]
    i = (i + 1) % 2
    while not is_mined(rock[i]):
        rock1color = pyautogui.pixel(400, 450)
        rock2color = pyautogui.pixel(500, 450)
        rock = [rock1color, rock2color]