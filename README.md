## Pré-requis - Install des requirements

toute les dependances sont dans requirements.txt

## Utilisation

commande pour lancer le serveur
```
python app/main.py
```

lien de l'api:
```
http://127.0.0.1:8000/
```

## Architecture

```
├── app/
│   ├── database.py
│   ├── api.py
│   ├── main.py
│   ├── exceptions/
│   │   └── exceptions.py
│   ├── models/
│   │   └── Gamesql.py 
│   ├── routes/
│   │   └── route.py
│   ├── templates/
│       └── Game.py 
│   
├── test/
│    └── unit/
│         └── app/
│              └── test.py
│
├── requirements.txt
```

## test Unitaire

Les tests unitaire sont dans le fichier ```test/unit/app/test.py```
