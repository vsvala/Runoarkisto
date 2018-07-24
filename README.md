# Runoarkisto -Tietokantasovellus harjoitustyö

 Helsingin yliopiston Tietokantasovellus (4 op) kurssilla (kesä-2018) harjoitustyönä tehty tietokantaa käyttävä web-sovellus. 
 Toteutus: PostgreSQL tietokanta , Python, Flask. 
 Julkaisu: verkossa Heroku-pilvipalvelussa
 
Runoarkistoon on tarkoitus kerätä kirjautuneilta käyttäjiltä elämän erilaisiin tilanteisiin sopivia
runoja ja aforismeja. Arkistosta voi eri aihepiirien eli kategorioiden avulla hakea haluaamaansa runoa, joka sopisi esimerkiksi syntymäpäiväkorttiin, häihin, ristäisiin, tupaantuliaisiin, joulukorttiin jne.. Sama runo voi kuulua useaan eri kategoriaan ja yhdessä kategoriassa voi olla useita runoja.

Tavallinen kirjautunut käyttäjä voi hakea runoja kannasta ja ehdottaa uusien lisäämistä kantaan.

Järjestelmän ylläpitäjä voi listä järjestelmään runoja itse ja hyväksyä ehdotettuja. Lisääminen voi tapahtua esimerkiksi syöttämällä tiedot lomakkeeseen tai lukemalla runo esimerkiksi tekstitiedostosta. Järjestelmän ylläpitäjä voi antaa myös tavallisille käyttäjille ylläpito-oikeudet, jolloin tämä voi lisätä runoja itse.

Jos aika riittää runoihin on tarkoitus liittää like/tykkäys toiminto, jolloin ruonille voi antaa äänensä ja runoista voi hakea suosituimpia eli eniten ääniä saaneita.

## Toimintoja:

- Kirjautuminen
- Runon haku nimen tai kategorioiden perusteella
- Runojen luku/selailu
- Runon lisäys lomakkeella
- Runon sisäänluku tiedostosta
- Runon poisto(vain Admin)
- Uuden runon ehdottaminen / ehdotuksen hyväksyminen
- Käyttäjätunnuksen luominen
- Käyttäjätietojen muutos ja tilin poisto(Vain Admin)


(mahdollisesti myös)
- Runojen tykkäys toiminto
- Suosituimpien runojen haku ja järjestäminen
