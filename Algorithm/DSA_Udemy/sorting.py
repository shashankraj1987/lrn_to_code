# Bubble Sort

class Sorting:
	def __init__(self, array: list[int]):
		self.array = array
		self.len = len(self.array)

	def bubble_sort(self):
		"""
		Iterate from the first element of the array and keep pushing the largest element to the end with each iteration.
		"""
		for x in range(self.len-1):
			for y in range(x+1, self.len):
				# print("x = ",self.array[x], "y = ", self.array[y])
				if self.array[x] > self.array[y]:
					self.array[x], self.array[y] = self.array[y], self.array[x]
			# print("*"*10)

	def selection_sort(self):
		"""
		Take index of the first element. For the duration of the array, replace it
		with the minimum element for the rest of the array.
		Then swap the element before next loop with minimum value.
		"""
		for x in range(self.len):
			min_val = x
			for y in range(x+1, self.len):
				print("Y is ",self.array[y])
				if self.array[min_val] > self.array[y]:
					self.array[min_val], self.array[y] = self.array[y] , self.array[min_val]
				if min_val != x:
					min_val = x

			print("Minimum value is ",self.array[min_val])

	def insertion_sort(self):
		for x in range(1, self.len):
			temp = self.array[x]
			j = x -1
			while (self.array[j] > temp) and j > -1:
				self.array[j+1] = self.array[j]
				self.array[j] = temp
				j-= 1


arr = [4,2,6,5,1,3]
# arr = [1,2,3,4,5,6]
sort = Sorting(arr)
sort.insertion_sort()
print(arr)