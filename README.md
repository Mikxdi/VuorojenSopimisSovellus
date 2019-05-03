# VuorojenSopimisSovellus
Sovellus salibandy vuorojen sopimiseen kaveriporukan kesken.

Ohjelman pääasiallisena käyttötarkoituksena on helpottaa salibandy vuorojen ennakkoon sopimista alustalla, jossa käyttäjät voivat ehdottaa vuoroa, paikkaa vuorolle sekä vuoron aikaa.
Näiden perusteella ehdotuksille voi antaa ääniä, jotta nähdään parhaiten sopivat vuorot

Ohjelma tulee sisältää neljä taulua. Nämä ovat käyttäjän tiedot sisältävä taulu, taulu kunkin ehdotuksen saamista äänistä, taulu ehdotuksista
ja taulu paikoista, joissa vuoro pidetään

Käyttäjät voivat lisätä ehdotuksia sopiviksi päiviksi. Mikäli kyseinen ehdotus saa päätetyn määrän 
ääniä, muuttuu vuoron tila alustavasta varattavaan. Tätä kuvaa ehdotuksien listauksessa kohta Toteutuu, joka saa kymmenen äänen mennessä rikki arvokseen True

## Linkki herokuun
[Heroku](https://vuoronvaraussovellus.herokuapp.com/)

## Sovelluksen asennus
Ohjeet ohjelman käyttöön paikallisesti sekä sen lisäämiseen herokuun.
Ohjelman käyttäminen vaatii Python3 löytymistä asennettuna. Ohjeet ovat Linux käyttöjärjestelmille.

Seuraavat kohdat toteutaan terminaalissa

1.      Kloonaa github repositorio komennolla haluamaasi kansioon ‘git clone https://github.com/Mikxdi/VuorojenSopimisSovellus’
      
2.      Siirry terminaalissa ohjelmakansioon komennolla ‘cd VuorojenSopimisSovellus’

3.      Luo sovellusta varten virtuaaliympäristö komennolla ‘python3 -m venv venv’
 
4.      Aktivoi ympäristö komennolla
        ‘source venv/bin/activate’

5.      Asenna ohjelman riippuvuudet suorittamalla komento
    	‘pip install -r requirements.txt’

6.    	Ohjelman saa käyttöön seuraavilla komennoilla sovelluksen juurikansiossa
    	‘source venv/bin/activate’
    	‘python3 run.py’
    
    	Tämän jälkeen sovellus pyörii selaimessa osoitteessa
    	[http://localhost:5000/](http://localhost:5000/)

Herokuun lisääminen

1.    	Suorita ohjelman asennus ensin paikallisesti yllä olevien ohjeiden mukaan
 
2.    	Luo heroku paikka sovellukselle komennolla
    	‘heroku create Sovelluksen-Haluttu-Nimi’

3.    	Lisää heroku git-hallintaan
    	‘git remote add heroku
	https://git.heroku.com/Sovelluksen-Haluttu-Nimi.git’

4.    	Lisää sovellus herokuun komennolla 
    	‘git add .’
    	‘git commit -m “Viesti”’
    	‘git push heroku master’

5.     	Aseta herokulle PostgreSQL
    	‘heroku config:set HEROKU=1’
    	‘heroku addons:add heroku-postgresql:hobby-dev’

## Ominaisuudet ja lyhyt kuvaus niiden käytöstä

*Ohjelmaan on mahdollista ja suotavaa rekisteröityä. Tämä mahdollistaa muiden toimintojen käyttämisen. Sovellukseen rekisteröityminen tapahtuu sivun ylälaidassa olevasta "Rekisteröidy" nappulasta, Tämän 
jälkeen pääset syöttämään haluamasi käyttäjänimen sekä salasanan. Sovelluksen kaikkien käyttäjien rooli on oletuksena tavallinen käyttäjä.

*Rekisteröitymisen jälkeen sovellukseen voi kirjautua painamalla nappulaa kirjaudu ja syöttämällä oikeat tiedot salasana ja käyttäjätunnus kenttiin. Tämä kirjaa sinut sisään ja mahdollistaa muiden toimintojen käytön

*Paikan lisääminen: Kirjautuneena käyttäjä voi painaa "Lisää uusi paikka" nappia, jolla käyttäjä pääsee paikan luomis näkymään. Syötettyään pyydetyt tiedot käyttäjä siirtyy automaattisesti paikkojen listaus näkymään, jossa käyttäjä voi poistaa tai muokata luomiansa paikkoja, sekä näkee muiden käyttäjien luomat paikat.

*Ehdotuksen lisääminen: Käyttäjä voi lisätä uuden ehdotuksen painamalla "Lisää uusi ehdotus" nappia. Syöttämällä tiedot käyttäjä pääsee Ehdotus listaukseen. Ehdotus listauksessa käyttäjä voi antaa ääniä ehdotuksille tai muokata ja poistaa omia ehdotuksiaan.
 
