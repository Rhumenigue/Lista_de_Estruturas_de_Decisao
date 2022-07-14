def jogadas(a, b):
    diferenca=abs(a-b)
    total, resto = divmod(diferenca, 10)
    if resto==0:
        jogadas=total
    else:
        jogadas=total+1
    print (jogadas)
