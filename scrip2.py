import sqlite3

# Connexion à la base de données SQLite (ou création si elle n'existe pas)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Création d'une nouvelle table pour stocker les résultats
cursor.execute('''CREATE TABLE IF NOT EXISTS laurent_nicolas_orders (
                    Date_Commande DATE,
                    Montant_Commande REAL
                 )''')

# Sélection des clients avec consentement marketing
cursor.execute('''SELECT Date_Commande, Montant_Commande
                  FROM commandes
                  WHERE Client_ID = 1''')

# Récupération des résultats
result = cursor.fetchall()

# Insertion des résultats dans la nouvelle table, seulement si les données n'existent pas déjà
for row in result:
    # Vérification de l'existence de la commande
    cursor.execute('''SELECT COUNT(*) FROM laurent_nicolas_orders
                      WHERE Date_Commande = ? AND Montant_Commande = ?''', row)
    exists = cursor.fetchone()[0]

    # Si la commande n'existe pas, on l'insère
    if exists == 0:
        cursor.execute('''INSERT INTO laurent_nicolas_orders (Date_Commande, Montant_Commande)
                          VALUES (?, ?)''', row)

# Validation de la transaction
conn.commit()

# Affichage des résultats insérés dans la nouvelle table
cursor.execute('''SELECT * FROM laurent_nicolas_orders ORDER BY Date_Commande DESC''')
new_result = cursor.fetchall()

for row in new_result:
    print(row)

# Fermeture de la connexion à la base de données
conn.close()
