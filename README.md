# Jobber

## Kuvaus
Käyttäjä voi lisätä työn sivustolle, jonka muut käyttäjät voivat hyväksyä. Työn suorittamisen jälkeen työn tekijä voi antaa arvosanan / arvostelun työlle, joka näkyy työn antajan omalla sivulla. Työn antaja voi myös antaa arvostelun työntekijästä. Työn suorittamisen jälkeen työntekijän tulee ilmottautua pois työstä, jolloin työn lisääjä voi poistaa kyseisen työn. Työntekijä voi seurata sivultaan sitä kuinka paljon on tienannut, sillä työnantaja ilmoittaa työn hinnan. Työntekijät voivat myös kysyä kysymyksiä tehtävässä, ja työn luoja pystyy vastaamaan näihin kysymyksiin.

## Linkki herokuun
* [Jobber](https://tsoha-jobber.herokuapp.com/jobs/new/)

# Dokumentaatio
* [User-Stories](https://github.com/nicholsss/Jobber/blob/master/Documentation/user_story.md)
* [Tietokantakaavio](https://github.com/nicholsss/Jobber/blob/master/Documentation/UusiKaavio.png)

# Käyttäjät
Admin
```
 Username: admin
 Password: admin
```
user
```
 Username: user
 Password: user 
```

## Asennusohjeet

**Tämän vaiheen suorittamiseen tarvitsen [Python3](https://www.python.org/downloads) asennettuna**

Lataa Reposition ZIP-tiedosto tai kopio se komentorivin avulla
```
git clone https://github.com/nicholsss/Jobber.git
```

Tämän jälkeen siirry projektin kansioon
```
cd Jobber
```

asenna projektiin virtuaaliympäristö komentorivillä komennolla

```
python3 -m venv venv
```

Aktivoi virtuaaliympäristö projektille komennolla
```
source venv/bin/activate
```

Lataa projektiin kuuluvat riippuvuudet
```
pip install -r requirements.txt
```

## Heroku
Tämän vaiheen suorittamiseen tarvitaan Heroku [Käyttäjätilin](https://signup.heroku.com), sekä [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

Aktivoi virtuaaliympäristö
```
source venv/bin/activate
```


Luodaan aluksi herokuun projektille oma paikka.
```
heroku create projekti-nimi
```

Lisätään versiohallintaan tieto projektin Heroku paikasta.
```
 https://git.heroku.com/projekti-nimi.git
```

Lähetä projekti Herokuun komennoilla
```
git add .
git commit -m "Message"
git push heroku master
```

**Herokuun lisäämisen jälkeen tahdomme sovellukselle vielä tietokannan**

Lisätään sovellukselle tieto siitä että se on Herokussa
```
heroku config:set HEROKU=1
```

Lisätään sovellukselle tietokanta Herokuun
```
heroku addons:add heroku-postgresql:hobby-dev
```


















