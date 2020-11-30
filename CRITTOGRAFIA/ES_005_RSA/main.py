import random

dictLet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "L": 9, "M": 10, "N": 11, "O": 12,
           "P": 13, "Q": 14, "R": 15, "S": 16, "T": 17, "U": 18, "V": 19, "Z": 20}
dictNum = {}


def main():
    dictLetInNum()
   # p = input_num("p")
   # q = input_num("q")
    p=13
    q=7
    n = p * q
    m = mcm(p, q)
    #c = find_c(m)
    c = 7
    d = find_d(m, c)

    print(f"Chiave Pubblica: n = {n} c = {c}")
    print(f"Chiave Privata: m = {m} d = {d}")
    """
    print("test criptazione / decriptazione")
    b = criptazione_numero(n, c, 13)
    print(f"Numero Criptato: b = {b}")
    a = decriptazione_numero(n, d, b)
    print(f"Numero Decriptato: a = {a}")

    parola = input("inserisci parola da criptare e poi decriptare: ")
    parola_criptata = criptazione_parola(parola, n, c)
    print(f"Parola criptata: {parola_criptata}")
    parola_decriptata = decriptazione_parola(parola_criptata, n, d)
    print(f"Parola decriptata: {parola_decriptata}")
"""

def dictLetInNum():
    for let in dictLet:
        dictNum[dictLet[let]] = let


def input_num(nome_variabile_input):
    check = False
    while not check:
        num = int(input(f"Inserisci {nome_variabile_input}: "))
        if is_primo(num):
            check = True
    return num


def is_primo(num):
    div, check = 2, 0
    while num / 2 >= div and check == 0:
        if num % div == 0:
            check += 1
        div += 1
    if check == 0 and num != 1:
        return True
    else:
        return False


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


def find_c(m):
    lista_c = []
    for c in range(2, m):
        if mcd(c, m) == 1:
            lista_c.append(c)
    return random.choice(lista_c)
    #return lista_c


def find_d(m, c):
    for d in range(0, m):
        if (c * d) % m == 1:
            return d
    return None


def criptazione_numero(n, c, a):
    if 0 <= a < n:
        return pow(a, c) % n


def decriptazione_numero(n, d, b):
    return pow(b, d) % n


def str_in_number(stringa):
    num = []
    for l in stringa:
        if l == ' ':
            num.append(None)
        else:
            num.append(dictLet[l.upper()])
    return num


def number_in_str(lista_numeri):
    StrLettere = ""
    for el in lista_numeri:
        if el == None:
            StrLettere += ' '
        else:
            StrLettere += dictNum[el]
    return StrLettere


def criptazione_parola(parola, n, c):
    print(parola)
    str_num = str_in_number(parola)
    print(str_num)
    lista_num_crip = []
    for el in str_num:
        if el == None:
            lista_num_crip.append(None)
        else:
            lista_num_crip.append(criptazione_numero(n, c, el))
    print(lista_num_crip)
    # parola_criptata = number_in_str(lista_num_crip)
    return lista_num_crip


def decriptazione_parola(lista_num, n, d):
    lista_num_decrip = []
    for el in lista_num:
        if el == None:
            lista_num_decrip.append(None)
        else:
            lista_num_decrip.append(decriptazione_numero(n, d, el))
    parola_decriptata = number_in_str(lista_num_decrip)
    return parola_decriptata


if __name__ == '__main__':
    main()
