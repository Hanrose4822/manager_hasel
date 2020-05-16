import random
import os
import getpass


# usuwanie wszystkich danych (nie działa bez któregokolwiek z tych plików)
def deleteplus():
    print('Na pewno?[t/n]')
    b = input()
    if b == 't':
        os.remove(r'F:\pswrd-info\crpswrd.txt')
        os.remove(r'F:\pswrd-info\key.txt')
        os.remove(r'E:\pswrd\pswrd.txt')
        os.remove(r'D:\manager\dcpdpswrd.txt')
    if b == 'n':
        print('dane nie zostaną usunięte')


# generator haseł
def generatorhasel():
    with open(r'D:\Programy_python\manager_hasel\info\znaki.txt', 'r') as f:
        znaki = f.read()
    wyraz = ''
    for x in range(random.randint(1, 100)):
        wyraz = wyraz + znaki[random.randint(0, len(znaki)-1)]
    sh = ''.join(random.choices(znaki, k=random.randint(1, 30)))
    with open(r'F:\pswrd-info\silne_haslo.txt', 'w') as g:
        g.write(sh)
    print('Hasło zostało wygenerowane (F:\\pswrd-info\\silne_haslo.txt)')


# pokazuje listę komend
def lista():
    print('Wybierz funkcję:\n [s]szyfrowanie \n [r]rozszyfrowywanie \n [delete]usuwanie informacji do roszyfrowywania '
          '(klucz i zaszyfrowane hasła) \n [nh]dodanie nowego hasła \n [delete+]usuwanie wszystkich danych '
          '\n [gh]generowanie silnego hasła')


# wprowadzanie nowego hasła do pliku
def nowehaslo():
    nhaslo = []
    print('wpisz platformę: ')
    platforma = input('\n')
    print('wpisz login: ')
    login = input('\n')
    print('wpisz hasło: ')
    newhaslo = input('\n')

    strnh = str(platforma) + str(login) + str(newhaslo) + '\n'
    nhaslo.append(nowehaslo)
    with open(r'sz', 'a') as h:
        h.write(strnh)


# usuwanie zaszyfrowanego hasła i klucza
def usuwanie_danych():
    print('Co chcesz usunąć? Klucz[klucz] / zaszyfrowane hasło[cpdpswrd] / wszystko[all]')
    y = input()
    if y == 'klucz':
        os.remove(r'F:\pswrd-info\key.txt')
    elif y == 'cpdpswrd':
        os.remove(r'F:\pswrd-info\crpswrd.txt')
    elif y == 'all':
        os.remove(r'F:\pswrd-info\crpswrd.txt')
        os.remove(r'F:\pswrd-info\key.txt')


# szyfrowanie haseł (Wymaga dysku E i F)
def szyfrowanie():
    def szyfr(h):
        key = random.randint(0, 9)
        return chr(ord(h) + key), key

    with open(r'E:\pswrd\pswrd.txt', 'r') as f:
        t = f.read()

    crznak = ''
    klucz = ''
    for i in t:
        z, k = szyfr(i)
        crznak = crznak + z
        klucz = klucz + str(k)

    with open(r'F:\pswrd-info\crpswrd.txt', 'w') as d:
        d.write(crznak)

    with open(r'F:\pswrd-info\key.txt', 'w') as d:
        d.write(klucz)

    os.remove('E:\\pswrd\\pswrd.txt')


def rozszyfr(litery, key):
    return chr(ord(litery) - key)


# rozszyfrowywanie haseł (Wymaga dysku E, F i D)
def rozszyfrowywanie():
    with open(r'F:\pswrd-info\key.txt', 'r') as f:
        klucz = f.read()
    with open(r'F:\pswrd-info\crpswrd.txt', 'r') as f:
        litery = f.read()

    tekst = ''
    for z, k in zip(litery, klucz):
        with open(r'D:\manager\dcpdpswrd.txt', 'w') as f:
            f.write(tekst)
        tekst = tekst + rozszyfr(z, int(k))


if __name__ == '__main__':

    haslo = getpass.getpass()
    while haslo != 'ad0118':
        haslo = getpass.getpass()

    print('Aby wyświetlic listę poleceń wpisz "list"')

    while True:
        try:
            # wywoływanie odpowiednich funkcji
            x = input('\nWpisz komendę: ')
            if x == 's':
                szyfrowanie()
            elif x == 'r':
                rozszyfrowywanie()
            elif x == 'delete':
                print('Na pewno?(t/n)')
                if input() == 't':
                    usuwanie_danych()
            elif x == 'nh':
                nowehaslo()
            elif x == 'list':
                lista()
            elif x == 'gh':
                generatorhasel()
            elif x == 'delete+':
                deleteplus()
                b = input()
            if x == 'exit':
                break
        except FileNotFoundError:
            print('wystąpił błąd. Sprawdź czy plik znajduje się na odpowiednim dysku.')
        except:
            print('Wystąpił błąd')

