import csv
import os
import IP2Location

lista_ip = []
lista_protocol = []


def main():
    with open('scan2.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        first = True
        for riga in csv_reader:
            if first:
                first = False
                continue
            if riga["Source"] not in lista_ip and len(riga["Source"].split(".")) == 4:
                lista_ip.append(riga["Source"])

            if riga["Destination"] not in lista_ip and len(riga["Destination"].split(".")) == 4:
                lista_ip.append(riga["Destination"])

            if riga["Protocol"] not in lista_protocol:
                lista_protocol.append(riga["Protocol"])

    print(lista_ip)
    print(lista_protocol)
    print(localizza(lista_ip))


def localizza(lista_ip):
    lista_loc = []
    for ip in lista_ip:
        database = IP2Location.IP2Location(os.path.join("sample.bin.db1", "IP-COUNTRY-SAMPLE.BIN"))
        rec = database.get_all(ip)
        if rec.country_short != '-' and rec.country_long != '-':
            lista_loc.append((ip, rec.country_short, rec.country_long))
            continue

        database = IP2Location.IP2Location(os.path.join("sample.bin.db2", "IP-COUNTRY-ISP-SAMPLE.BIN"))
        rec = database.get_all(ip)
        if rec.country_short != '-' and rec.country_long != '-':
            lista_loc.append((ip, rec.country_short, rec.country_long))
            continue

    return lista_loc


if __name__ == '__main__':
    main()
