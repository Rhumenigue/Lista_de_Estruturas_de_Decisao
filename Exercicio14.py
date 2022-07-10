def qtdcopos(n: int) -> None:
    
    if n % 4 == 0 and n > 0:
        print("Pode levar pros calourinhos, deivis!")
    else:
        print(f"Pode voltar pro ceubinho, deivis! Falta(m) {4 - (n % 4)} copo(s)!")
            