from datetime import date
from model import Shramba, Vnos, Vrsta

moja_shramba = Shramba()

knjige = moja_shramba.dodaj_vrsto('knjige')
filmi = moja_shramba.dodaj_vrsto('filmi')

Vnos(knjige, 'Krive so zvezde', 'John Green', 'ljubezenski roman', date(2019, 5, 5), '5')
Vnos(knjige, 'Harry Potter', 'J. K. Rowling', 'znanstvena fantastika', date(2020, 1, 3), '5')
Vnos(filmi, 'To all the boys', 'nek režiser', 'romatična komedija', date(2019, 6, 5), '4')

print(knjige)
print(filmi)
print(moja_shramba)