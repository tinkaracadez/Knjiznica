from datetime import date
from model import Knjiznica

#velike tiskane črke uporabljamo za konstante
LOGO = '''
  _  __      _ _           _           
 | |/ /     (_|_)         (_)          
 | ' / _ __  _ _ _____ __  _  ___ __ _ 
 |  < | '_ \| | |_  / '_ \| |/ __/ _` |
 | . \| | | | | |/ /| | | | | (_| (_| |
 |_|\_\_| |_| |_/___|_| |_|_|\___\__,_|
           _/ |                        
          |__/                         
'''
DATOTEKA_S_STANJEM = 'stanje.json'

#naročimo programu, naj v shrambo da podatke iz jsona (naloži stanje iz datoteke)
#če mu to ne uspe, naj bo shramba prazna
#try:
    #knjiznica = Knjiznica.nalozi_stanje(DATOTEKA_S_STANJEM)
#except FileNotFoundError:
knjiznica = Knjiznica()

#pomožne funkcije za vnos

def krepko(niz):
    return f'\033[1m{niz}\033[0m'

def uspeh(niz):
    return f'\033[1;94m{niz}\033[0m'

def napaka(niz):
    return f'\033[1;91m{niz}\033[0m'



#tu bi lahko dodala funkciji prikaz_naslova in prikaz_vrste
#če bi želela, da se le-to drugače obarva



def vnesi_stevilo(pozdrav):
    while True:
        try:
            stevilo = input(pozdrav)
            return int(stevilo)
        except ValueError:
            print(napaka(f'Prosim, da vneseš število!'))


def izberi(seznam):
    for indeks, (oznaka, _) in enumerate(seznam, 1):
        print(f'{indeks}) {oznaka}')
    while True:
        izbira = vnesi_stevilo('> ')
        if 1 <= izbira <= len(seznam):
            _, element = seznam[izbira - 1]
            return element
        else:
            print(napaka(f'Izberi število med 1 in {len(seznam)}'))


#če bi imela funkcijo za prikaz vrste, bi jo uporabila tu
#def izberi_vrsto(vrste):
    #return izberi([vrste])



#sestavni deli uporabniškega vmesnika


def glavni_meni():
    print(krepko(LOGO))
    print(krepko('Dobrodošli v programu knjižnica!'))
    print('Za izhod pritisnite Ctrl-C.')
    while True:
        try:
            print(80* '=')
            print()
            print(krepko('Kaj želite narediti?'))
            moznosti = [
                ('dodati vnos', dodaj_vnos),
                ('dodati vrsto', dodaj_vrsto),
                ('pogledati stanje', poglej_stanje),
                #('poiskati že vnešeno delo', poisci_vnos),
            ]
            izbira = izberi(moznosti)
            print(80* '-')
            izbira()
            print()
            input('Pritisnite Enter za shranjevanje in vrnitev v osnovni meni...')
            knjiznica.shrani_stanje(DATOTEKA_S_STANJEM)
        except ValueError as e:
            print(napaka(e.args[0]))
        except KeyboardInterrupt: #če uporabnik pritisne ctrl+C
            print()
            print('Nasvidenje!')
            return
        

def dodaj_vnos():
    naslov = input('Naslov> ')
    avtor = input('Avtor> ')
    print('Vrsta:')
    vrsta = izberi([(vrsta.ime, vrsta) for vrsta in knjiznica.vrste]) 
    datum = date.today().strftime('%Y-%m-%d')
    knjiznica.dodaj_vnos(naslov, avtor, vrsta, datum)
    print(uspeh('Vnos uspešno dodan.'))
    

def dodaj_vrsto():
    ime_vrste = input('Vnesi ime vrste> ')
    knjiznica.dodaj_vrsto(ime_vrste)
    print(uspeh('Vrsta uspešno dodana!'))


def poglej_stanje():
    for vrsta in knjiznica.vrste:
        print(krepko('VRSTA:'))
        print(f'- {vrsta.ime}')
        print(krepko('Vnosi:'))
        for vnos in knjiznica.vnosi:
            if vnos.vrsta == vrsta:
                print(f'- {vnos.naslov}')
        print()


glavni_meni()