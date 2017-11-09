import numpy as np
def area():
	r = float(input('What is the radius of the circle?'))
	area = np.pi*r**2
	print('The area of a circle with radius ' + str(r) + ' is: ' + str(round(area,2))) 
def circumference():
	r = float(input('What is the radius of the circle?'))
	circumference = 2*np.pi*r
	print('The circumference of a circle with radius ' + str(r) + ' is: ' + str(round(circumference,2))) 

area() 
circumference()
