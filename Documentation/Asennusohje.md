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