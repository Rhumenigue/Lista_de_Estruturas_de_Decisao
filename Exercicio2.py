def area (a, b, shape):
    if shape == "retangulo":
        print(f'O retangulo tem {int(a*b)} de area')
    elif shape == "losango":
        print(f'O losango tem {int(a*b/2)} de area')
    else:
        print(f'O triangulo tem {int(a*b/2)} de area')
