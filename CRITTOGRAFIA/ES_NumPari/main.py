def main():
    numero = int(input("‘Inserire un n numeri: ‘"))
    listaPrimi = []
    n_primi = 0
    n = 2
    while n_primi < numero:
        div, check = 2, 0
        while n / 2 >= div and check == 0:
            if n % div == 0:
                check += 1
            div += 1
        if check == 0:
            listaPrimi.append(n)
            n_primi += 1
        n += 1
    print(listaPrimi)
    print(listaPrimi[len(listaPrimi)-1])


if __name__ == '__main__':
    main()
