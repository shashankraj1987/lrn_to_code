n = 0
while n < 10:
    print(n)
    n = n+1

print("hello world {xyz}".format(xyz="abc"))

name = "Shashank Raj"

print(name[0:-2])

array = (10, 20, 30, 40, 50)
print(array[1:3])

array1 = [ "abc", 123, "xyz", 999 ]
print(array1[0:2])

array1.append(456)

print(array1)

n = 20
if n < 10: print(10)
else: print(20)

d = { 'A':25, 'B':30, 'C':40 }

print(d)

for key in d:
    print (key , d[key], end = ' ')

print()
x=[1,2,3,4,5]
print(x)
print(x+x)

### Increasing the value of an array object ###

x=x+[x[3]+2]
print(x)

a,b,c,d,e,f=x

print(a,b,c,d)


x.pop()

print(x)
x.pop(0)

print(x)


########### List Comprehension ###########

sq2 = [ x ** 2 for x in range(10)]
print(sq2)

sq2even = [ x for x in sq2 if x % 2 == 0]
print(sq2even)


sqodd = [ x for x in sq2 if x % 2 != 0 ]
print(sqodd)


## Another Example of List Comprehension ##

a = [1 , 2, 3]
b = [4, 5, 1]
c = []

for x in a:
    for y in b:
        if (x != y ):
            c.append((x,y))
print(c)

### The above example done in one line using list comprehension ##

c = [(x,y) for x in a for y in b if x!=y ]

print(c)

################################################################

for z in range(0,20,2):
    print(z, end = ' ')

arr = [z for z in range(0,20,2)]
print(arr, end=' ')

### Dictionary Compreension
print("\n")
print ("This is an example of Dictionary Comprehension ")

print("\n")
d1 = { x:x**2 for x in range(10)}
print (d1)

print("\n")
print (" This is an example of Array Comprehension ")
y = [ num **2 for num in range(0,6)]
print(y)
