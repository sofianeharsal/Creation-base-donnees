import sqlite3

# Connexion à la base de données SQLite (ou création si elle n'existe pas)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Création d'une nouvelle table pour stocker les résultats
cursor.execute('''CREATE TABLE IF NOT EXISTS clients_marketing (
                    Nom TEXT,
                    Prenom TEXT
                 )''')

# Sélection des clients avec consentement marketing
cursor.execute('''SELECT Nom, Prénom
                  FROM clients
                  WHERE Consentement_Marketing = 1''')

# Récupération des résultats
result = cursor.fetchall()

# Insertion des résultats dans la nouvelle table
cursor.executemany('''INSERT INTO clients_marketing (Nom, Prenom)
                      VALUES (?, ?)''', result)

# Validation de la transaction
conn.commit()

# Affichage des résultats insérés dans la nouvelle table
cursor.execute('SELECT * FROM clients_marketing')
new_result = cursor.fetchall()

for row in new_result:
    print(row)

# Fermeture de la connexion à la base de données
conn.close()
