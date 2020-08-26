from model import Shramba

#dokler testiram, v trenutno datoteko kopiram naslednje podatke:
from datetime import date
from model import Shramba

moja_shramba = Shramba()

knjige = moja_shramba.dodaj_vrsto('knjige')
filmi = moja_shramba.dodaj_vrsto('filmi')

moja_shramba.dodaj_vnos(knjige, 'Krive so zvezde', 'John Green', 'ljubezenski roman', date(2019, 5, 5), '5')
moja_shramba.dodaj_vnos(knjige, 'Harry Potter', 'J. K. Rowling', 'znanstvena fantastika', date(2020, 1, 3), '5')
moja_shramba.dodaj_vnos(filmi, 'To all the boys', 'nek režiser', 'romatična komedija', date(2019, 6, 5), '4')
#konec začasnih podatkov, izbrisala bom, ko bo program končan
#in se bo te podatke bralo iz datoteke

#napišemo pomožno funkcijo, ki preverja, da je vnešeno število, ko to zahtevamo
def vnesi_stevilo(pozdrav):
    while True:
        stevilo = input(pozdrav)
        if stevilo.isdigit():
            return int(stevilo)
        else:
            print(f'Prosim, da vneseš število!')

#napišem funkcijo, ki izbira:
def izberi(seznam):
    for indeks, element in enumerate(seznam, 1):
        print(f'{indeks}) {element}')
    while True:
        izbira = vnesi_stevilo('> ')
        if  1 <= izbira <= len(seznam):
            return seznam[izbira - 1]
        else:
            print(f'Izberi število med 1 in {len(seznam)}')


def glavni_meni():
    while True:
        #uporabniku ponudi možnosti
        print('''
        Kaj bi rad naredil?
        1) dodal vnos
        2) dodal vrsto
        3) pogledal stanje
        4) šel iz programa
        ''')
        izbira = input('> ')
        if izbira == '1':
            dodaj_vnos()
        elif izbira == '2':
            dodaj_vrsto()
        elif izbira == '3':
            poglej_stanje()
        elif izbira == '4':
            print('Nasvidenje!')
            break   
        else:
            print('Neveljavna izbira')



def dodaj_vnos():
    #napisali bomo funkcijo, ki izbira
    print('Vrsta:')
    vrsta = izberi(moja_shramba.vrste) 
    naslov = input('Naslov> ')
    avtor = input('Avtor> ')
    zanr = input('Žanr> ')
    datum = date.today()
    ocena = vnesi_stevilo('Ocena(1-5)> ')
    moja_shramba.dodaj_vnos(vrsta, naslov, avtor, zanr, datum, ocena)
    print('Vnos uspešno dodan.')
    
def dodaj_vrsto():
    ime_vrste = input('Vnesi ime vrste> ')
    moja_shramba.dodaj_vrsto(ime_vrste)
    print('Vrsta uspešno dodana!')


def poglej_stanje():
    for vrsta in moja_shramba.vrste:
        print(vrsta)

glavni_meni()