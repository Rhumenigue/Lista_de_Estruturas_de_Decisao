def banner(n):
    if n > 0:
        if not n % 2:
            print("| | | | | | | | | |")
        else:
            print("- - - - - - - - - -")
    else:
        if not n % 2:
            print(". . . . . . . . . .")
        else:
            print("= = = = = = = = = =")