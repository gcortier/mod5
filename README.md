# Template MLOps – FastIA

## Objectif
Ce projet propose une architecture de base pour déployer des applications IA avec un frontend Streamlit et un backend FastAPI, dockerisés et prêts pour l’intégration continue.

## Structure du projet

```
.
├── frontend/
│   ├── app.py           # Interface utilisateur Streamlit
│   └── Dockerfile       # Image Docker du frontend
├── backend/
│   ├── main.py          # API FastAPI (3 routes)
│   ├── modules/
│   │   └── calcul.py    # Fonction de calcul (carré)
│   ├── tests/
│   │   └── test_calcul.py # Test Pytest
│   └── Dockerfile       # Image Docker du backend
├── docker-compose.yml   # Orchestration des services
└── .github/
    └── workflows/
        └── test.yml     # CI GitHub Actions
```

## Fonctionnalités
- **Frontend** : Champ pour saisir un entier, envoi à l’API, affichage du carré.
- **Backend** :
  - `/` : Message d’accueil
  - `/health` : Vérification de santé
  - `/calcul` : Retourne le carré d’un entier (validation Pydantic)
- **Logs** : Intégration Loguru sur front et back
- **Tests** : Couverture de la fonction de calcul avec Pytest
- **CI/CD** : Lancement automatique des tests à chaque push


## Installation & Lancement

### 1. Lancer avec Docker Compose
```bash
docker compose up --build
```
- Frontend : http://localhost:8501
- Backend : http://localhost:8000/docs

### 2. Lancer les tests backend (optionnel, hors Docker)
```bash
cd backend
pytest tests/
```

## Modules à installer (hors Docker)

- **Backend** :
  - fastapi
  - uvicorn
  - loguru
  - pydantic
  - pytest

- **Frontend** :
  - streamlit
  - loguru
  - requests

### Installation rapide (hors Docker)
```bash
pip install fastapi uvicorn loguru pydantic pytest streamlit requests
```
```bash
pip install -r requirements.txt
```
# sauvegarder le fichier requirements.txt
```bash
pip freeze > requirements.txt
```


## CI/CD
- Les tests sont lancés automatiquement via GitHub Actions (`.github/workflows/test.yml`).



## Etapes de travail
- Récupération de tout ce qui a été fait dans les autre modules pour faire un projet minimal avec fast api et streamlit, dockerisé et prêt pour l’intégration continue.
- Exploration du doc github Actions : [Github_Actions](https://docs.google.com/document/d/1EgYEtMalAhMkZm5m78RHs62w6ngZxsqZOKuqMbj2E8c/edit?tab=t.0)
