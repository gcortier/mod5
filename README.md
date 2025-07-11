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
- Le `.venv` 
```bash
python -m venv .venv
```
- activer l'environnement virtuel :
```bash
.venv\Scripts\Activate.ps1
```

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
pip install fastapi uvicorn loguru pydantic pytest streamlit requests prometheus-client python-multipart psutil
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
- La dernière version de chaque image Docker est poussée sur Docker Hub à chaque push.



## Etapes de travail
- Récupération de tout ce qui a été fait dans les autre modules pour faire un projet minimal avec fast api et streamlit, dockerisé et prêt pour l’intégration continue.
- Exploration du doc github Actions : [Github_Actions](https://docs.google.com/document/d/1EgYEtMalAhMkZm5m78RHs62w6ngZxsqZOKuqMbj2E8c/edit?tab=t.0)
- Compliqué de setup correctement les contecte d'executions.
- Phase docker build CD
- Ajout des secrets DOCKER_* dans la partie action de github
- Exploration du doc et tests pour Uptime Kuma + hook discord
- Explorations et setup à partir du projet git docker-compose-prometheus-grafana en référence + qq articles :
  - [Building a Monitoring Stack with Prometheus, Grafana, and Alerting: A Docker Compose](https://medium.com/@ravipatel.it/building-a-monitoring-stack-with-prometheus-grafana-and-alerting-a-docker-compose-ef78127e4a19)
  - Monitoring systeme avec Prometheus et Grafana (dashboard 1860) : on doit ajouter un container node-exporter pour monitorer le système
  - Ajout et visualisation du dashboard dans Grafana
    - Trouver un moyen d'automatiser les logs des appels aux routes : implementation 'prometheus-fastapi-instrumentator'
  - Ajout d'un dashboard pour visualiser les appels à l'API FastAPI

