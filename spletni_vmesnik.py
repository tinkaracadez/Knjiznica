import bottle
from model import Knjiznica

DATOTEKA_S_STANJEM = 'stanje.json'
#try:
    #knjiznica = Knjiznica.nalozi_stanje(DATOTEKA_S_STANJEM)
#except:
knjiznica = Knjiznica()

@bottle.get('/') #če gre kdo na stran / dobi logo
def zacetna_stran():
    return bottle.template('zacetna_stran.html', knjiznica=knjiznica)
    
@bottle.get('/zivjo/<ime>/')
def pozdravi(ime):
    return bottle.template('pozdrav.html', ime_osebe=ime)

bottle.run(debug=True, reloader=True) #naročimo bottlu naj zažene strežnik
