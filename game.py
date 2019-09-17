from PIL import Image
import cv2
import numpy as np
import keyboard
import random
arr = np.ones((600,500))
arr = arr*255
for i in range(500):
	for j in range(500):
		if i%10 == 9 or j%10 == 9:
			arr[i][j] = 0.8
def change(x,y,z):
	for i in range(9):
		for j in range(9):
			if i >=3 and i<6 and j >= 3 and j<6:
				continue
			arr[x+i][y+j] = z
def next(x,d1,d2):
	y = None
	if d1 == 0 and d2 == 0:
		y = (x[0], (x[1]-10+500)%500)
	if d1 == 0 and d2 == 1:
		y = (x[0], (x[1]+10)%500)
	if d1 == 1 and d2 == 0:
		y = ((x[0]-10+500)%500, x[1])
	if d1 == 1 and d2 == 1:
		y = ((x[0]+10)%500, x[1])
	return y

num = [[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], 
[1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0], 
[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
[0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
[0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0], 
[0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
[0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0]]

def show(x,p):
	for i in range(5):
		for j in range(3):
			change(p[0]+i*10, p[1]+j*10, x[i*3+j])



def show_point(n):
	p = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
	colon = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
	clean = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	pos = [(520, 160), (520, 200), (520,240), (520,280), (520,320)]
	show(p, pos[0])
	show(colon, pos[1])
	for i in range(3):
		show(clean, pos[4-i])
		show(num[int(n%10)], pos[4-i])
		n = n/10

def fun():
	cv2.imshow('Input', arr)
	show_point(0)
	c = 0
	d1 = 1
	d2 = 1
	e = 1
	a = []
	speed = 200
	points = 0
	inc = 0
	mat = np.zeros((500,500))
	for i in range(10):
		a.append((10*i,100))
		mat[10*i,100] = 1
	for i in a:
		change(i[0], i[1], 0)
	cv2.imshow('Input', arr)
	while True:
		if inc == 1 and speed > 30:
			inc = 0
			speed -= 3
		if e == 1:
			e = 0
			food = (int(random.random()*50)*10, int(random.random()*50)*10)
			while mat[food[0], food[1]] != 0:
				food = (int(random.random()*50)*10, int(random.random()*50)*10)
			mat[food[0],food[1]] = 2;
			change(food[0], food[1], 0)
		c += 1
		if keyboard.is_pressed('up'): 
			if d1 == 0:
				d1 = 1
				d2 = 0
		if keyboard.is_pressed('down'): 
			if d1 == 0:
				d1 = 1
				d2 = 1
		if keyboard.is_pressed('left'): 
			if d1 == 1:
				d1 = 0
				d2 = 0
		if keyboard.is_pressed('right'): 
			if d1 == 1:
				d1 = 0
				d2 = 1
		if keyboard.is_pressed('q'):
			print('Quiting!!')
			return points
		x = next(a[len(a)-1], d1,d2)
		if mat[x[0], x[1]] == 2:
			points += 10
			inc = 1
			mat[x[0], x[1]] == 1
			e = 1
			a.append(x)
			show_point(points)
			cv2.imshow('Input', arr)
			continue	
		mat[a[0][0], a[0][1]] = 0
		if mat[x[0], x[1]] == 1:
			print("Game Over!!")
			return points
		mat[x[0], x[1]] = 1
		change(a[0][0], a[0][1], 255)
		change(x[0], x[1], 0)
		a.remove(a[0])
		a.append(x)	
		cv2.imshow('Input', arr)
		cv2.waitKey(speed)
print("your points are : ", fun())