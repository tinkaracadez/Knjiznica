import json

class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, shramba):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.shramba = shramba


class Shramba:
    def __init__(self):
        self.vrste = []
        self.vnosi = []

    def dodaj_vrsto(self, ime):
        for vrsta in self.vrste:
            if vrsta.ime == ime:
                raise ValueError('Vrsta že obstaja!')  #sprožimo izjemo         
        nova = Vrsta(ime, self)
        self.vrste.append(nova)
        return nova
        #self.vrste.append(vrsta) (ni treba, ker je v vrstici zgoraj v oklepaju self)

    def dodaj_vnos(self, vrsta, naslov, avtor, zanr, datum, ocena):
        #preverimo, če kdo hoče dodati nekaj, kar ni moje
        if vrsta.shramba != self:
            raise ValueError(f'Vrsta {vrsta} ne spada v to shrambo!')
        else:
            nov = Vnos(vrsta, naslov, avtor, zanr, datum, ocena)
            self.vnosi.append(nov)
            return nov

    def __str__(self):
        return f'Vrste: {self.vrste}'

    def v_slovar(self):
        return {
            'vrste': [vrsta.v_slovar() for vrsta in self.vrste],
            'vnosi': [vnos.v_slovar() for vnos in self.vnosi],
        }


class Vrsta:
    def __init__(self, ime, shramba):
        self.ime = ime
        self.shramba = shramba
        #self.vnosi = []

    def __repr__(self):
        return f'<Vrsta: {self}>'

    def __str__(self):
        return f'{self.ime}: {self.stanje()}'

    def stanje(self):
        return [vnos.naslov for vnos in self.vnosi]

    def v_slovar(self):
        return {
            'ime': self.ime,
            #'shramba': self.shramba,
        }


class Vnos:
    def __init__(self, vrsta, naslov, avtor, zanr, datum, ocena):
        self.vrsta = vrsta
        self.naslov = naslov
        self.avtor = avtor
        self.zanr = zanr
        self.datum = datum
        self.ocena = ocena

    #vsak vnos bomo dali v nek slovar, da ga bomo nato s pomočjo jsona vpisali v datoteko
    def v_slovar(self):
        return {
            'vrsta': self.vrsta.ime,
            'naslov': self.naslov,
            'avtor': self.avtor,
            'zanr': self.zanr,
            'datum': str(self.datum),
            'ocena': self.ocena,
        }


