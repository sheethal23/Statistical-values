#!/usr/bin/python3

'''
Name		:SHEETHAL YELLISETTY 
PURPOSE		:TO CALCULATE AND PRINT STATISTICAL VALUES OF INPUT FROM STDIN
'''

import math                      #for computing math functions we need to import math
import sys


def read_data(numbers):           #subroutine to read float point numbers from stdin
    lines = []
    for i in sys.stdin:
       lines.append(i) 
       numbers = [float(j) for j in lines]
    return numbers



def std_deviation(numbers, mean):   #subroutine to calculate standard deviation
    total_sum = 0
    for a in range(len(numbers)):
        total_sum += (numbers[a] - mean) ** 2
    under_root = total_sum * 1.0 / len(numbers)
    return math.sqrt(under_root)


def print_stat():                  #subroutine that prints the statistical values of input numbers          
    numbers = []
    collection = read_data(numbers)
    if(len(collection) != 0):      #checks weather input is empty or not
    	print("Output Statistics for Input Data")
    	print("--------------------------------")
    	print("Low:    " + str(min(collection)))
    	print("High:   " + str(max(collection)))
    	mean = round(sum(collection) / len(collection), 2)
    	print("Mean:   " + str(mean))
    	print("StdDev:  " + str(round(std_deviation(collection, mean) ,2)) + "\n")
    else:
    	print("Output Statistics for Input Data")
    	print("--------------------------------")
    	print("Low:    " )
    	print("High:   " )
    	print("Mean:   " )
    	print("StdDev:  " )

	
print_stat()                      #calling of subroutine                
