# Using Python Arrays vs Array Objects

import array as arr
import random

lst = [random.randint(0,x) for x in range(10)]
arr2 = arr.array('I',[random.randint(0,x) for x in range(10,20)])

print(f'{type(lst) = }')
print(f'{type(arr2) = }')

print(f'{lst = }')
print(f'{arr2 = }')

print(arr2.count(0))