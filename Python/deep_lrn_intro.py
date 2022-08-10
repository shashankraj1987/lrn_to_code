# -*- coding: utf-8 -*-

import numpy as np

list_of_numbers = np.random.normal(25,7,12)

for i in list_of_numbers:
    if (i % 2 == 0):
        print(i , " is Even")
    else:
        print(i, " is Odd")

print("All Done")
    