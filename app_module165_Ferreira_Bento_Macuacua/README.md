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
├── entrypoint.sh
├── init-db.sh
├── .env.example
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

URL : `http://127.0.0.1:5001/`

### 2. Recherche et filtre
La page de recherche permet de filtrer les Pokémon :
- par nom,
- par type principal (`type_1`).

URL : `http://127.0.0.1:5001/search`

### 3. Statistiques et classement
La page de statistiques affiche :
- le top 10 des Pokémon les plus puissants selon `base_stat_total`,
- le nombre de Pokémon par type principal.

URL : `http://127.0.0.1:5001/stats`

---

# Option 1 - Installation avec Docker

## Prérequis
Installer Docker Desktop sur Windows 11. Aucune installation de MongoDB nécessaire.

## Lancement avec Docker Compose

Depuis le dossier de l'application :

```bash
docker compose up --build
```

Docker démarre automatiquement :
- Un conteneur **MongoDB** qui importe les données Pokémon au premier démarrage
- Un conteneur **Flask** qui attend que MongoDB soit prêt avant de démarrer

Ouvrir ensuite le navigateur :

```text
http://127.0.0.1:5001
```

## Premier lancement vs relances

Au **premier lancement**, MongoDB importe automatiquement les données via `init-db.sh`. Les relances suivantes utilisent le volume persistant — l'import ne se répète pas.

Pour repartir de zéro (réimporter les données) :

```bash
docker compose down -v
docker compose up --build
```

## Changer le port (optionnel)

Si le port `5001` est déjà utilisé sur votre machine, créez un fichier `.env` à partir du modèle :

```bash
cp .env.example .env
```

Puis modifiez `APP_PORT` dans `.env` :

```env
APP_PORT=5002
```

L'application sera alors accessible sur `http://127.0.0.1:5002`.

## Logs MongoDB masqués

Les logs de MongoDB sont masqués par défaut. Si ils apparaissent quand même (version Docker Compose < 2.22), utiliser cette commande à la place :

```bash
docker compose up --attach app
```

## Interagir avec les conteneurs

### MongoDB — ouvrir mongosh
```bash
docker exec -it mongo_module165 mongosh
```

Exemples de requêtes une fois dans mongosh :
```js
use my_data_Ferreira_Bento_Macuacua
db.open_data.findOne()
db.open_data.countDocuments()
db.my_team.find()
```

### MongoDB — logs
```bash
docker logs mongo_module165
```

### Application Flask — ouvrir un shell
```bash
docker exec -it app_module165_pokemon sh
```

### Application Flask — logs
```bash
docker logs app_module165_pokemon
```

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
http://127.0.0.1:5001
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
