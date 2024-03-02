
#1

def multiply_all(l: list):
    res_mult = 1
    for i in l:
        res_mult *= i
    return res_mult

l = [1,2,3,4,5]
print(multiply_all(l))

#2

def count_up_low(s: str):
    count_up = 0
    count_low = 0
    for i in s:
        if i.isupper() or (i >= 'A' and i <= 'Z'):
            count_up += 1
        elif i.islower() or (i >= 'a' and i <= 'z'):
            count_low += 1
    return(count_up,count_low)
            

s = 'KBTU Best University'
print(count_up_low(s))

#3

def palindrome(s1: str):
    rev_s1 = ''
    for i in s1:
        rev_s1 = i + rev_s1
        
    if rev_s1 == s1:
        return (f"This string is palindrome, bc {s1} = {rev_s1}")
    else:
        return (f"This string isn't palindrome, bc {s1} != {rev_s1}")
    

s1 = input()
print(palindrome(s1))

#4
from time import sleep
from math import sqrt

def square_root_by_time(num,time):
    square_root = sqrt(num)
    sleep(time / 1000)
    return f'Square root of {num} after {time} miliseconds is {square_root}'

number = int(input())
time_to_do = int(input())
print(square_root_by_time(number,time_to_do))

#5

def tuple_true(tup):
    return all(tup)

tuple_list = tuple([input() for x in range(3)])
print(tuple_true(tuple_list))
