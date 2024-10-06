import pandas as pd
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('db.db')

# Exécution de la requête SQL et chargement des résultats dans un DataFrame
query = """
SELECT Nom, Prénom, Date_Commande
FROM fusion
WHERE Date_Commande > 01/01/2023;
"""
df = pd.read_sql_query(query, conn)

# Affichage des résultats
print(df)

# Fermeture de la connexion
conn.close()
