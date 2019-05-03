# VuorojenSopimisSovellus
Sovellus salibandy vuorojen sopimiseen kaveriporukan kesken.

Ohjelman pääasiallisena käyttötarkoituksena on helpottaa salibandy vuorojen ennakkoon sopimista alustalla, jossa käyttäjät voivat ehdottaa vuoroa, paikkaa vuorolle sekä vuoron aikaa.
Näiden perusteella ehdotuksille voi antaa ääniä, jotta nähdään parhaiten sopivat vuorot

Ohjelma tulee sisältämään kolme taulua. Nämä ovat käyttäjän tiedot sisältävä taulu, taulu ehdotuksista
ja taulu paikoista, joissa vuoro pidetään

Käyttäjät voivat lisätä ehdotuksia sopiviksi päiviksi. Mikäli kyseinen ehdotus saa päätetyn määrän 
ääniä, muuttuu vuoron tila alustavasta varattavaan.

[Heroku](https://vuoronvaraussovellus.herokuapp.com/)

Ohjeet ohjelman käyttöön paikallisesti sekä sen lisäämiseen herokuun.
Ohjelman käyttäminen vaatii Python3 löytymistä asennettuna. Ohjeet ovat Linux käyttöjärjestelmille.

Seuraavat kohdat toteutaan terminaalissa
1. 	Kloonaa github repositorio komennolla haluamaasi kansioon
	‘git clone https://github.com/Mikxdi/VuorojenSopimisSovellus’
      
2.      Siirry terminaalissa ohjelmakansioon komennolla
	‘cd VuorojenSopimisSovellus’

3.      Luo sovellusta varten virtuaaliympäristö komennolla
  	‘python3 -m venv venv’
 
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

