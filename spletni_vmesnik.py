from datetime import date
import bottle
from model import Knjiznica

DATOTEKA_S_STANJEM = 'stanje.json'
#try:
knjiznica = Knjiznica.nalozi_stanje(DATOTEKA_S_STANJEM)
#except:
#    knjiznica = Knjiznica()

@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/knjiznica/')    

@bottle.get('/knjiznica/')
def zapisovanje_knjig():
    return bottle.template('knjiznica.html', knjiznica=knjiznica)

@bottle.get('/pomoc/')
def pomoc():
    return bottle.template('pomoc.html')

@bottle.post('/dodaj-vrsto/')
def nova_vrsta():
    knjiznica.dodaj_vrsto(bottle.request.forms.getunicode('ime'))
    knjiznica.shrani_stanje(DATOTEKA_S_STANJEM)
    bottle.redirect('/')

@bottle.post('/dodaj-vnos/')
def nov_vnos():
    naslov = bottle.request.forms.getunicode('naslov')
    avtor = bottle.request.forms.getunicode('avtor')
    vrsta = knjiznica.poisci_vrsto(bottle.request.forms['vrsta'])
    datum = date.today().strftime('%Y-%m-%d')
    knjiznica.dodaj_vnos(naslov, avtor, vrsta, datum)
    knjiznica.shrani_stanje(DATOTEKA_S_STANJEM)
    bottle.redirect('/')

bottle.run(debug=True, reloader=True) #naročimo bottlu naj zažene strežnik
