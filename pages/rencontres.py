import streamlit as st
import pandas as pd
from constants import CATEGORIE_NIVEAU, NIVEAU_COMPETITIONS, SHEETS_CONFIG
from utils import nettoyer_colonnes, charger_depuis_google_sheets

# Configuration de la page
st.set_page_config(page_title="Affectation des arbitres", layout="wide")
st.title("Affectation automatique des arbitres aux rencontres")

@st.cache_data
def charger_donnees():
    """Charge toutes les données nécessaires"""
    try:
        # Chargement des rencontres
        rencontres = charger_depuis_google_sheets(SHEETS_CONFIG["rencontres"])
        rencontres = nettoyer_colonnes(rencontres)
        
        # Chargement des arbitres
        arbitres = charger_depuis_google_sheets(SHEETS_CONFIG["arbitres"])
        arbitres = nettoyer_colonnes(arbitres)
        
        # Chargement des disponibilités
        dispo = charger_depuis_google_sheets(SHEETS_CONFIG["disponibilites"])
        dispo = nettoyer_colonnes(dispo)
        
        # Nettoyage des disponibilités
        dispo['DATE'] = pd.to_datetime(dispo['DATE'], errors='coerce').dt.date
        dispo['DISPONIBILITE'] = (
            dispo['DISPONIBILITE']
            .astype(str)
            .str.strip()
            .str.upper()
            .apply(lambda x: "OUI" if x == "OUI" else "NON")
        )
        
        return rencontres, arbitres, dispo
        
    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {str(e)}")
        st.stop()

# Chargement des données avec gestion d'erreur
try:
    rencontres, arbitres, disponibilites = charger_donnees()
except Exception as e:
    st.error(f"Erreur critique: Impossible de charger les données. {str(e)}")
    st.stop()

# ... [le reste de votre code existant] ...