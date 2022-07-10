def pitorestico(a: int, b: int, c: int) -> None:
    
    if (a % 2 == 0 and a % 3 == 0 and a % 5 == 0) and \
       (b % 2 == 0 and b % 3 == 0 and b % 5 == 0) and \
       (c % 2 == 0 and c % 3 == 0 and c % 5 == 0):
        print("Pitorestico!!!")
    else:
        print("Nao foi dessa vez")