#1
N = int(input())
gen_numbers = (i**2 for i in range(N+1))

for i in gen_numbers:
    print(i)
print('-'*10)
#2

def gen_ints(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
list_ints = list(gen_ints(n))

print(*list_ints, sep=', ')
print('-'*10)
#3

def gen_div_3_4(num):
    for i in range(num+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
list_div_3_4 = list(gen_div_3_4(n))

print(*list_div_3_4,sep=', ')
print('-'*10)
#4

a = int(input())
b = int(input())

numbers = (i**2 for i in range(a,b+1))

for i in numbers:
    print(i)
print('-'*10)
#5

def gen_decreasing(n):
    while n >=0:
        yield n
        n -=1

n = int(input())
list_decreased_num = list(gen_decreasing(n))

print(list_decreased_num)
print('-'*10)
