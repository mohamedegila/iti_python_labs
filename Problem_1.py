#calculate distance between to points

#import Math lib
import math

print("Problem #1 ")
print("===============")

# taking three input at a time
x1, y1, x2, y2 = [int(x) for x in input("Enter values x1, y1, x2, y2:  ").split()]


def calculate_distance(x1, y1, x2, y2):
    '''
    Function to calculate distance between 
    two given points p1(x1,y1) - p2(x2,y2) 
    '''
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return float(distance)

print("===================================================")
print("Distance between given points: ", calculate_distance(x1, y1, x2, y2))