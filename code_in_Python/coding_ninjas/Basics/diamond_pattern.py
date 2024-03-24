n = 7
n1 = (n+1)/2
n2 = n1 - 1

# Dealing with the Top Half of the Code
# =======================================

# Spaces = n1-i
# Stars = 2i-1

i = 1
while i <= n1:
    spc = 1
    while spc <= n1-i:
        print('-', end=' ')
        spc += 1

    stars = 1
    while stars <= (2*i)-1:
        print('*', end=' ')
        stars += 1
    print()
    i += 1

# Dealing with the Bottom Half of the Code
# =======================================

# Spaces = n2-i+1
# Stars = 2i-1

i = n2
while i >= 1:
    spc = 1
    while spc <= (n2-i)+1:
        print('-', end=' ')
        spc += 1

    stars = (2*i)-1
    while stars >= 1:
        print('*', end=' ')
        
        stars -= 1
    i -= 1
    print()
