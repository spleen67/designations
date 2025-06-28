# Fichier: constants.py

SHEETS_CONFIG = {
    "disponibilites": "https://docs.google.com/spreadsheets/d/113KAFUl9E4ceFqm-gIfQ-zhigYGnOGPh/export?format=xlsx",
    "arbitres": "https://docs.google.com/spreadsheets/d/1UUZBFPMCkVGzVKeTP_D44ZpGwTHlu0Q0/export?format=xlsx",
    "rencontres": "https://docs.google.com/spreadsheets/d/1cM3QiYhiu22sKSgYKvpahvNWJqlxSk-e/export?format=xlsx"  # À compléter 
}

# Niveaux de compétition (exemple)
NIVEAU_COMPETITIONS = {
   "ELITE 1 FEMININE": (6, 4), "ELITE 2 FEMININE": (7, 6),
    "ELITE ALAMERCERY": (7, 6), "ELITE CRABOS": (6, 4),
    "ESPOIRS FEDERAUX": (6, 4), "EUROPEAN RUGBY CHAMPIONS CUP": (1, 1),
    "EXCELLENCE B - CHAMPIONNAT DE FRANCE": (9, 7), "FEDERALE 1": (6, 6),
    "FEDERALE 2": (7, 7), "FEDERALE 3": (8, 8),
    "FEDERALE B - CHAMPIONNAT DE FRANCE": (9, 7),
    "FEMININES MOINS DE 18 ANS A XV - ELITE": (7, 6),
    "FEMININES REGIONALES A X": (13, 10),
    "FEMININES REGIONALES A X « MOINS DE 18 ANS »": (14, 13),
    "REGIONAL 1 U16": (15, 9), "REGIONAL 1 U19": (10, 9),
    "REGIONAL 2 U16": (15, 9), "REGIONAL 2 U19": (13, 9),
    "REGIONAL 3 U16": (15, 9), "REGIONAL 3 U19": (13, 9),
    "REGIONALE 1 - CHAMPIONNAT TERRITORIAL": (9, 7),
    "REGIONALE 2 - CHAMPIONNAT TERRITORIAL": (11, 9),
    "REGIONALE 3 - CHAMPIONNAT TERRITORIAL": (13, 9),
    "RESERVES ELITE": (7, 6),
    "RESERVES REGIONALES 1 - CHAMPIONNAT TERRITORIAL": (11, 9),
    "RESERVES REGIONALES 2 - CHAMPIONNAT TERRITORIAL": (13, 11)
}

# Mapping des catégories d'arbitres à un niveau numérique
CATEGORIE_NIVEAU = {
    INTERNATIONNAUX": 1, "2EME DIVISION PRO": 2, "NATIONALE 1 ET 2": 3,
    "ARBITRES ASSISTANTS PRO": 4, "ARBITRES ASSISTANTS NAT": 5,
    "DIVISIONNAIRES 1": 6, "DIVISIONNAIRES 2": 7, "DIVISIONNAIRES 3": 8,
    "LIGUE 1": 9, "LIGUE 2": 10, "LIGUE 3": 11, "LIGUE 4": 12, "LIGUE 5": 13,
    "MINEURS 17 ANS": 14, "MINEURS 16 ANS": 15, "MINEURS 15 ANS": 16
}
