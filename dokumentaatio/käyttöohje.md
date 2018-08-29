
# Käyttöohjeita sovelluksen toiminnallisuuksille

Tähän ohjeeseen on kirjattu käyttöohjeita sovelluksen eri toiminnallisuuksille.

### Kirjautuminen

Sovelluksen sivuston osia on suojattu salasanalla, jotta ulkopuoliset eivät pääse käsiksi sen kaikkiin toiminnallisuuksiin. Sovellukseen on määritelty pääkäyttäjän ADMIN ja tavallisen käyttäjän USER tilit, jotka ovat sovelluksen testikäytön kannalta olennaisia. Nämä tilit ovat:

        | käyttäjärooli  | Käyttäjätunnus   | Salasana   |
        | ------------   | ---------------- | ---------- |
        | admin          | hello            | world      |
        | user           | test             | test       |

Sovellukseen on mahdollista luoda uusia user käyttäjätilejä rekisteröintilomakkeen kautta. Kirjautumalla admin tunnuksella on myös mahdollista antaa tavalliselle käyttäjälle admin oikeudet. Kirjautumaton käyttäjä ohjataan kirjautumissivulle joko Kirjaudu -linkistä tai jos hän yrittää navigoida suojatuille sovelluksen sivuille.

Kirjautumattomalla käyttäjällä on pääsy etusivulle ja runojen lukemiseen sekä hakemiseen. Kirjautunut käyttäjä puolestaan päsee lisäksi listaamaan, lisäämään, muokkaamaan ja poistamaan omia runoja.  Pääkäyttäjä pääsee lisäksi käyttäjien hallintaan, sekä muokkaamaan ja poistamaan kaikkia runoja ja kategorioita.

Sivut ja toiminnot joihin ko. käyttäjällä ei ole oikeuksia ovat piilotettuna käyttäjältä.

# Kaikille sallittuja toimintoja

## *etusivu* 

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/etusivu.png" width="700">

Kirjautuessasi sovellukseen sinut ohjataan etusivulle, jossa on lyhyt esittely sovelluksesta sekä aforismi. Navigaatiopalkin linkeistä pääset haluamiisi toimintoihin.

Etusivulle pääsee palaamaan muista sovelluksen paikoista painamalla navigaatiopalkin vasemmassa yläreunassa olevasta "Runoarkisto" nimestä.


## *kaikkien runojen listaus ja yksittäisen runon tietojen ja kategorioiden näyttö* 

Voit listata näkyville kaikki runot aakkosjärjestyksessä painamalla "runot" linkkiä navigaatiopalkissa. Runoista näytetään 10 runoa kerrallaan. Sivun alareunan seuraav runo painikkeesta pääset selaamaan runoja eteenpäin ja edellinen taaksepäin. Sivun alareunassa myös kerrotaanpaljonko runoja on yhteensä

Mikäli olet kirjautunut näet runon listauksen yhteydessä myös runon tykkäys napin.

Mikäli olet kirjautunut ylläpitäjänä näet yksittäisen runon listauksen yhteydessä myös "runon muokkautilaan napin, josta pääset muokkaamaan ja poistamaan runon sekä poistamaan ja lisäämään sille uusia kategorioita. 

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/runot_kaikki.png" width="700">

## *Runojen haku* 

Voit etsiä runoja runoarkistosta nimen tai kategorian perusteella painamalla "etsi" linkkiä navigaatiopalkissa. Syöttämällä lomakkeeseen arkistossa olevan runon nimen tai kategorian, näet kyseisen runon tai listan hakemaasi kategoriaan kuuluvista runoista. Jos hakemaasi runoa tai kategoriaa ei löydy, saat ilmoituksen.

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/haku.png" width="700">

## *Top10 tykätyimpien runojen listaus* 

Navikaatiopalkin "top10" linkistä pääset tarkastelemaan 10 tykätyintä runoa ja niiden tykkäysten määrää. Klikkaamalla runoa, näet sen kokonaisuudessaan.

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/top10.png">

## *Rekisteröityminen=uuden käyttäjän lisääminen ja kirjautuminen*

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/rekist.png" width="700">

##### rekisteröityminen
Sovellukseen on tehty erillinen lomakesivu rekisteröinnille eli uuden käyttäjän luomiselle. Kyseiselle sivulle pääsee painamalla navigaatiopalkin oikean laidan linkkiä: *"Rekisteröidy"*. Syötä avautuneeseen lomakkeen kenttiin pyydetyt tiedot ja ota huomioon nimimerkeille ja salasanoille annetut rajoitteet. Korjaa tarvittaessa syötteesi virheilmoitusten ilmoittamista virheistä. Lomake rekisteröi käyttäjän rooliksi automaattisesti USER:in

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/kirjaudu.png" width="700">

##### kirjautuminen
Rekisteröinnin onnistumisen jälkeen sovellukseen pääsee kirjautumaan avautuvan kirjautumislomakkeen kautta ja myös navigaatiopalkin linkin *"Kirjaudu"* kautta. Navigaation oikeassa reunassa näet kirjautuneen käyttäjänimen ja roolin USER. Uloskirjautuminen tapahtuu oikeassa reunassa olevan "kirjaudu ulos" navigaatiolinkin kautta, jota painamalla ohjaudut etusivulle.

# Kirjautuneelle sallittuja toimintoja

## *Runojen lisäys*

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/runonlisäys.png" width="700">

Voit kirjata uuden runon järjestelmään painamalla "Lisää runo" linkkiä navigaatiopalkissa. Syötä avautuvaan lomakkeeseen pyydetyt tiedot, korjaa tarvittaessa virheilmoitusten ilmoittamat virheet syötteissä. Lisätty runo näkyy aukeavassa kirjautuneen käyttäjän runojen listaus näkymässä.

## *Kirjautuneen käyttäjän runojen listaus ja yksittäisen runon tiedot*

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/kayttajan_runot.png" width="700">

Voit listata lisäämiesi runojen otsikot näkyville painamalla "lisäämäsi runot" linkkiä navigaatiopalkissa. Klikkaamalla runon nimeä/linkkiä saat kyseisen runon kokonaan näkyviin sekä napin runon muokkaustilaan. 

## *Runon muokkaustila* 

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/muokkaus.png" width="700">

Painamalla käyttäjän yksittäisen runon näkymässä nappia "runon muokkaustilaan" saat näkyviin "muokkaa runoa, poista runo, lisää kategoria ja poisto kategoria" napit, joiden kautta voit suorittaa kyseiset toiminnot valitulle runolle. 

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/modif.png" width="700">

#### *Runon muokkaus ja poisto* 
Runon muokkausnappi avaa lisäämislomakkeen kaltaisen, mutta esitäytetyn muokkauslomakkeen valitsemastasi yksittäisestä runosta. Muokkaa haluamiasi kenttiä ja korjaa mahdollisten virheilmoitusten ilmoittamat virheet syötteissä. Painamalla "Muokkaa runoa!" nappia tekemäsi muutokset tallentuvat järjestelmään ja näet muokatun runosi. Poisto nappi poistaa runon.

#### *Kategorian lisäys ja poisto* 
Kategorian lisäysnappi avaa täytettävän lomakkeen kategorian lisäykseen. "Poista kategoria" napista voit poistaa kyseisen kategorianko runolta.

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/lisaa_kategoria.png" width="600">

**POISTAMINEN POISTAA KYSEISEN KOHTEEN PYSYVÄSTI JÄRJESTELMÄSTÄ EIKÄ SITÄ VOIDA TÄMÄN JÄLKEEN PALAUTTAA!**
poistonapit merkitty violetinsävyisellä värillä


# Ylläpitäjälle rajattuja toimintoja

Ainoastaan ylläpitäjän hallussa olevat navigaatiolinkit näkyvät vihreällä.

## *Käyttäjien hallinnointi, muokkaus, poisto ja listaus *

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/hallinta.png" width="700">

Pääkäyttäjänä pääset hallinnoimaan ja listaamaan käyttäjien tiedot navigaatiopalkin "käyttäjät" linkin kautta. Linkistä avautuvassa käyttäjien hallinta näkymässä pystyt "muokkaa" ja "poista" napista muokkaamaan ja poistamaan käyttäjän. Huom!! Käyttäjän poisto napi poistaa järjestelmästä myös hänen runonsa kategorioineen.

Muokkaus nappi avaa yksittäisen käyttäjän tiedoilla esitäytetyn muokkauslomakkeen. Lomakkeeseen on lisätty rekisteröitymisliomakkeesta poiketen nyt myös rooli selection kenttä. Rooli kentän avulla voi muokata USER käyttäjästä ADMIN käyttäjän ja toisinpäin. 

Näkymästä voit lisäksi klikata linkistä "Katso ketkä käyttäjät ovat lisänneet runoja" näkyville listan käyttäjistä joilla on runoja lisättynä ja mitä runoja ko. käyttäjällä on.

Samassa näkymässä alimpana on runojen tykkäysten resetointi eli poisto nappi, joka poistaa kaikkien runojen tykkäykset.


## *Kaikkien runojen muokkaus*

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/runot_admin.png" width="700">
          
Ylläpitäjänä näet kaikkien runojen listauksen yhteydessä tykkäys napin lisäksi myös "runon muokkaustilaan" napin, josta pääset muokkaamaan ja poistamaan runon sekä poistamaan ja lisäämään sille uusia kategorioita. (kts. alun kohta "kaikkien runojen listaus..")

Kaikkien runojen muokkaustila toimii vastaavalla tavalla kuin kirjautuneen käyttäjän runojen muokkaustila. (kts.ohjeet kohdasta "Kirjautuneen käyttäjän runojen listaus ja yksittäisen runon tiedot")


## *Kategorioiden listaus ja poisto* 

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/kategoriat.png" width="700">

Pääkäyttäjänä pääset listaamaan kaikki kategoriat navigaatiopalkin punaisen "kategoriat" linkin kautta. Listauksen poisto napeista pystyt poistamaan aina ko. kategorian.

## *Tilastoja*

Navikaation "tilastoja" linkikiä painamalla pääset tarkastelemaan mutamia sivun tilastoja.

<img src="https://github.com/vsvala/Runoarkisto/blob/master/dokumentaatio/kuvat/stats.png" width="700">


