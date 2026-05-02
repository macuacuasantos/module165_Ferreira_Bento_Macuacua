# Application Module 165 - Pokémon

## Groupe
Guilherme Ferreira, Ricardo Bento et Santos Macuácua

## Description
Cette application Python Flask exploite les données Pokémon stockées dans une base de données MongoDB standalone.

- Base de données : `my_data_Ferreira_Bento_Macuacua`
- Collection : `open_data`
- Langage : Python

## Architecture générale

```text
app_module165_Ferreira_Bento_Macuacua/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── search.html
    └── stats.html
```

## Technologies utilisées
- Python 3.12
- Flask
- PyMongo
- MongoDB standalone
- HTML / CSS
- Docker

## Fonctionnalités

### 1. Liste des Pokémon
La page d'accueil affiche les 50 premiers Pokémon de la collection `open_data`.

URL : `http://127.0.0.1:5000/`

### 2. Recherche et filtre
La page de recherche permet de filtrer les Pokémon :
- par nom,
- par type principal (`type_1`).

URL : `http://127.0.0.1:5000/search`

### 3. Statistiques et classement
La page de statistiques affiche :
- le top 10 des Pokémon les plus puissants selon `base_stat_total`,
- le nombre de Pokémon par type principal.

URL : `http://127.0.0.1:5000/stats`

---

# Option 1 - Installation avec Docker

## Prérequis
Installer Docker Desktop sur Windows 11.

Le serveur MongoDB standalone doit être lancé sur le PC et la base suivante doit exister :

```text
my_data_Ferreira_Bento_Macuacua
```

La collection suivante doit aussi exister :

```text
open_data
```

## Lancement avec Docker Compose

Depuis le dossier de l'application :

```bash
docker compose up --build
```

Ouvrir ensuite le navigateur :

```text
http://127.0.0.1:5000
```

## Configuration MongoDB sans authentification

Dans `docker-compose.yml`, la configuration par défaut est :

```yaml
MONGO_URI: "mongodb://host.docker.internal:27017/"
MONGO_DB: "my_data_Ferreira_Bento_Macuacua"
MONGO_COLLECTION: "open_data"
```

`host.docker.internal` permet au conteneur Docker d'accéder au MongoDB installé sur le PC Windows.

## Configuration MongoDB avec authentification

Si MongoDB utilise l'authentification, remplacer `MONGO_URI` dans `docker-compose.yml` par :

```yaml
MONGO_URI: "mongodb://userModify:userModify@host.docker.internal:27017/my_data_Ferreira_Bento_Macuacua?authSource=my_data_Ferreira_Bento_Macuacua"
```

Adapter le mot de passe si nécessaire.

## Arrêter l'application Docker

```bash
docker compose down
```

---

# Option 2 - Installation locale sur Windows 11

## Prérequis
Installer :
- Python 3
- MongoDB Community Server
- MongoDB Database Tools si nécessaire

Vérifier que MongoDB est lancé.

## Créer un environnement virtuel

```bash
python -m venv venv
```

Activer l'environnement virtuel :

```bash
venv\Scripts\activate
```

## Installer les dépendances

```bash
pip install -r requirements.txt
```

## Lancer l'application

```bash
python app.py
```

Ouvrir ensuite :

```
http://127.0.0.1:5000
```

## Variables d'environnement disponibles

L'application peut être configurée avec :

```
MONGO_URI
MONGO_DB
MONGO_COLLECTION
```

Valeurs par défaut :

```
MONGO_URI=mongodb://localhost:27017/
MONGO_DB=my_data_Ferreira_Bento_Macuacua
MONGO_COLLECTION=open_data
```

## Conclusion
Cette application répond aux critères du module 165, car elle exploite une base MongoDB standalone et propose trois affichages différents des données Pokémon : liste, recherche et statistiques.
