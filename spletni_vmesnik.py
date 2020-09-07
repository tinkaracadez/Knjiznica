from datetime import date
import bottle
import os
import random
import hashlib
from model import Uporabnik, Knjiznica

uporabniki = {}
skrivnost = 'HUDA SKRIVNOST'

for ime_datoteke in os.listdir('uporabniki'):
    uporabnik = Uporabnik.nalozi_stanje(os.path.join('uporabniki', ime_datoteke))
    uporabniki[uporabnik.uporabnisko_ime] = uporabnik

def poisci_vrsto(ime_polja):
    ime_vrste = bottle.request.forms.getunicode(ime_polja)
    knjiznica = knjiznica_uporabnika()
    return knjiznica.poisci_vrsto(ime_vrste)

def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret=skrivnost)
    if uporabnisko_ime is None:
        bottle.redirect('/prijava/')
    return uporabniki[uporabnisko_ime]

def knjiznica_uporabnika():
    return trenutni_uporabnik().knjiznica

def shrani_trenutnega_uporabnika():
    uporabnik = trenutni_uporabnik()
    uporabnik.shrani_stanje(os.path.join('uporabniki', f'{uporabnik.uporabnisko_ime}.json'))

@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/knjiznica/')    

@bottle.get('/knjiznica/')
def zapisovanje_knjig():
    knjiznica = knjiznica_uporabnika()
    return bottle.template('knjiznica.html', knjiznica=knjiznica)

@bottle.get('/pomoc/')
def pomoc():
    return bottle.template('pomoc.html')

@bottle.get('/prijava/')
def prijava_get():
    return bottle.template('prijava.html')
    bottle.redirect('/')

@bottle.post('/prijava/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    h = hashlib.blake2b()
    h.update(geslo.encode(encoding='utf-8'))
    zasifrirano_geslo = h.hexdigest()
    if 'nov_racun' in bottle.request.forms and uporabnisko_ime not in uporabniki:
        uporabnik = Uporabnik(
            uporabnisko_ime,
            zasifrirano_geslo,
            Knjiznica()
        )
        uporabniki[uporabnisko_ime] = uporabnik
    else:
        uporabnik = uporabniki[uporabnisko_ime]
        uporabnik.preveri_geslo(zasifrirano_geslo)
    bottle.response.set_cookie('uporabnisko_ime', uporabnik.uporabnisko_ime, path='/', secret=skrivnost)
    bottle.redirect('/')

@bottle.post('/odjava/')
def odjava():
    bottle.response.delete_cookie('uporabnisko_ime', path='/')
    bottle.redirect('/')

@bottle.post('/dodaj-vnos/')
def nov_vnos():
    knjiznica = knjiznica_uporabnika()
    naslov = bottle.request.forms.getunicode('naslov')
    avtor = bottle.request.forms.getunicode('avtor')
    vrsta = poisci_vrsto('vrsta')
    datum = date.today().strftime('%Y-%m-%d')
    knjiznica.dodaj_vnos(naslov, avtor, vrsta, datum)
    shrani_trenutnega_uporabnika()
    bottle.redirect('/')

@bottle.post('/dodaj-vrsto/')
def nova_vrsta():
    knjiznica = knjiznica_uporabnika()
    knjiznica.dodaj_vrsto(bottle.request.forms.getunicode('ime'))
    shrani_trenutnega_uporabnika()
    bottle.redirect('/')

bottle.run(debug=True, reloader=True)
