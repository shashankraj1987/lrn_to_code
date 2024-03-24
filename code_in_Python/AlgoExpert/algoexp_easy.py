from typing import List

class TwoSum:
    def __init__(self,array: list[int], target:int):
        self.array = array
        self.target = target

    def twoNumberSum_mysoln(self) -> list[int]:
        n=0
        for x in range(len(self.array)):
            val1 = self.array[x]
            n+=1
            # print(array[x])
            for y in range(len(self.array)-n):
                val2 = self.array[-y-1]
                print(f'Comparing {val1} with {val2}')
                sum = val1+val2
                if sum == self.target:
                    return val1,val2
            print("*"*25)
        return []
        
    def twoNumberSum_algoexp(self):
        for i in range(len(self.array)-1):
            firstNum = self.array[i]
            for j in range(i+1,len(self.array)):
                secondNum = self.array[j]
                if firstNum+secondNum == self.target:
                    return [firstNum,secondNum]
        
        return []

# ============================================================

class Validate_seq:
    def __init__(self,arr:List[int],seq:List[int]):
        self.arr = arr
        self.seq = seq

    def my_soln(self):
        pass
        

    def algoexp_sol(self):
        pass 

