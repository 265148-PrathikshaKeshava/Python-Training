'''2. Given three points in space A, B and C, determine if the points make a isoceles
   triangle, or right angled triangle or both [15]'''
import math



def classify_triangle(x1, y1, x2, y2, x3, y3):
    # Calculate distances between the points
    AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    CA = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
   

    # Sort the distances 
    sides = sorted([AB, BC, CA])
    a, b, c = sides[0], sides[1], sides[2]

    # Check for right angle triangle 
    if math.isclose(a**2 + b**2, c**2):
        if a == b or b == c or a == c:
            return "Right-Angle Isosceles Triangle"
        else:
            return "Right-Angle Triangle"
    
    # Check for isosceles triangle
    if a == b or b == c or a == c:
        return "Isosceles Triangle"
    
    # If no other condition is met, it's a scalene triangle
    return "Scalene Triangle"

# Input: Coordinates of three points (A, B, C)
x1, y1 = map(float, input("Enter coordinates for point A (x1, y1): ").split())
x2, y2 = map(float, input("Enter coordinates for point B (x2, y2): ").split())
x3, y3 = map(float, input("Enter coordinates for point C (x3, y3): ").split())

# Classify the triangle
result = classify_triangle(x1, y1, x2, y2, x3, y3)
print("The triangle is classified as:", result)
