import os
import streamlit as st
from loguru import logger
import requests

st.title("Calculateur de carré")

number = st.number_input("Entrez un entier", step=1, format="%d")
API_URL = os.getenv("API_URL", "http://localhost:8000")

if st.button("Calculer le carré"):
    try:
        st.write(f"Envoi de la requête à l'API : {API_URL}/calcul avec le nombre {int(number)}")
        response = requests.post(f"{API_URL}/calcul", json={"number": int(number)})
        if response.status_code == 200:
            result = response.json()["result"]
            st.success(f"Le carré de {int(number)} est {result}")
            logger.info(f"Calcul du carré de {int(number)}: {result}")
        else:
            st.error(f"Erreur: {response.text}")
            logger.error(f"Erreur API: {response.text}")
    except Exception as e:
        st.error(f"Erreur: {e}")
        logger.error(f"Exception: {e}")
