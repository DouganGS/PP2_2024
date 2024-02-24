import math

#1

degree = int(input())
radian = math.radians(degree)

print('Input degree:',degree, '\nOutput radian:', round(radian,6),'\n')

#2

height = int(input('Height: '))
first_val = int(input('Base, first value: '))
second_val = int(input('Base, second value: '))
expected_val = ((first_val+second_val)*height)/2

print('Expected Output:', expected_val,'\n')

#3

number_of_side = int(input('Input number of sides: '))
length_of_side = int(input('Input the length of a side: '))
area_of_polygon = (number_of_side* (length_of_side**2))/4

print('The area of the polygon is:',int(area_of_polygon),'\n')

#4

length_of_base = int(input('Length of base: '))
length_of_side = int(input('Height of parallelogram: '))
area_of_parallelogram =  float(length_of_base * length_of_side)

print('Expected Output:',area_of_parallelogram)
