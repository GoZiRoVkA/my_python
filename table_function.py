value = input("Введите атомный номер элемента X: ")
if value:
    X = float(value)
    if X == 3.0:
        print("Li")
    elif X == 25:
        print("Mn")
    elif X == 80:
        print("Hg")
    elif X == 17:
        print("Cl")
    else:
        print("Что это?!")
else:
    print("Введите  атомный номер элемента")
    
