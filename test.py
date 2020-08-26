from datetime import date
from model import Shramba

moja_shramba = Shramba()

knjige = moja_shramba.dodaj_vrsto('knjige')
filmi = moja_shramba.dodaj_vrsto('filmi')

moja_shramba.dodaj_vnos(knjige, 'Krive so zvezde', 'John Green', 'ljubezenski roman', date(2019, 5, 5), '4')
moja_shramba.dodaj_vnos(knjige, 'Harry Potter', 'J. K. Rowling', 'znanstvena fantastika', date(2020, 1, 3), '5')
moja_shramba.dodaj_vnos(filmi, 'To all the boys', 'nek režiser', 'romatična komedija', date(2019, 6, 5), '4')

print(moja_shramba)