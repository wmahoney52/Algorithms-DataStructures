"""
Monte Carlo Estimation of π

A program that uses the Monte Carlo technique to estimate a value for π (3.1415926...).
The program generates and stores a user-specified number of (x, y) points for the estimation. 
Then, using the given formula, an estimation of pi is generated. Each time the estimation runs, 
the user enters a new number of points. The program runs until the user quits. 
"""

import random
import unicodedata

#Function to get the number of points from the user, accounting for invalid input.
#Returns the user's number of points if the input was valid or -1 to quit.
def get_user_input(): 
    while True: 
        try:
            total_num_points = int(input("Number of points (-1 to quit): "))
            if total_num_points == -1: 
                return -1
            elif total_num_points < -1 or total_num_points == 0: 
                print("Must be a positve number of points.") 
                continue
        except ValueError:
            print("Must be a positive number of points.")
            continue
        return total_num_points

#Function to store all (x, y) points as a list of tuples, count the points within the circle, 
#and print all points. Returns the number of points within the circle. 
def generate_points(points_list, total_num_points):  
    num_points_in_circle = 0
    print("Points generated: ")
    for i in range(total_num_points): 
        points_list.append((random.uniform(-1, 1), random.uniform(-1, 1)))
        print(points_list[i])
        if (points_list[i][0] ** 2) + (points_list[i][1] ** 2) <= 1:
            num_points_in_circle += 1 
    return num_points_in_circle

print("MONTE CARLO ESTIMATION OF " + unicodedata.lookup("GREEK SMALL LETTER PI"))

#Continually get user input, perform the calculation for pi, and print the results until the user quits.
while True:  
    points_list = [] 

    #Get the number of points from the user. If the user enters -1, exit the loop, ending the program. 
    total_num_points  = get_user_input()
    if total_num_points == -1:
        break

    #Generate and print the list of points based on the user's input and perform the calculation for pi. 
    num_points_in_circle = generate_points(points_list, total_num_points)
    pi_estimation = 4 * num_points_in_circle / total_num_points

    #Print the number of points within the circle and the estimation of pi. 
    print("Number of points within the circle: " + str(num_points_in_circle))
    print("Approximation of " + unicodedata.lookup("GREEK SMALL LETTER PI") + ": " + str(pi_estimation))
