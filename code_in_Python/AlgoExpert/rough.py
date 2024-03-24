# Subsequence Question 
# array = [5,1,22,25,6,-1,8,10]
# sequence = [1,6,-1,10]
# print(isValidSubsequence(array,sequence))
def isValidSubsequence(array:list[int], sequence:list[int]):
    x_loop = 0
    y_loop = 0
    for x in range(x_loop,len(array)):
        for y in range(y_loop,len(sequence)):
            if array[x] == sequence[y]:
                x_loop+=1
                y_loop+=1
                break
    return x_loop == len(sequence) 


# Selection Sort 
# arr = [13,4,9,5,3]
def sel_sort(arr):
    for x in range(len(arr)):
        min = x
        for y in range(x+1, len(arr)):
            if arr[y] < arr[min]:
                min = y
        arr[x], arr[min] = arr[min], arr[x]

# sel_sort(arr)
# print(arr)


# Merge two sorted arrays
def merge_sorted(arr1,arr2):
    arr3 = []
    i,j=0,0
    len1,len2 = len(arr1), len(arr2)
    
    # When the Arrays have same Length 

    while (i<len1 and j < len2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    
    while (i<len1):
            arr3.append(arr1[i])
            i+=1
    
    while(j< len2):
        arr3.append(arr2[j])
        j+=1
    
    return arr3
                  
# a1 = [1,3,4,7,11]
# a2 = [4,9,11,13]
# print(merge_sorted(a1,a2))

def push_zeroes_end(arr):
    num,zero = 0,0
    hi = len(arr)
    while num < hi:
        if arr[num] > 0 and zero == num:
            zero+=1
        elif arr[num] > 0 :
            arr[zero], arr[num] = arr[num],arr[zero]
            zero = num
            num+=1
        else:
            num+=1

# arr = [9,0,0,8,2]
# push_zeroes_end(arr)
# print(arr)