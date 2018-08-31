# Käyttötapaukset

## Kaikki käyttäjät:  
tiedon selaaminen

- Kukatahansa käyttäjä voi  listata  runot akkosjärjestykseen ja lukea lisättyjä runoja (sivutus 10). ok
- Kukatahansa käyttäjä voi hakea yksittäistä runoa sen nimen perusteella, jotta runo löytyisi nopeammin. ok
- Kukatahana käyttäjä voi hakea runoja eri kategorioiden eli aihepiirien mukaan, jotta hän löytää tiettyyn tilanteeseen sopivan runon. ok
- Kukatahansa käyttäjä voi lukea suosituimmat runot (top 10). ok (lokaalisti toimii, herokussa ei)
- Kukatahansa käyttäjä voi rekisteröityä sivustolle, jotta hän voi kirjautua saadakseen lisää toiminnallisuuksia käyttöönsä. ok

```sql
kaikki käyttäjät aakkostettuina ja sivutettuna
SELECT * FROM runo ORDER BY runo.name LIMIT 10 OFFSET ?; (OFFSET= 10 * page, annetaan parametrina)

Runon hakeminen nimellä
SELECT * FROM runo WHERE (runo.name = ? <parametrina käyttäjän syöte>); 

Runon hakeminen kategorian mukaan 
SELECT DISTINCT runo.id, runo.name, runo.sisalto, runo.runoilija FROM category, categories, runo WHERE runo.id=categories.runo_id AND categories.category_id=category.id AND category.aihe=:categ.params(categ='käyttäjän syöte')
(parametrina käyttäjän syöttämä kategorian aihe)

Haetaan 10 tykätyintä runoa
SELECT runo.id, runo.name COUNT(likes) AS total FROM liked, runo, runo_liked WHERE runo.id=liked.runo_id AND liked.id=runo_liked.liked_id"  GROUP BY likes, runo.name, runo.id" ORDER BY total DESC LIMIT 10;

käyttäjän User lisäys:
INSERT INTO account (name, username, password, role) VALUES ('nimi', 'tunnus', 'salasana', 'user');

```

Kirjautunut käyttäjä:

- Kirjautunut käyttäjä voi lisätä runoja arkistoon, jotta arkistossa olisi enemmän valinnan varaa. ok
- Kirjautunut käyttäjä voi listata kaikki lisäänsä runot ja tarkastella yksittäistä. ok
- Kirjautunut käyttäjä voi poistaa tai muokata lisäämäänsä runoa, typojen varalta. ok
- Kirjautunut käyttäjä voi lisätä ja poistaa lisäämänsä runojen kategorioitaja keksiä uusia,jos runo ei sovi valmiisiin. ok
- Kirjautunut käyttäjä voi tykätä runoista(kerran per runo), jotta saadaan tietoon suosituimmat runot. ok


```sql

Haetaan kirjautuneen käyttäjän runo
SELECT DISTINCT runo.id, runo.name FROM runo, account WHERE (runo.account_id =?<parametrinä kirjautunut käyttäjä>);

Haetaan tietyn runon kaikki tiedot
SELECT * FROM runo WHERE runo.id = ? <parametrinä klikatun runon runo.i>);

Onko käyttäjä jo tykännyt runosta
SELECT SUM(likes) AS total FROM liked, runo_liked WHERE liked.runo_id=? <parametrina valittu runon id> AND liked.account_id=? <parametrina annettu käyttäjän id)   

Runon poisto
DELETE FROM runo WHERE runo.id = ? <parametrinä annettu runo.id >);

Runon muokkaus:
UPDATE Runo SET name = '?', sisalto = '?'  runoilija = '?' WHERE runo.id = ?; (? = <parametrinä annettu erikseen otsikko, sisalto, runoilja ja runo.id >)
```
Ylläpitäjä:

- Ylläpitäjä voi itse lisätä runoja ja uusia kategorioita tietokantaan haettaviksi. ok
- Ylläpitäjä voi lisätä, listata, lisätä muokata ja poistaa runoja, jotta mahdollisia virheitä voitaisiin korjata ja ei haluttuja runoja poistaa. ok
- Ylläpitäjä voi listata kategoriat, sekä lisätä ja poistaa niitä. ok
- Ylläpitäjä voi listata, lisätä, muokata ja poistaa kaikkia käyttäjän tietoja. ok
- Ylläpitäjä voi hallinnoida: listata, muokata, lisätä ja poistaa rekisteröityneen käyttäjän esim. väärinkäytösten varalta tai esim. antaakseen käyttäjälle ADMIN oikeudet. ok
- Ylläpitäjä voi nähdä tilastoja (yhteenvetokyselyt) sivustolta. kaikki ok
	- Listaa kaikki käyttäjät jotka on lisänneet runoja ja mitä runoja on lisätty
	- Arkiston runojen määrä 
	- Arkiston rekisteröityneiden käyttäjien lukumäärä
	- Eniten runoja lisänneet käyttäjät (Top 10) 
- Ylläpitäjä lisätä voi poistaa tykkäyksiä. (lokaalisti toimii, herokussa ei)



```sql

hakee kaikki käyttäjät joilla on lisättyjä runoja

"SELECT account.id, account.username FROM account"
                    " LEFT JOIN runo ON runo.account_id = account.id"
                    " GROUP BY account.id"
                    " HAVING COUNT(runo.id) > 0")

Hakee top10 eniten runoja lisänneet käyttäjät

 "SELECT account.id, account.username, COUNT(runo.id) as runocount FROM account"
                    " LEFT JOIN runo ON runo.account_id = account.id"
                    " WHERE (runo.id>0)"
                    " GROUP BY account.id"
                    " ORDER BY runocount DESC"
                    " LIMIT 10")

Laskee arkiston käyttäjien määrän

"SELECT account.id, COUNT(*) AS howmany FROM account"
                    " LEFT JOIN runo ON runo.account_id = account.id"
                    " GROUP BY account.id")             

```

### Tietokannan luonti lauseet (CREATE TABLE)

```sql
CREATE TABLE category (
	id INTEGER NOT NULL, 
	aihe VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(100) NOT NULL, 
	username VARCHAR(20) NOT NULL, 
	password VARCHAR(20) NOT NULL, 
	role VARCHAR(10) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
CREATE TABLE runo (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	sisalto VARCHAR(2000) NOT NULL, 
	runoilija VARCHAR(100) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE liked (
	id INTEGER NOT NULL, 
	likes INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE categories (
	runo_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (runo_id, category_id), 
	FOREIGN KEY(runo_id) REFERENCES runo (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);

CREATE TABLE runo_liked (
	runo_id INTEGER NOT NULL, 
	liked_id INTEGER NOT NULL, 
	PRIMARY KEY (runo_id, liked_id), 
	FOREIGN KEY(runo_id) REFERENCES runo (id), 
	FOREIGN KEY(liked_id) REFERENCES liked (id)
);

```
