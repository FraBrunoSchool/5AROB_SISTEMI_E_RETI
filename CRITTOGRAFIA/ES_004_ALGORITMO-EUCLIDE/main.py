def main():
    a = int(input("Inserire il primo numero: "))
    b = int(input("Inserire il primo numero: "))
    AlgoritmoEuclide(a if a > b else b, a if a < b else b)


def AlgoritmoEuclide(a, b):
    r = None
    while r != 0:
        r = a % b
        a = b
        b = r
    print(a)


if __name__ == '__main__':
    main()