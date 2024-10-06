import sqlite3

# Connexion à la base de données SQLite (ou création si elle n'existe pas)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Création d'une nouvelle table pour stocker le total des commandes du client 61
cursor.execute('''CREATE TABLE IF NOT EXISTS total_ID_61 (
                    total_orders FLOAT
                 )''')

# Sélection et calcul de la somme des Montant_Commande pour le client avec Client_ID = 61
cursor.execute('''SELECT SUM(Montant_Commande)
                  FROM commandes
                  WHERE Client_ID = 61''')

# Récupération du résultat (la somme)
result = cursor.fetchone()

# Arrondi du total des commandes à deux chiffres après la virgule
rounded_total = round(result[0], 2) if result[0] is not None else 0.0

# Insertion du total arrondi des commandes dans la nouvelle table
cursor.execute('''INSERT INTO total_ID_61 (total_orders)
                  VALUES (?)''', (rounded_total,))

# Validation de la transaction
conn.commit()

# Affichage des résultats insérés dans la nouvelle table
cursor.execute('''SELECT * FROM total_ID_61 
               ''')
new_result = cursor.fetchall()

print(new_result)

# Fermeture de la connexion à la base de données
conn.close()
