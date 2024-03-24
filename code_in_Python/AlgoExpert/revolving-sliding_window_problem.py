from typing import List
from sys import argv

def revolving_sliding_window(arr:List,window_len:int,iters:int) ->None:
    l_index = 0

    l_arr = len(arr)

    left_side_elem = 0
    right_side_elem = 0

    print(f'array is {arr}')
    for i in range(iters):
        temp_arr = []
        print(f'Iteration -- {i+1}')
        
        # print(f'{l_index} + {window_len} < {l_arr}')
        if (l_index + window_len) < l_arr:
            print(arr[l_index:l_index+window_len])
            
            l_index = l_index+window_len
            # print(f'Left Index is {l_index}\n')
        
        else:
            left_side_elem = l_arr - l_index
            right_side_elem = window_len - left_side_elem

            # print(f'{left_side_elem} -- {right_side_elem}')
            tmp_arr = arr[l_index:l_arr]+arr[:right_side_elem]
            # print(arr[l_index:l_arr],(arr[:right_side_elem]))
            print(tmp_arr)
            l_index = right_side_elem

def main(argv) -> None:
    if len(argv) == 1:
        arr = [1,2,3,6,3,2,5]
        window_len = 3
        iters = 6
    else:
        arr = [1,2,3,5,8,2,3,9]
        window_len = int(argv[1])
        iters = int(argv[2])


    revolving_sliding_window(arr,window_len,iters)

if __name__ == '__main__':
    main(argv)
