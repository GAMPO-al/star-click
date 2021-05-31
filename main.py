import pyautogui as py
from time import sleep
sleep(1)
x = 0
while True:
	star = py.locateCenterOnScreen('stars.png',confidence=0.8)
	if star is not None:
	    py.moveTo(star)
	    py.click()
	    print("stars clicked")
	sleep(0.7)
	nixt = py.locateCenterOnScreen('next.png',confidence=0.8)
	if nixt is not None:
	    py.moveTo(nixt)
	    py.click()
	    print("next clicked")
	print(x)
	x+=1
