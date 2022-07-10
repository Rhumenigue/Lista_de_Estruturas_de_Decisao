def formamisteriosa(a,b,c):
    if a == b:
        print("pode ser quadrado")
    elif a != b:
        print("pode ser retangulo")
    if (a + b) > c and (b + c) > a :
        if a==b and a==c and b==c:
            print("pode ser triangulo equilatero")
        elif a!=b and a!=c and b!=c:
            print("pode ser triangulo escaleno")
        elif a==b or b==c or a==c:
            print("pode ser triangulo isosceles")