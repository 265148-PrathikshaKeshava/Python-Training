''' 
1. Write a program to calculate the height of a building given the 
   distance of the measuring instrument from the building and angle formed 
   at the observer when the highest point is seen [15]

 '''
import math

dis = float(input("Enter the distance in feet: "))

deg = int(input("Enter the angle: "))

#Height of the building= disxtan(degree)
 
h= 0.3048 *(dis * math.tan(math.radians(deg)))

print("The height of the building is %.2f" % h)

