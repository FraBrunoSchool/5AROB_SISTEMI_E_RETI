dictLet = {}
dictNum = {}

def main():
    n = 536131
    c = 5939
    p, q = fattorizzazione(n)
    print(f"p = {p} - q = {q}")
    m = mcm(p, q)
    d = find_d(m, c)
    print(f"Chiave Pubblica: n = {n} c = {c}")
    print(f"Chiave Privata: m = {m} d = {d}")
    str = decriptazione_parola([459541, 134033, 243696, 243696, 497836, 121848, 497836, 252297, 243696, 357421], n, d)
    print(str)


def dictLetInNum():
    dictLet = {}
    dictNum = {}
    for i in range(65, 91):
        dictLet[chr(i)] = i - 65
        dictNum[i - 65] = chr(i)
    return dictLet, dictNum


def decriptazione_parola(lista_num, n, d):
    lista_num_decrip = []
    for el in lista_num:
        if el == None:
            lista_num_decrip.append(None)
        else:
            lista_num_decrip.append(decriptazione_numero(n, d, el))
    parola_decriptata = number_in_str(lista_num_decrip)
    return parola_decriptata

def decriptazione_numero(n, d, b):
    return pow(b, d) % n

def number_in_str(lista_numeri):
    StrLettere = ""
    for el in lista_numeri:
        if el == None:
            StrLettere += ' '
        else:
            StrLettere += dictNum[el]
    return StrLettere


def find_d(m, c):
    for d in range(0, m):
        if (c * d) % m == 1:
            return d
    return None


def mcm(a, b):
    a, b = a - 1, b - 1
    return (a * b) // mcd(a if a > b else b, a if a < b else b)


def mcd(a, b):
    r = None
    while r != 0:
        r = a % b
        a = b
        b = r
    return a

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
    return fattori[0], fattori[1]


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
    dictLet, dictNum = dictLetInNum()
    main()