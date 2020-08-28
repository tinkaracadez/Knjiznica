import json
from datetime import date
from model import Knjiznica

knjiznica = Knjiznica()

knjige = knjiznica.dodaj_vrsto('knjige')
filmi = knjiznica.dodaj_vrsto('filmi')

knjiznica.dodaj_vnos('Krive so zvezde', 'John Green', 'ljubezenski roman', date(2019, 5, 5))
knjiznica.dodaj_vnos('Harry Potter', 'J. K. Rowling', 'znanstvena fantastika', date(2020, 1, 3))

stanje = moja_shramba.v_slovar()
with open('stanje.json', 'w') as datoteka:
    json.dump(stanje, datoteka, ensure_ascii=False, indent=4)
