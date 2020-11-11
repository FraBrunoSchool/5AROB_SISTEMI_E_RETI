def main():
    print(fattorizzazione(int(input("Inserire un numero da fattorizzare : "))))


def fattorizzazione(num):
    div = 2
    fattori = []
    while num >= div:
        if Isprimo(div):
            if num % div == 0:
                fattori.append(div)
                num /= div
            else:
                div = div + 1
        else:
            div = div + 1
    return fattori

def Isprimo(num):
    div, check = 2, 0
    while num / 2 >= div and check == 0:
        if num % div == 0:
            check += 1
        div += 1
    if check == 0 and num != 1:
        return True
    else:
        return False


if __name__ == '__main__':
    main()