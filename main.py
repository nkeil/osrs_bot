import pyautogui
import math
import sys
import time

rock1coords = (500, 450)
rock2coords = (400, 450)
unmined = (130, 120, 120)
mined = (78, 73, 72)

pyautogui.PAUSE = 1

def color_distance(r1, g1, b1, r2, g2, b2):
	return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)

def is_mined(rockcolor):
	unmined_dist = color_distance(*rockcolor, *unmined)
	mined_dist   = color_distance(*rockcolor, *mined)
	return mined_dist < unmined_dist

current_rock = 1
is_mining = False
while(True):
	time.sleep(1)
	rock1color = pyautogui.pixel(x=rock1coords[0], y=rock1coords[1])
	rock2color = pyautogui.pixel(x=rock2coords[0], y=rock2coords[1])
	rock1_mined = is_mined(rock1color)
	rock2_mined = is_mined(rock2color)

	
	sys.stdout.write(f"rock1_mined: {rock1_mined}\n")
	sys.stdout.write(f"rock2_mined: {rock2_mined}\n")
	sys.stdout.write(f"current_rock: {current_rock}\n")
	sys.stdout.write(f"is_mining: {is_mining}\n")
	sys.stdout.flush()

	if is_mining:
		if current_rock == 1 and rock1_mined:
			is_mining = False
			current_rock = 2
		if current_rock == 2 and rock2_mined:
			is_mining = False
			current_rock = 1
      
	else:
		if current_rock == 1 and not rock1_mined:
			pyautogui.click(x=rock1coords[0], y=rock1coords[1])
			is_mining = True
		if current_rock == 2 and not rock2_mined:
			pyautogui.click(x=rock2coords[0], y=rock2coords[1])
			is_mining = True



# rock1location = pyautogui.center(pyautogui.locateOnScreen("rock1.png"))
# rock2location = pyautogui.center(pyautogui.locateOnScreen("rock2.png"))
# print(rock1location)
# print(rock2location)

# im1 = pyautogui.screenshot('test.png', region=(300, 300, 300, 200))

# pyautogui.PAUSE = 6
# while(True):
# 	pyautogui.leftClick(x=525, y=433)
# 	pyautogui.leftClick(x=411, y=423)sys.stdout.write