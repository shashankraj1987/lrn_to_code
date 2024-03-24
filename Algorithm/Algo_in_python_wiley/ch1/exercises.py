# R-1.1

# def is_multiple(n,m):
#     if m > n:
#         return False
#     for x in range(1,n+1):
#         if n//x == m:
#             return True

#     return False

#print(is_multiple(12,4))

# ** R-1.2
'''
Check whether a number is even or odd, without using division, multiplication or modulo

https://www.geeksforgeeks.org/3-ways-check-number-odd-even-without-using-modulus-operator-set-2-can-merge-httpswww-geeksforgeeks-orgcheck-whether-given-number-even-odd/

Two ways to do this. 

1) Set a variable to true and loop over the number. Keep alternating the value of the boolean for the loop's duration. If the value is same, then even else odd.

2) Check whether the last bit of the number is 1. If yes, then number is odd or else even. 
'''

# def is_even(n):
#     isEven = True
#     for x in range(n):
#         if isEven:
#             isEven = False
#         else:
#             isEven = True

#     return isEven

#print(is_even(7))

# R-1.3

# def min_max(lst):
#     min_val = float('-inf')
#     max_val = 0 

#     for val in lst:
#         if val > min_val:
#             min_val = int(val)
#         elif val < max_val:
#             max_val = int(val)
#     return (max_val, min_val)

# lst = (4,2,6,9,-1,-88,400,12)

#print(min_max(lst))

# R-1.4

# def sum_sqr(num):
#     ss = 0 
#     for val in range(num):
#         if val%2 == 0:
#             ss = ss+val**2
#     return ss

# def sum_sqr_lc(num):
#     ss = [x**2 for x in range(num) if x%2 == 0]
#     return sum(ss)

#print(sum_sqr(5))
#print(sum_sqr_lc(5))

# R-1.6

# str_val = "abcdef"
# k = -3
# j = len(str_val)+k

#print(str_val[k])
#print(str_val[j])

# R-1.7

# x = range(-8,9,2)
# rng = [n for n in x]
# print(rng)

#R-1.8

x = 1
lst = []
for _ in range(8):
    lst.append(x)
    x = x*2

# print(lst)
# FIXME: #Do the above using list comprehension

# R-1.9
import random
from typing import List
# print(random.choice(lst))
# print(random.randrange(0,8))

def rnd_choice(lst:List) -> None:
    lst.sort()
    start = lst[0]
    end = lst[len(lst)-1]
    found = True
    while found:
        rnd_no = random.randrange(start,end)
        if rnd_no in lst:
            return rnd_no
        else:
            found = True

for _ in range(20):
    print(rnd_choice([2,4,3,8,11,23]),end = ' ')