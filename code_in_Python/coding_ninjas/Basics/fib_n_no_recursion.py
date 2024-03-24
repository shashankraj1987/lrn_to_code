num = 20
fib = 1
first = 1
second = 1
counter = 3

while counter <= num:
    fib = first+second
    first = second
    second = fib
    counter += 1

print(fib)
