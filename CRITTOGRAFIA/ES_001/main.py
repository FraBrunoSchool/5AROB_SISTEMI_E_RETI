dictLet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "L": 9, "M": 10, "N": 11, "O": 12,
           "P": 13, "Q": 14, "R": 15, "S": 16, "T": 17, "U": 18, "V": 19, "Z": 20}
dictNum = {}


def main():
    dictLetInNum()
    chiave = "ITISDELPOZZO"
    messaggio = "CIAO"

    # print(dictLet)
    # print(dictNum)
    msgNum = stringaInNumber(messaggio)
    keyNum = stringaInNumber(chiave)
    print(f"Messaggio: {msgNum} + Chiave {keyNum}")
    somma = sommaKeyMsg(keyNum, msgNum)
    print(somma)
    mod = modulo(somma)
    print(mod)
    StrLettere = NumToLet(mod)
    print(StrLettere)

    StrLettereCifr = stringaInNumber(StrLettere)
    print(StrLettereCifr)
    sotr = sottrKeyMsg(keyNum, StrLettereCifr)
    print(sotr)
    modCifr = modulo(sotr)
    print(modCifr)
    StrLettereDecifrato = NumToLet(modCifr)
    print(StrLettereDecifrato)


def dictLetInNum():
    for let in dictLet:
        dictNum[dictLet[let]] = let


def stringaInNumber(stringa):
    num = []
    for l in stringa:
        num.append(dictLet[l])
    return num


def sommaKeyMsg(chiave, messaggio):
    somma = []
    if len(chiave) > len(messaggio):
        for count, n in enumerate(messaggio):
            somma.append(n + chiave[count])
    else:
        print("chive non abbastanza lunga")
    return somma


def modulo(somma):
    mod = []
    for el in somma:
        mod.append(el % len(dictLet))
    return mod


def NumToLet(mod):
    StrLettere = ""
    for el in mod:
        StrLettere += dictNum[el]
    return StrLettere


def sottrKeyMsg(chiave, messaggio):
    somma = []
    if len(chiave) > len(messaggio):
        for count, n in enumerate(messaggio):
            somma.append(n - chiave[count])
    else:
        print("chive non abbastanza lunga")
    return somma


if __name__ == '__main__':
    main()
