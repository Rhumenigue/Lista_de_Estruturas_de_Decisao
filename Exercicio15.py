x=int(input())
print(f'{int(x)}')
while x!=1:
    if x%2 == 0 and x != 0:
        print(f'{int(x/2)}')
        x=x/2
    else:
        print(f'{int(x*3+1)}')
        x=x*3+1
