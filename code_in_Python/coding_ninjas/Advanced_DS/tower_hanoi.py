##  Tower of Hanoi 

# Only one disk moves at a time. 
# Larger disk cannot be aboev a smaller disk

from typing import List

towers = ["a","b","c"]

def rec_toh(disks:int, t:List[int]) -> None:
    if disks == 0:
        return
    
    if disks == 1:
        print(t[0],t[2])
        return
    
    rec_toh(disks-1,[t[0],t[2],t[1]])
    print(t[0],t[2])
    rec_toh(disks-1,[t[1],t[0],t[2]])

rec_toh(2,towers)

print("********************************")

def towerofhanoi(n, src, aux,dest):
    if n == 0:
        return 

    if n ==1:
        print(src,dest)
        return 
    
    towerofhanoi(n-1,src,dest,aux)
    print(src,dest)
    towerofhanoi(n-1,aux,src,dest)

towerofhanoi(2,"a","b","c")
