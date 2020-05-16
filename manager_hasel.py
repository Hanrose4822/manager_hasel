import random
import os
import getpass

haslo = getpass.getpass()
while haslo != 'ad0118':
    haslo = getpass.getpass()

print('Aby wyświetlic listę poleceń wpisz "list"')
while True:
    #pokazuje listę komend
    def list():
        print('Wybierz funkcję: szyfrowanie[s] \n rozszyfrowywanie[r] \n usuwanie informacji do roszyfrowywania (klucz i zaszyfrowane hasła)[delete] \n dodanie nowego hasła[nh]: ')

    #wprowadzanie nowego hasła do pliku
    def nowehaslo():
        nhaslo = []
        print('wpisz platformę: ')
        platforma = input('\n')
        print('wpisz login: ')
        login = input('\n')
        print('wpisz hasło: ')
        nowehaslo = input('\n')

        strnh = str(platforma)+ str(login)+ str(nowehaslo)+'\n'
        nhaslo.append(nowehaslo)
        with open(r'E:\pswrd\pswrd.txt', 'a') as h:
            h.write(strnh)

    #usuwanie zaszyfrowanego hasła i klucza
    def usuwanie_danych():
        print('Co chcesz usunąć? Klucz[klucz] / zaszyfrowane hasło[cpdpswrd] / wszystko[all]')
        y = input()
        if y == 'klucz':
            os.remove('F:\pswrd-info\key.txt')
        elif y == 'cpdpswrd':
            os.remove('F:\pswrd-info\crpswrd.txt')
        elif y == 'all':
            os.remove('F:\pswrd-info\crpswrd.txt')
            os.remove('F:\pswrd-info\key.txt')

    #szyfrowanie haseł (Wymaga dysku E i F)
    def szyfrowanie():
        def szyfr(x):
            klucz = random.randint(0, 9)
            return chr(ord(x) + klucz), klucz

        with open(r'E:\pswrd\pswrd.txt', 'r') as f:
            t = f.read()

        crznak = ''
        klucz = ''
        for i in t:
            z,k = szyfr(i)
            crznak = crznak + z
            klucz = klucz + str(k)

        with open(r'F:\pswrd-info\crpswrd.txt', 'w') as d:
            d.write(crznak)

        with open(r'F:\pswrd-info\key.txt', 'w') as d:
            d.write(klucz)

        os.remove("E:\\pswrd\\pswrd.txt")

    #rozszyfrowywanie haseł (Wymaga dysku E, F i D)
    def rozszyfrowywanie():
        def rozszyfr(znak, klucz):
            return chr(ord(znak) - klucz)

        with open(r'F:\pswrd-info\key.txt', 'r') as f:
            klucz = f.read()
        with open(r'F:\pswrd-info\crpswrd.txt', 'r') as f:
            znak = f.read()

        tekst = ''
        for z,k in zip(znak,klucz):
            with open(r'D:\manager\dcpdpswrd.txt', 'w') as f:
                f.write(tekst)
            tekst = tekst + rozszyfr(z,int(k))

    #wywoływanie odpowiednich funkcji
    x = input()
    if x == 's':
        szyfrowanie()
    elif  x == 'r':
        rozszyfrowywanie()
    elif x == 'delete':
        print('Na pewno?(t/n)')
        if input() == 't':
            usuwanie_danych()
    elif x == 'nh':
        nowehaslo()
    elif x == 'list':
        list()
    if x == 'exit':
        break

