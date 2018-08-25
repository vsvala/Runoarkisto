## Käyttötapaukset

Kaikki käyttäjät:

- Kukatahansa käyttäjä voi  listata ja lukea lisättyjä runoja.
- Kukatahansa käyttäjä voi hakea runoja niiden nimen perusteella, jotta runo löytyisi nopeammin.
- Kukatahana käyttäjä voi hakea runoja eri kategorioiden eli aihepiirien mukaan, jotta hän löytää tiettyyn tilanteeseen sopivan runon.
- Kukatahana käyttäjä voi listata suosituimmat runot.
- Kukatahansa käyttäjä voi rekisteröityä sivustolle, jotta hän voi kirjautua  ja  saisi lisää toiminnallisuuksia käyttöönsä

Kirjautunut käyttäjä:

- Kirjautunut käyttäjä voi ehdottaa runoja lisättäväksi arkistoon, jotta arkistossa olisi enemmän valinnan varaa
- Kirjautunut käyttäjä voi muokata ehdottamaansa runoa, typojen varalta.
- Kirjautunut käyttäjä voi ehdottaa runolle uusia kategorioita , jos runo ei sovi valmiisiin.
- Kirjautunut käyttäjä voi äänestää runoa, jotta saadaan tietoon suosituimmat runot


Ylläpitäjä:

- Ylläpitäjä voi hyväksyä kirjautuneen käyttäjän ehdottaman runon tai kategorian lisättäväksi
- Ylläpitäjä voi itse lisätä runoja ja uusia kategorioita tietokantaan haettaviksi.
- Ylläpitäjä voi lisätä muokata ja poistaa runoja ja kategorioita, jotta mahdollisia virheitä voitaisiin korjata ja ei haluttuja runoja poistaa
- Ylläpitäjä voi lisätä, muokata ja poistaa tykkäys toimintoja virhetilanteiden varalta
-Ylläpitäjä voi hallinnoia, lisätä ja poistaa rekisteröityneen käyttäjän esim. väärinkäytösten varalta.

### Tietokannan luonti lauseet

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
CREATE TABLE categories (
	runo_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (runo_id, category_id), 
	FOREIGN KEY(runo_id) REFERENCES runo (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);
```
