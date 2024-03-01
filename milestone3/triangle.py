import sys

def get_triangle(row: int) -> list[list[int]]:
    triangle = []

    for row in range(row):
        row_list = []
        for el in range(row+1):
            row_list.append(factorial(row)//(factorial(el)*factorial(row-el)))
        triangle.append(row_list)
    print('Triangle List:', triangle)
    return triangle

def print_triangle(triangle):
    print("Your Triangle:")
    for row in triangle:
        for el in range(len(triangle) - len(row)):
            print(end= ' ')
        for el in row:
            print(el, end = ' ')
        print()

def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return "It is not possible to calculate factorial for negative number"
    else:
        res =  1
        for i in range(1, num + 1):
            res *= i
        return res
    
row = int(sys.argv[1])
print_triangle(get_triangle(row))
