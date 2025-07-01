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

## Prérequis
- Docker & Docker Compose
- Python 3.10+

## Installation & Lancement

### 1. Cloner le dépôt
```bash
git clone <repo_url>
cd mod5
```

### 2. Lancer avec Docker Compose
```bash
docker compose up --build
```
- Frontend : http://localhost:8501
- Backend : http://localhost:8000/docs

### 3. Lancer les tests backend (optionnel, hors Docker)
```bash
cd backend
pip install -r <(pip freeze > requirements.txt && cat requirements.txt)
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

## CI/CD
- Les tests sont lancés automatiquement via GitHub Actions (`.github/workflows/test.yml`).

## Auteur
FastIA – Template MLOps 2025
