import json

class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, shramba):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.shramba = shramba


class Shramba:
    def __init__(self):
        self.vrste = []

    def dodaj_vrsto(self, ime):
        return Vrsta(ime, self)
        #self.vrste.append(vrsta) (ni treba, ker je v vrstici zgoraj v oklepaju self)

    def dodaj_vnos(self, vrsta, naslov, avtor, zanr, datum, ocena):
        #preverimo, če kdo hoče dodati nekaj, kar ni moje
        if vrsta.shramba != self:
            print('Tole pa ni dobro!')
        return Vnos(vrsta, naslov, avtor, zanr, datum, ocena)

    def __str__(self):
        return f'Vrste: {self.vrste}'


class Vrsta:
    def __init__(self, ime, shramba):
        self.ime = ime
        self.shramba = shramba
        self.shramba.vrste.append(self)
        self.vnosi = []

    def __repr__(self):
        return f'<Vrsta: {self}>'

    def __str__(self):
        return f'{self.ime}: {self.stanje()}'

    def stanje(self):
        return [vnos.naslov for vnos in self.vnosi]


class Vnos:
    def __init__(self, vrsta, naslov, avtor, zanr, datum, ocena):
        self.vrsta = vrsta
        self.vrsta.vnosi.append(self)
        self.naslov = naslov
        self.avtor = avtor
        self.zanr = zanr
        self.datum = datum
        self.ocena = ocena


