def classificador(a,b,c):
    max_val = max(a, b, c)
    if a + b > c and b + c > a:
        print("triangulo")
        if a == b or b == c or a == c:
            print("isosceles")
        if a == b and b == c and c == a:
            print("equilatero")
        if a != b and b != c and c != a:
            print("escaleno")
        if (max_val) **2 == a **2 + b **2 or max_val**2 == b**2 + c**2 or max_val**2 == a**2 + c**2:
            print("retangulo")
    else:
        print("gondim sendo gondim")