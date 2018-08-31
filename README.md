# Runoarkisto -Tietokantasovellus harjoitustyö

 Helsingin yliopiston Tietokantasovellus (4 op) kurssilla (kesä-2018) harjoitustyönä tehty tietokantaa käyttävä web-sovellus. 
 - Toteutus: Herokun PostgreSQL tietokanta , Python, HTML, CSS, [ SQLAlchemy ](https://www.sqlalchemy.org),  Flask sovelluskehys, WTForms kirjasto lomakkeiden luomisessa ja validoinnissa,  Bootstrap-kirjasto ulkoasun tyylittelyssä.
 - Julkaisu: verkossa Heroku-pilvipalvelussa: https://tsoha-python-runoarkisto.herokuapp.com/
 - Pääkäyttäjän ja käyttäjän kirjautuminen:
   - **admin**
       - Username: hello
       - Password: world
   - **User**
       - Username: test
       - Password: test     
 
Runoarkistoon on tarkoitus kerätä kirjautuneilta käyttäjiltä elämän erilaisiin tilanteisiin sopivia
runoja ja aforismeja. Arkistosta voi eri aihepiirien eli kategorioiden avulla hakea haluaamaansa runoa, joka sopisi esimerkiksi syntymäpäiväkorttiin, häihin, ristäisiin, tupaantuliaisiin, joulukorttiin. Sama runo voi kuulua useaan eri kategoriaan ja yhdessä kategoriassa voi olla useita runoja. Kategorioita voi tarvittaessa myös lisätä.

Kukatahansa voi lukea ja hakea runoja arkistosta. Kirjautunut käyttäjä voi lisäksi lisätä runoja arkistoon ja muokata lisäämiään runoja.Lisääminen tapahtuu syöttämällä tiedot lomakkeeseen.

Järjestelmän ylläpitäjä=pääkäytäjä pääsee muokkaamaan kaikkia runoja ja niiden kategorioita. Lisäksi hän pääsee hallinnoimaan, poistamaan ja muokkaamaan käyttäjien tietoja. Järjestelmän ylläpitäjä voi antaa myös tavallisille käyttäjille pääkäyttäjän oikeudet. Järjestelmän ylläpitäjä voi myös tehdä yhteenvetokyselyitä tietokannasta.

Jos aika riittää runoihin on tarkoitus liittää like/tykkäys toiminto, jolloin runoille voi antaa äänensä ja runoista voi hakea suosituimpia eli eniten ääniä saaneita.

## Toimintoja

Runo(CRUD)
- Kaikkien runojen listaus ja yksittäisen tarkastelu
- Runon haku nimen tai kategorian perusteella
- Runon lisäys ja muokkaus
- Runon poisto

Kategoria(CRD)
- Yksittäisen runon kategorioiden tarkastelu
- Kategorian lisäys runolle ja poisto 
- Kategorioiden listaus ja poisto(admin)

Käyttäjä(CRUD)
- Käyttäjän lisäys rekisteröityminen/käyttäjätunnusten luominen
- Kirjautuminen
- Käyttäjien listaus(vain admin)
- Käyttäjätietojen muokaus ja käyttäjän poisto(vain admin)

Tykkäys
- Runojen tykkäystoiminto(kirjautunut)
- Tykätyimpien runojen haku top 10 
- Tykkäysten resetointi(admin)

- Yhteenvetokyselyt tietokannasta: 
    - Kirjautuneen käyttäjän runojen haku 
    - Käyttäjät jotka ovat lisänneet runoja (admin)
    - Valitun runon kaikkien kategorioiden haku(admin)
    - Ketkä lisänneet eniten runoja top 10 (admin)
    - Runon haku otsikon mukaan
    - Runojen haku kategorian mukaan
    - Kuinka monta runoa ja mitkä runot tietty käyttäjä on lisännyt?
    - Paljonko runoja yhteensä
    - Paljonko käyttäjiä yhteensä
  
    Jatko ehdotuksia (todo)
    - Kuinka monta runoa on kussakin kategoriassa?
    * (Kunkin kategorian suosituin runo?)
    - Käyttäjän haku syötetyn nimen mukaan? (admin)
    - etsi toimintoon ignooraus isoista ja pienistä kirjaimista ja regular expression..löytämisen helpottamiseksi..
    - salasanan Bcryptaus

## Dokumentaatio
- [Tietokantakaavio](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/Runo_db_kaavio%20(2).png)
- [User storyt ja SQL lauseet](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/userstory.md)
- [Asennusohje](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/asennusohje.md)
- [Käyttöohje](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/käyttöohje.md)
- [Omat kokemukset](https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/käyttöohje.md)


## Puutteet & jatkokehitysideat
Mitä puutteita tai bugeja ohjelmassa on? Mitä lisäominaisuuksia ohjelmaan voisi lisätä?

