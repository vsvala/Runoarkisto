## Käyttötapaukset

Kaikki käyttäjät:

- Kukatahansa käyttäjä voi  listata ja lukea lisättyjä runoja. ok
- Kukatahansa käyttäjä voi hakea runoja niiden nimen perusteella, jotta runo löytyisi nopeammin. ok
- Kukatahana käyttäjä voi hakea runoja eri kategorioiden eli aihepiirien mukaan, jotta hän löytää tiettyyn tilanteeseen sopivan runon. ok
- Kukatahansa käyttäjä voi lukea suosituimmat runot (top 10). ok
- Kukatahansa käyttäjä voi rekisteröityä sivustolle, jotta hän voi kirjautua  ja  saisi lisää toiminnallisuuksia käyttöönsä. ok

Kirjautunut käyttäjä:

- Kirjautunut käyttäjä voi lisätä runoja arkistoon, jotta arkistossa olisi enemmän valinnan varaa. ok
- Kirjautunut käyttäjä voi listata lisäänsä runot. ok
- Kirjautunut käyttäjä voi poistaa tai muokata lisäämäänsä runoa, typojen varalta. ok
- Kirjautunut käyttäjä voi lisätä ja poistaa lisäämänsä runojen kategorioitaja keksiä uusia,jos runo ei sovi valmiisiin. ok
- Kirjautunut käyttäjä voi tykätä runoista, jotta saadaan tietoon suosituimmat runot. ok


Ylläpitäjä:

- Ylläpitäjä voi itse lisätä runoja ja uusia kategorioita tietokantaan haettaviksi. ok
- Ylläpitäjä voi listata, lisätä muokata ja poistaa runoja, jotta mahdollisia virheitä voitaisiin korjata ja ei haluttuja runoja poistaa. ok
- Ylläpitäjä voi listata kategoriat, sekä lisätä ja poistaa niitä. ok
- Ylläpitäjä voi listata, lisätä, muokata ja poistaa käyttäjien tietoja. ok
- Ylläpitäjä voi hallinnoida: listata, muokata, lisätä ja poistaa rekisteröityneen käyttäjän esim. väärinkäytösten varalta tai esim. antaakseen käyttäjälle ADMIN oikeudet. ok
- Ylläpitäjä voi nähdä tilastoja (yhteenvetokyselyt) sivustolta. kaikki ok
	- Listaa kaikki käyttäjät jotka on lisänneet runoja ja mitä runoja on lisätty
	- Arkiston runojen määrä 
	- Arkiston rekisteröityneiden käyttäjien lukumäärä
	- Eniten runoja lisänneet käyttäjät (Top 10) 
- Ylläpitäjä voi lisätä, muokata ja poistaa tykkäyksiä. Kesken näistä vain lisäys tehtynä, mutta toimii vain lokaalisti, ei herokussa...

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
	runo_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(runo_id) REFERENCES runo (id)
);
CREATE TABLE categories (
	runo_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (runo_id, category_id), 
	FOREIGN KEY(runo_id) REFERENCES runo (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);

```
