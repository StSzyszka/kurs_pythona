# Napisz program, który będzie bazą (kontakty, samochody, itp.), program ma pytać użytkownika, co chce zrobić, dając mu minimum te opcje:
# dodanie imienia, usuniecie imienia,
# sprawdzenie czy imię jest w bazie,
# usunięcie imienia,
# sprawdzenie ilości imion w bazie oraz zakończenie programu.
# Jeśli czujesz się pewniej to postaraj się aby użytkownik mógł podać więcej szczegółów np. nazwisko, nr telefonu, adres itp.

import csv


def print_menu():

    print("""Witaj w bazie danych:
    wybierz opcję którą chcesz zrobić:
    -> wpisz '+' jeżeli chcesz dodać osobę do bazy danych
    -> wpisz '-' jeżeli chcesz usunąć osobę z bazy danych
    -> wpisz 'check' jeżeli chcesz sprawdzić czy dana osoba jest w bazie danych
    -> wpisz 'nr' jeżeli chcesz dowiedzieć się ile osób jest w bazie danych
    Pamiętaj że zawsze możesz zakończyć program wpisując 'exit' """)


def dodanie_do_bazy():
    """Pozwala dodać osobę do bazy danych"""
    with open ('baza_imion.csv', 'a', encoding='utf-8') as plik:
        filewriter = csv.writer(plik, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        filewriter.writerow([name])

    print('imię zostało dodane')


def usuniecie_z_bazy():
    """Pozwala dodać osobę do bazy danych"""
    usuwane = input('podaj imie które chcesz usunąć: ')

    with open('baza_imion.csv', 'r+', encoding='utf-8') as plik:
        reader = csv.reader(plik)

        lista_z_imionami = []
        rownr = 0
        for row in reader:
            if row == []:
                row = + 1
            elif row != []:
                lista_z_imionami.append(row[0])
                #                print(lista_z_imionami)
            rownr = rownr + 1
        print(lista_z_imionami)

        for i in lista_z_imionami:
            if i == usuwane:
                lista_z_imionami.remove(str(usuwane))

        print(lista_z_imionami)

        with open('baza_imion.csv', 'w', encoding='utf-8') as plik:
            filewriter = csv.writer(plik, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            for j in lista_z_imionami:
                filewriter.writerow([j])


def sprawdzenie_czy_jest_w_bazie():
    with open('baza_imion.csv', 'r', encoding='utf-8') as plik:
        reader = csv.reader(plik)

        for row in reader:
            if row == []:
                row =+ 1
            elif row == baza_szukane:
                print("szukane imie {} jest w bazie".format(szukane))
            else:
                pass


def wyswietlenie_bazy():
    with open('baza_imion.csv', 'r', encoding='utf-8') as plik:
        reader = csv.reader(plik)

        lista_z_imionami = []
        rownr = 0
        for row in reader:
            if row == []:
                row = + 1
            elif row != []:
                lista_z_imionami.append(row[0])
                #                print(lista_z_imionami)
            rownr = rownr + 1
        print(lista_z_imionami)



def sprawdzenie_ilosci_osob_w_bazie():
    """Pozwala sprawdzić ilosc osob w bazie danych"""
    with open('baza_imion.csv', 'r', encoding='utf-8') as plik:
        reader = csv.reader(plik)
        lista_z_imionami = []

        rownr = 0

        for row in reader:
            if row == []:
                row = + 1
            elif row != []:
                lista_z_imionami.append(row[0])
                #                print(lista_z_imionami)
            rownr = rownr + 1
        for counter, value in enumerate(lista_z_imionami, 1):
            pass

        print('liczba imion znajdujących się w bazie wynosi: {}'.format(counter))



# główna pętla programu

print_menu()

while True:

    koniec = 'exit'
    print('''
    wybierz opcje: ''')
    wybor = input()
    lista_z_imionami = []

    if wybor == '+':
        name = input(str('podaj imie: '))
        dodanie_do_bazy()

    elif wybor == '-':
        usuniecie_z_bazy()

    elif wybor == 'check':
        baza_szukane = []
        szukane = input(str('podaj szukane imie: '))
        baza_szukane.append(szukane)
        sprawdzenie_czy_jest_w_bazie()

    elif wybor == 'nr':
        sprawdzenie_ilosci_osob_w_bazie()

    elif wybor == 'look':
        wyswietlenie_bazy()

    elif wybor == koniec:
        print('koniec działania programu')
        exit(1)

    else:
        print('nie wybrałeś żadnej z dostępnych opcji, dziękujemy')
        exit()





