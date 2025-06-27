import pandas as pd
import unicodedata

def nettoyer_colonnes(df):
    """Normalise les noms de colonnes d'un DataFrame"""
    if isinstance(df, pd.DataFrame):
        df.columns = [
            unicodedata.normalize('NFKD', col).encode('ascii', errors='ignore').decode('utf-8').strip().upper()
            for col in df.columns
        ]
    return df

def charger_depuis_google_sheets(sheet_id, sheet_name=0):
    """Charge un DataFrame depuis Google Sheets"""
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx"
    try:
        # sheet_name=0 pour charger la première feuille par défaut
        return pd.read_excel(url, sheet_name=sheet_name)
    except Exception as e:
        raise Exception(f"Erreur lors du chargement Google Sheet {sheet_id}: {str(e)}")