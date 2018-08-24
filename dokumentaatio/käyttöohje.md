
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

Etusivulle pääsee palaamaan muista sovelluksen paikoista painamalla navigaatiopalkin vasemmassa yläreunassa olevasta "Runoarkisto" nimestä.

## *kaikkien runojen listaus ja yksittäisen runon tietojen ja kategorioiden näyttö* 

Voit listata näkyville kaikkien runojen otsikko linkit painamalla "runot" linkkiä navigaatiopalkissa. Painamalla runon nimeä/ linkkiä, avautuu yksittäinen runo näkyville. Jos haluat myös kyseisen runon kategoriat näkyville paina "runon kategoriat" linkkiä.

Mikäli olet kirjautunut ylläpitäjänä näet yksittäisen runon listauksen yhteydessä myös "runon muokkautilaan napin, josta pääset muokkaamaan ja poistamaan runon sekä poistamaan ja lisäämään sille uusia kategorioita. 

## *Runojen haku* 

Voit etsiä runoja runoarkistosta nimen tai kategorian perusteella painamalla "runot" linkkiä navigaatiopalkissa. Syöttämällä lomakkeeseen arkistossa olevan runon nimen tai kategorian, näet kyseisen runon tai listan hakemaasi kategoriaan kuuluvista runoista. Jos hakemaasi runoa tai kategoriaa ei löydy, saat ilmoituksen.

# Kirjautuneelle sallittuja toimintoja

## *Runojen lisäys*

Voit kirjata uuden runon järjestelmään painamalla "Lisää runo" linkkiä navigaatiopalkissa. Syötä avautuvaan lomakkeeseen pyydetyt tiedot, korjaa tarvittaessa virheilmoitusten ilmoittamat virheet syötteissä. Lisätty runo näkyy aukeavassa kirjautuneen käyttäjän runojen listaus näkymässä.

## *Kirjautuneen käyttäjän runojen listaus ja yksittäisen runon tiedot*

Voit listata lisäämiesi runojen otsikot näkyville painamalla "lisäämäsi runot" linkkiä navigaatiopalkissa. Klikkaamalla runon nimeä/linkkiä saat kyseisen runon kokonaan näkyviin sekä napin runon muokkaustilaan. 

## *Runon muokkaustila* 

Painamalla käyttäjän yksittäisen runon näkymässä nappia "runon muokkaustilaan" saat näkyviin "muokkaa runoa, poista runo, lisää kategoria ja poisto kategoria" napit, joiden kautta voit suorittaa kyseiset toiminnot valitulle runolle. 

#### *Runon muokkaus ja poisto* 
Runon muokkausnappi avaa esitäytetyn muokkauslomakkeen valitsemastasi yksittäisestä runosta. Muokkaa haluamiasi kenttiä ja korjaa mahdollisten virheilmoitusten ilmoittamat virheet syötteissä. Painamalla "Muokkaa runoa!" nappia tekemäsi muutokset tallentuvat järjestelmään ja näet muokatun runosi. Poisto nappi poistaa runon olemastasi näkymästä.

#### *Kategorian lisäys ja poisto* 
Kategorian lisäysnappi avaa täytettävän lomakkeen kategorian lisäykseen. "Poista kategoria" napista voit poistaa kyseisen kategorian.

**POISTAMINEN POISTAA KYSEISEN KOHTEEN PYSYVÄSTI JÄRJESTELMÄSTÄ EIKÄ SITÄ VOIDA TÄMÄN JÄLKEEN PALAUTTAA!**



# Ylläpitäjälle rajattuja toimintoja


## *Käyttäjien hallinnointi*
todo

## *Kaikkien runojen muokkaus*

Ylläpitäjänä näet kaikkien runojen yksittäisen runon listauksen yhteydessä lisäksi myös "runon muokkaustilaan" napin, josta pääset muokkaamaan ja poistamaan runon sekä poistamaan ja lisäämään sille uusia kategorioita. (kts. alun kohta "kaikkien runojen listaus"..)

Kaikkien runojen muokkaustila toimii vastaavalla tavalla kuin kirjautuneen käyttäjän runojen muokkaustila. (kts.ohjeet kohdasta "Kirjautuneen käyttäjän runojen listaus ja yksittäisen runon tiedot"..)


## *Kategorioiden listaus ja poisto* 

Pääkäyttäjänä pääset listaamaan kaikki kategoriat navigaatiopalkin "kategoriat" linkin kautta. Listauksen poistonapeista pystyt poistamaan aina ko. kategorian.
