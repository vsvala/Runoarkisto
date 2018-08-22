# Runoarkisto -Tietokantasovellus harjoitustyö

 Helsingin yliopiston Tietokantasovellus (4 op) kurssilla (kesä-2018) harjoitustyönä tehty tietokantaa käyttävä web-sovellus. 
 - Toteutus: Herokun PostgreSQL tietokanta , Python, SQLAlchemy,  Flask sovelluskehys, WTForms kirjasto lomakkeiden luomisessa ja validoionnissa,  Bootstrap-kirjasto ulkoasun tyylittelyssä.
 - Julkaisu: verkossa Heroku-pilvipalvelussa: https://tsoha-python-runoarkisto.herokuapp.com/
 - Pääkäyttäjän ja käyttäjän kirjautuminen:
  -**admin**
      - Username: hello
      - Password: world
 -**User**
      - Username: test
      - Password: test     
 
Runoarkistoon on tarkoitus kerätä kirjautuneilta käyttäjiltä elämän erilaisiin tilanteisiin sopivia
runoja ja aforismeja. Arkistosta voi eri aihepiirien eli kategorioiden avulla hakea haluaamaansa runoa, joka sopisi esimerkiksi syntymäpäiväkorttiin, häihin, ristäisiin, tupaantuliaisiin, joulukorttiin. Sama runo voi kuulua useaan eri kategoriaan ja yhdessä kategoriassa voi olla useita runoja. Kategorioita voi tarvittaessa myös lisätä.

Tavallinen kirjautunut käyttäjä voi hakea runoja kannasta ja ehdottaa uusien lisäämistä kantaan.

Järjestelmän ylläpitäjä voi listä järjestelmään runoja itse ja hyväksyä ehdotettuja. Lisääminen voi tapahtua esimerkiksi syöttämällä tiedot lomakkeeseen tai lukemalla runo esimerkiksi tekstitiedostosta. Järjestelmän ylläpitäjä voi antaa myös tavallisille käyttäjille ylläpito-oikeudet, jolloin tämä voi lisätä runoja itse. Järjestelmän ylläpitäjä voi myös tehdä yhteenvetokyselyitä tietokannasta.

Jos aika riittää runoihin on tarkoitus liittää like/tykkäys toiminto, jolloin runoille voi antaa äänensä ja runoista voi hakea suosituimpia eli eniten ääniä saaneita.

## Toimintoja

- Runon haku nimen tai kategorioiden perusteella
- Runojen luku/selailu
- Runon lisäys ja muokkaus lomakkeella
- Runon sisäänluku tiedostosta
- Runon poisto(vain Admin)
- Uuden runon  ehdottaminen / ehdotuksen hyväksyminen
- Uuden kategorian lisäys ja poisto (Admin)
- Uuden kategorian ehdottaminen / ehdotuksen hyväksyminen
- Käyttäjätunnuksen luominen/rekisteröityminen
- Kirjautuminen
- Käyttäjätietojen muutos ja tilin poisto(vain Admin)
- Rekisteröityjen käyttäjien listaaminen ja haku

- Yhteenvetokyselyt tietokannasta:
    -Käyttäjät jotka ovat lisänneet runoja
    -Kirjautuneen käyttäjän runojen haku
    -Valitun runon kaikkien kategorioiden haku
    -Runon haku otsikon mukaan
    -Runonojen haku kategorian mukaan
    
    todo
    -Runojen haku valitun käyttäjän mukaan 
    - Kuinka monta runoa ja mitkä runot tietty käyttäjä on lisännyt?
    - Kuinka monta runoa on kussakin kategoriassa?
    * (Kunkin kategorian suosituin runo?)
    - ?


(mahdollisesti myös)
* Runojen tykkäys/äänestys toiminto
* Suosituimpien runojen haku top10 ja järjestäminen


## Dokumentaatio
- [Alustava tietokantakaavio](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/Runo_db_kaavio.png)
- [User storyt](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/userstory.md)
- [Asennusohje](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/asennusohje.md)
- [Käyttöohje](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/käyttöohje.md)
