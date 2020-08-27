from model import Shramba

#dokler testiram, v trenutno datoteko kopiram naslednje podatke:
from datetime import date
from model import Shramba

moja_shramba = Shramba()

#polnjenje začetne shrambe s testnimi podatki (kasneje gre to ven)

knjige = moja_shramba.dodaj_vrsto('knjige')
filmi = moja_shramba.dodaj_vrsto('filmi')

moja_shramba.dodaj_vnos(knjige, 'Krive so zvezde', 'John Green', 'ljubezenski roman', date(2019, 5, 5), '5')
moja_shramba.dodaj_vnos(knjige, 'Harry Potter', 'J. K. Rowling', 'znanstvena fantastika', date(2020, 1, 3), '5')
moja_shramba.dodaj_vnos(filmi, 'To all the boys', 'nek režiser', 'romatična komedija', date(2019, 6, 5), '4')
#konec začasnih podatkov, izbrisala bom, ko bo program končan
#in se bo te podatke bralo iz datoteke

#pomožne funkcije za vnos

#naslednji funkciji poskrbita za obarvanje besedila
def uspeh(niz):
    print('\033[1;94m' + niz + '\033[0m')

def napaka(niz):
    print('\033[1;91m' + niz + '\033[0m')

#napišemo pomožno funkcijo, ki preverja, da je vnešeno število, ko to zahtevamo
def vnesi_stevilo(pozdrav):
    while True:
        stevilo = input(pozdrav)
        if stevilo.isdigit():
            return int(stevilo)
        else:
            napaka(f'Prosim, da vneseš število!')

#lepša oblika funkcije za kasnejšo uporabo
#podčrtaj _ v oklepaju bo nadomestila neka funkcija
def izberi(seznam):
    for indeks, (oznaka, _) in enumerate(seznam, 1):
        print(f'{indeks}) {oznaka}')
    while True:
        izbira = vnesi_stevilo('> ')
        if 1 <= izbira <= len(seznam):
            _, element = seznam[izbira - 1]
            return element
        else:
            napaka(f'Izberi število med 1 in {len(seznam)}')

#sestavni del uporabniškega vmesnika
def glavni_meni():
    while True:
        try:
            #uporabniku ponudi možnosti
            moznosti = [
                ('dodal vnos', dodaj_vnos),
                ('dodal vrsto', dodaj_vrsto),
                ('pogledal stanje', poglej_stanje)
            ]
            print('Kaj bi rad naredil?')
            izbira = izberi(moznosti)
            izbira()
        except ValueError as e:
            napaka(e.args[0])
        except KeyboardInterrupt: #če uporabnik pritisne ctrl+C
            print('Nasvidenje!')
            return
        

def dodaj_vnos():
    #napisali bomo funkcijo, ki izbira
    print('Vrsta:')
    vrsta = izberi([(vrsta.ime, vrsta) for vrsta in moja_shramba.vrste]) 
    naslov = input('Naslov> ')
    avtor = input('Avtor> ')
    zanr = input('Žanr> ')
    datum = date.today()
    ocena = vnesi_stevilo('Ocena(1-5)> ')
    moja_shramba.dodaj_vnos(vrsta, naslov, avtor, zanr, datum, ocena)
    uspeh('Vnos uspešno dodan.')
    
def dodaj_vrsto():
    ime_vrste = input('Vnesi ime vrste> ')
    moja_shramba.dodaj_vrsto(ime_vrste)
    uspeh('Vrsta uspešno dodana!')


def poglej_stanje():
    for vrsta in moja_shramba.vrste:
        print(vrsta)

glavni_meni()