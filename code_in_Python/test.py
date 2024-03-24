def main():
    x = 0
    y = 1

    print(f'The ID of X is {id(x)} and the Value is {x}')
    print(f'The ID of Y is {id(y)} and the value is {y}')

    x += 1
    y=y+2


    print(f'Now the ID of x is {id(x)} and the value is {x}')
    print(f'Now the ID of Y is {id(y)} and the value is {y}')

if __name__=="__main__":
    main()
