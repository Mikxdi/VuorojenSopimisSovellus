# Käyttäjätarinat
| Kuka | Mitä | Miksi  |Tila|
|----|-----| -----|-----|
| Käyttäjä | Uuden paikan lisääminen | Käyttäjä voi tuoda uusia mahdollisuuksia |Valmis|
| Käyttäjä | Rekisteröityminen ja kirjautuminen    | Mahdollistaa sovelluksen käyttämisen| Valmis|
| Käyttäjä | Uuden ehdotuksen lisääminen|Käyttäjälle mahdollisuus lisätä haluamansa vuoro| Valmis|
|Käyttäjä|Ehdotuksen muokkaaminen|Mahdollisesti virheellistä tietoa sisältävän ehdotuksen muokkaaminen|Valmis|
|Käyttäjä|Paikan muokkaaminen ja poistaminen|Mahdollisen väärän paikan poistaminen tai muokkaaminen|Valmis|
| Moderaattori |Käyttäjän poistaminen|Mahdollisen haittakäyttäjän tilin poistaminne|Kesken|



# SQL-kyselyt

## Ehdotusten listaaminen

SELECT Suggestion.name, Suggestion.whenis, Location.name, Location.price, Suggestion.success, Suggestion.id, Account.id, COUNT(Vote.id) AS Votes FROM Suggestion
        JOIN Location ON Location.id = Suggestion.location_id 
        JOIN Account ON Account.id = Suggestion.account_id
        LEFT JOIN Vote ON Vote.suggestion_id = Suggestion.id
        GROUP BY Suggestion.name, Location.name, Suggestion.success, Suggestion.whenis, Location.price, Suggestion.id, Account.id;

## Käyttäjän lisääminen

INSERT INTO Account (id, name, username, password, role)
	VALUES(?, ?, ?, ?);

## Käyttäjän sisäänkirjautuminen

SELECT account.id AS account_id, , 
    account.name AS account_name, 
    account.username AS account_username, 
    account.password AS account_password, 
    account.role AS account_urole 
    FROM account
    WHERE account.username = ? AND account.password = ?;

##Paikan luominen

INSERT INTO location (id, name, price, account_id)
	VALUES (?, ?, ?, ?);

##Paikan poistaminen
Poistetaan ensin äänet, jotka liittyvät ehdotuksiin joissa on poistettava paikka
DELETE FROM Vote WHERE vote.suggestion_id = ?;
Poistetaan ensin ehdotukset, joissa on kyseinen paikka
DELETE FROM Suggestion WHERE suggestion.location_id = ?;
Poistetaan paikka
DELETE FROM Location WHERE location.id = ?;

## Ehdotuksen luominen

INSERT INTO suggestion (id, name, whenis, location_id, success, account_id)
	VALUES(?, ?, ?, ?, ?);

## Ehdotuksen poisto

Poistetaan ensin ehdotukseen liittyvät äänet
DELETE FROM Vote WHERE vote.suggestion_id = ?;
poistetaan ehdotus
DELETE FROM Suggestion WHERE suggestion.id = ?;


## Ehdotuksen muokkaus

UPDATE Suggestion
SET name = ?, whenis = ?, location_id = ?
WHERE suggestion.id = ?;

## Paikan muokkaus

UPDATE Location
SET name = ?, price = ?
WHERE location.id = ?;
