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
    rencontres = nettoyer_colonnes(charger_depuis_google_sheets(SHEETS_CONFIG["rencontres"]))
    arbitres = nettoyer_colonnes(charger_depuis_google_sheets(SHEETS_CONFIG["arbitres"]))
    
    dispo = nettoyer_colonnes(charger_depuis_google_sheets(SHEETS_CONFIG["disponibilites"]))
    dispo['DATE'] = pd.to_datetime(dispo['DATE'], errors='coerce').dt.date
    dispo['DISPONIBILITE'] = dispo['DISPONIBILITE'].astype(str).str.strip().str.upper()
    dispo['DISPONIBILITE'] = dispo['DISPONIBILITE'].apply(lambda x: "OUI" if x == "OUI" else "NON")
    
    return rencontres, arbitres, dispo

def filtrer_arbitres_eligibles(rencontre, arbitres_dispo):
    """Filtre les arbitres éligibles pour une rencontre"""
    competition = rencontre.iloc[0]['COMPETITION NOM'].strip().upper()
    niveau_min, niveau_max = NIVEAU_COMPETITIONS.get(competition, (None, None))
    
    if niveau_min is None or niveau_max is None:
        st.error(f"Niveau non défini pour la compétition: {competition}")
        return pd.DataFrame()
    
    arbitres_dispo['CATEGORIE'] = arbitres_dispo['CATEGORIE'].str.upper()
    arbitres_dispo['NIVEAU'] = arbitres_dispo['CATEGORIE'].map(CATEGORIE_NIVEAU)
    
    return arbitres_dispo[
        arbitres_dispo['NIVEAU'].apply(lambda x: niveau_min <= x <= niveau_max if pd.notna(x) else False)
    ]

# Chargement des données
rencontres, arbitres, disponibilites = charger_donnees()

# Interface utilisateur
st.subheader("Sélectionnez une rencontre")
rencontre_id = st.selectbox("Rencontre :", rencontres['RENCONTRE NUMERO'].unique())

if rencontre_id:
    rencontre = rencontres[rencontres['RENCONTRE NUMERO'] == rencontre_id]
    st.write("Détails de la rencontre :", rencontre)
    
    date_rencontre = rencontre.iloc[0]['DATE']
    dispo_date = disponibilites[disponibilites['DATE'] == date_rencontre]
    dispo_oui = dispo_date[dispo_date['DISPONIBILITE'] == "OUI"]
    
    # Jointure avec les arbitres
    arbitres_dispo = pd.merge(dispo_oui, arbitres, left_on='NO LICENCE', right_on='NUMERO AFFILIATION', how='left')
    
    # Filtrage par niveau
    arbitres_eligibles = filtrer_arbitres_eligibles(rencontre, arbitres_dispo)
    
    # Affichage des résultats
    st.subheader("Arbitres proposés")
    if not arbitres_eligibles.empty:
        st.dataframe(
            arbitres_eligibles[['NOM', 'PRENOM', 'NO LICENCE', 'CATEGORIE', 'NIVEAU']],
            column_config={
                "NOM": "Nom",
                "PRENOM": "Prénom",
                "NO LICENCE": "N° Licence",
                "CATEGORIE": "Catégorie",
                "NIVEAU": "Niveau"
            },
            use_container_width=True
        )
    else:
        st.warning("Aucun arbitre disponible et compatible avec le niveau requis.")