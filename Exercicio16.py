def piscininha(x, y, w, h, a, b):
    dentro=((a<=x+w) and (a>=x)) and ((b<=y+h) and (b>=y))
    borda=dentro and (a==x or a==x+w or b==y or b==y+w)
    if dentro and not borda:
        print ( 'Dando um tchibum')
    elif borda:
        print('So com os pezin dentro da agua')
    else:
        print('Tomando um solzin')