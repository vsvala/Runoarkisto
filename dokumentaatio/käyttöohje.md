
# Käyttöohjeita sovelluksen toiminnallisuuksille

Tähän ohjeeseen on kirjattu käyttöohjeita sovelluksen eri toiminnallisuuksille.

### Kirjautuminen

Sovelluksen sivuston osia on suojattu salasanalla, jotta ulkopuoliset eivät pääse käsiksi sen kaikkiin toiminnallisuuksiin. Sovellukseen on määritelty pääkäyttäjän ja tavallisen käyttäjän tilit, jotka ovat sovelluksen testikäytön kannalta olennaisia. Nämä tilit ovat:

        | käyttäjärooli  | Käyttäjätunnus   | Salasana   |
        | ------------   | ---------------- | ---------- |
        | admin          | hello            | world      |
        | user           | test             | test       |

Sovellukseen on mahdollista luoda uusia user käyttäjätilejä rekisteröintilomakkeen kautta. Kirjautumalla admin tunnuksella on myös mahdollista antaa tavalliselle käyttäjälle admin oikeudet. Kirjautumaton käyttäjä ohjataan kirjautumissivulle joko Kirjaudu -linkistä tai jos hän yrittää navigoida suojatuille sovelluksen sivuille.

Kirjautumattomalla käyttäjällä on pääsy etusivulle ja runojen lukemiseen sekä hakemiseen. Kirjautunut käyttäjä puolestaan päsee lisäksi lisäämään, muokkaamaan ja poistamaan omia runoja.  Pääkäyttäjä pääsee lisäksi käyttäjien hallintaan, sekä muokkaamaan ja poistamaan kaikkia runoja ja kategorioita.

Sivut ja toiminnot joihin ko. käyttäjällä ei ole oikeuksia ovat piilotettuna käyttäjältä.

# Kaikille sallittuja toimintoja

## *Rekisteröityminen / uuden käyttäjän luonti, kirjautuminen*

Sovellukseen on tehty erillinen sivu rekisteröinnille eli uuden käyttäjän luomiselle. Kyseiselle sivulle pääsee painamalla navigaatiopalkin oikean laidan linkkiä: *"Rekisteröidy"*.
Syötä lomakkeen kenttiin pyydetyt tiedot ja ota huomioon nimimerkeille ja salasanoille annetut rajoitteet. Korjaa tarvittaessa syötteesi virheilmoitusten ilmoittamista virheistä. Rekisteröinnin onnistumisen jälkeen sovellukseen pääsee kirjautumaan avautuvan kirjautumislomakkeen kautta ja myös navigaatiopalkin linkin *"Kirjaudu"* kautta. Navigaation oikeassa reunassa näet kirjautuneen käyttäjänimen ja roolin. Uloskirjautuminen tapahtuu oikeassa reunassa olevan "kirjaudu ulos" navigaatiolinkin kautta, jota painamalla ohjaudu etusivulle.

## *etusivu* 
Kirjautuessasi sovellukseen sinut ohjataan etusivulle, jossa on lyhyt esittely sovelluksesta sekä aforismi. Navigaatiopalkin linkeistä pääset haluamiisi toimintoihin.

Etusivulle pääsee palaamaan muista sovelluksen paikoista painamalla navigaatiopalkin vasemmassa yläreunassa olevasta "Sukelluskeskus Dyykkimestarit" nimestä.

## *kaikkien runojen listaaminen ja yksittäisen runon  tietojen näyttö* 

Voit listata kaikkien runojen otsikko linkit painamalla "runot" linkkiä navigaatiopalkissa. Painamalla otsikko linkkiä, avautuu yksittäinen runo näkyville. Jos haluat myös kyseisen runon kategoriat näkyville paina *"runon kategoriat"* linkkiä.
Mikäli olet kirjautunut ylläpitäjänä, näet listauksen vain itse kirjatuista työtehtävistä. Mikäli olet kirjautunut ylläpitäjänä näet yksittäisen runon mukana myös napit, joista pääset muokkaamaan, poistamaan runon tai lisäämään sille uusia kategorioita. 

## *Runojen haku* 

Voit etsiä runoja runoarkistosta nimen tai kategorian perusteella painamalla "runot" linkkiä navigaatiopalkissa. Syöttämällä lomakkeeseen arkistossa olevan runon nimen tai kategorian, näet kyseisen runon tai listan hakemaasi kategoriaan kuuluvista runoista. Jos hakemaasi runoa tai kategoriaa ei löydy, saat ilmoituksen.

# Kirjautuneelle sallittuja toimintoja

## *Runojen lisäys*

Voit kirjata uuden runon järjestelmään painamalla "Lisää runo" linkkiä navigaatiopalkissa. Syötä avautuvaan lomakkeeseen pyydetyt tiedot, korjaa tarvittaessa virheilmoitusten ilmoittamat virheet syötteissä. Lisätty runo näkyy aukeavassa listaus sivussa.

## *Kirjautuneen käyttäjän runojen listaus, muokkaus, poisto ja kategorioiden lisäys *

Voit listata lisäämäsi runot näkyville painamalla "lisäämäsi runot" linkkiä navigaatiopalkissa. "muokkaa runoa, poista runo, lisää runollle kategoria" nappien kautta voit suorittaa kyseiset toiminnot. Runon muokkausnappi avaa esitäytetyn muokkauslomakkeen valitsemastasi yksittäisestä runosta.Lomakkeen lähetysnapin painallus näyttää muokkaamasi runon.  Kategorian lisäysnappi avaa lomakkeen kategorian lisäykseen. Lomakkeen lähetys näyttää runon ja sen kategoriat(kesken). Poisto nappi poistaa runon olemastasi näkymästä.


## *Runon muokkaaminen* 

Kirjautuneena käyttäjänä voit muokata ja poistaa lisäämiäsi runoja "lisäämäsi runot" listauksen kautta. Paina "Muokkaa" nappia. Tämä avaa yksittäisen työtehtävän tiedot sisältävän muokkauslomakesivun. Muokkaa haluamiasi kenttiä ja korjaa mahdollisten virheilmoitusten ilmoittamat virheet syötteissä. Painamalla "Muokkaa tehtävää!" nappia tekemäsi muutokset tallentuvat järjestelmään ja sinut ohjataan lisäämmäsi runot näkymään.


## *Runon poistaminen* 

**tavallinen käyttäjä**
Voit poistaa omia järjestelmään kirjaamiasi runoja lisäämäsi runot listauksen kautta. Paina "poista runo" nappia. Tämä poistaa työtehtävän järjestelmästä.


**RUNON POISTAMINEN POISTAA RUNON PYSYVÄSTI JÄRJESTELMÄSTÄ EIKÄ SITÄ VOIDA TÄMÄN JÄLKEEN PALAUTTAA!**


# Ylläpitäjälle rajattuja toimintoja


## *Käyttäjien hallinnointi*
todo

## *Kaikkien runojen poisto, muokkaus*

Pääkäyttäjänä voit lisäksi poistaa kaikkia järjestelmään kirjattuja runoja kaikkien runojen listaus tarkastelun kautta. Paina "Poista" nappia. Tämä poistaa työtehtävän järjestelmästä.
todo

## *Kategorioiden listaus ja poisto* (vain pääkäyttäjä)
todo
Pääkäyttäjänä pääset hallinnoimaan kategorioita navigaatiopalkin "kategoriat" linkin kautta. Tällä hetkellä poistonappi...TODO ehkä listaus mitkä runot jategorioiden alle????..
