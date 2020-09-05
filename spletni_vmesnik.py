from datetime import date
import bottle
import os
import random
from model import Knjiznica

knjiznice = {}
for ime_datoteke in os.listdir('shranjene_knjiznice'):
    st_uporabnika, koncnica = os.path.splitext(ime_datoteke)
    knjiznice[st_uporabnika] = Knjiznica.nalozi_stanje(os.path.join('shranjene_knjiznice', ime_datoteke))

def poisci_vrsto(ime_polja):
    ime_vrste = bottle.request.forms.getunicode(ime_polja)
    knjiznica = knjiznica_uporabnika()
    return knjiznica.poisci_vrsto(ime_vrste)

def knjiznica_uporabnika():
    st_uporabnika = bottle.request.get_cookie('st_uporabnika')
    if st_uporabnika is None:
        st_uporabnika = str(random.randint(0, 2 ** 40))
        knjiznice[st_uporabnika] = Knjiznica()
        bottle.response.set_cookie('st_uporabnika', st_uporabnika, path='/')
    return knjiznice[st_uporabnika]

def shrani_knjiznico_uporabnika():
    st_uporabnika = bottle.request.get_cookie('st_uporabnika')
    knjiznica = knjiznice[st_uporabnika]
    knjiznica.shrani_stanje(os.path.join('shranjene_knjiznice', f'{st_uporabnika}.json'))


@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/knjiznica/')    

@bottle.get('/knjiznica/')
def zapisovanje_knjig():
    print(knjiznice)
    knjiznica = knjiznica_uporabnika()
    return bottle.template('knjiznica.html', knjiznica=knjiznica)

@bottle.get('/pomoc/')
def pomoc():
    return bottle.template('pomoc.html')

@bottle.post('/dodaj-vnos/')
def nov_vnos():
    knjiznica = knjiznica_uporabnika()
    naslov = bottle.request.forms.getunicode('naslov')
    avtor = bottle.request.forms.getunicode('avtor')
    #vrsta = poisci_vrsto('vrsta')
    vrsta = knjiznica.poisci_vrsto(bottle.request.forms['vrsta'])
    datum = date.today().strftime('%Y-%m-%d')
    knjiznica.dodaj_vnos(naslov, avtor, vrsta, datum)
    shrani_knjiznico_uporabnika()
    bottle.redirect('/')

@bottle.post('/dodaj-vrsto/')
def nova_vrsta():
    knjiznica = knjiznica_uporabnika()
    knjiznica.dodaj_vrsto(bottle.request.forms.getunicode('ime'))
    shrani_knjiznico_uporabnika()
    bottle.redirect('/')

bottle.run(debug=True, reloader=True)
