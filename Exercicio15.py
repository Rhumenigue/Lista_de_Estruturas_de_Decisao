def maravilhosos(numero):
    print(int(numero))
    while numero != 1:
        if not numero % 2:
           return maravilhosos(numero/2)
        else:
            return maravilhosos(3*numero + 1)
N = int(input())
maravilhosos(N)

