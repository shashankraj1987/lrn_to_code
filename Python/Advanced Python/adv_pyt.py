import numpy as np
import os

lst = np.arange(2,15,3)

print(lst)

n="True"
drv=" "

while n != 'False':
      drv = input("Enter the Drive Letter : ")
      if drv.__len__() > 3:
            n = "False"
            print(" Drive letter cannot be greater than 2 ")
            quit()
      else:
          print ("Will attempt to list all the drives: ")
          print(type(drv))
          print(drv)
          lst_dir=os.listdir(drv)
      n = "False"

for i in lst_dir:
    print(i)
