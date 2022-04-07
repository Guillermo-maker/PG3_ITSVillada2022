Num = int(input("Ingrese un número: "))


def isStep(n):
    a = map(int, str(n)[1:])
    b = map(int, str(n)[:-1])
    return all(abs(a_digit - b_digit) == 1 for a_digit, b_digit in zip(a, b))


if isStep(Num) == True:
    print(Num, " Es step")
else:
    print(Num, " No es step")
