import pandas as pd
import unicodedata

def nettoyer_colonnes(df):
    """Normalise les noms de colonnes"""
    df.columns = [
        unicodedata.normalize('NFKD', col).encode('ascii', errors='ignore').decode('utf-8').strip().upper()
        for col in df.columns
    ]
    return df

def charger_depuis_google_sheets(sheet_id, sheet_name=None):
    """Charge un DataFrame depuis Google Sheets"""
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx"
    return pd.read_excel(url, sheet_name=sheet_name)