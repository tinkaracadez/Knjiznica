import json

class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, shramba):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.shramba = shramba


class Knjiznica:
    def __init__(self):
        self.vrste = []
        self.vnosi = []
        self._vrste_po_imenih = {}
        self._vnosi_po_vrstah = {}

    def dodaj_vrsto(self, ime):
        if ime in self._vrste_po_imenih:
            raise ValueError('Vrsta s tem imenom že obstaja!')         
        nova = Vrsta(ime, self)
        self.vrste.append(nova)
        self._vrste_po_imenih[ime] = nova
        self._vnosi_po_vrstah[nova] = []
        return nova

    def dodaj_vnos(self, naslov, avtor, vrsta, datum):
        self._preveri_vrsto(vrsta)
        nov = Vnos(naslov, avtor, vrsta, datum)
        self.vnosi.append(nov)
        self._vnosi_po_vrstah[vrsta].append(nov)
        return nov

    def poisci_vrsto(self, ime):
        return self._vrste_po_imenih[ime]

    def vnosi_vrste(self, vrsta):
        yield from self._vnosi_po_vrstah[vrsta]

    def _preveri_vrsto(self, vrsta):
        if vrsta.knjiznica != self:
            raise ValueError(f'Vrsta {vrsta} ne spada v to knjižnico!')

    def slovar_s_stanjem(self):
        return {
            'vrste': [{
                'ime': vrsta.ime,
            } for vrsta in self.vrste],
            'vnosi': [{
                'naslov': vnos.naslov,
                'avtor': vnos.avtor,
                'vrsta': vnos.vrsta.ime,
                'datum': str(vnos.datum),
            } for vnos in self.vnosi],
        }



#DODAJ @CLASSMETHOD ?! IN NEKO FUNKCIJO nalozi_iz_slovarja
#povezano z uporabnikom?



    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.slovar_s_stanjem(), datoteka, ensure_ascii=False, indent=4)



#DODAJ @CLASSMETHOD ?! IN ŠE ENO FUNKCIJO nalozi_stanje
#povezano z uporabnikom? +CLS



class Vrsta:
    def __init__(self, ime, knjiznica):
        self.ime = ime
        self.knjiznica = knjiznica

    def stanje(self):
        return [vnos.naslov for vnos in self.vnosi()]

    def vnosi(self):
        yield from self.knjiznica.vnosi_vrste(self)


class Vnos:
    def __init__(self, naslov, avtor, vrsta, datum):
        self.naslov = naslov
        self.avtor = avtor
        self.vrsta = vrsta
        self.datum = datum

    #neka funkcija glede datumov?
    #def __lt__(self, other):
    #    return self.datum < other.datum


