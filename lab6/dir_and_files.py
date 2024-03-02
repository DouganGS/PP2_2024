import os

#1

def dir_names(road):
    print(f'\nDirectories in {road}:')
    for dirn in os.listdir(road):
        if os.path.isdir(dirn):
            print(dirn)

def file_names(road):
    print(f'\nFiles in {road}:')
    for item in os.listdir(road):
        if os.path.isfile(item):
            print(item)

def all_names(road):
    print(f'\nDirectories and files in {road}:')
    for i in os.listdir(road):
        print(i)

road = os.getcwd()
dir_names(road)
file_names(road)
all_names(road)

#2

def test_existence(road):
    if os.path.exists(road):
        print(f"Yes file exists in {road}")
    else:
        print(f"No file doesn't exists in {road}")

def test_readability(road):
    if os.path.access(road, os.R_OK):
        print(f"Yes file has readability in {road}")
    else:
        print(f"Yes file hasn't readability in {road}")
        
def test_writability(road):
    if os.path.access(road, os.W_OK):
        print(f"Yes file has writability in {road}")
    else:
        print(f"Yes file hasn't writability in {road}")

def test_executability(road):
    if os.path.access(road,os.X_OK):
        print(f"Yes file has executability in {road}")
    else:
        print(f"Yes file hasn't executability in {road}")

road = os.getcwd()

test_existence(road)
test_readability(road)
test_writability(road)
test_executability(road)

# 3 

def test_exist(road):
    if os.path.exists(road):
        dir_name, file_name = os.path.split(road)
        print(dir_name,file_name)
    else:
        print(f"Your path doesn't exist in {road}")
        

road = os.getcwd()
test_exist(road)

# 4

with open('file.txt','r') as f:
    lines = len(f.readlines())
    print(lines)

# 5

road = os.getcwd()
my_list = ['Is','The','Kbtu','Best','University','?']

with open(r'C:\Users\Dougan\OneDrive\Рабочий стол\python\Lab works\lab6\file.txt','w') as f:
    for i in my_list:
        f.write(i + '\n')

f.close()

#6
import string
def gen_files():
    for i in string.ascii_uppercase:
        file_name = f'{i}.txt'
        with open(file_name, 'w') as file:
            file.write(f"This is {i}.txt")

gen_files()

# 7

with open('txt1.txt','r') as first_txt, open('txt2.txt','w') as second_txt:
    for i in first_txt:
        second_txt.write(i)

# 8

def del_file(road):
    if os.path.exists(road):
        os.remove(road)

road = input()
del_file(road)
        
