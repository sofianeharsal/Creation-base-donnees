import sqlite3
import csv

# Connexion à la base de données SQLite (ou création si elle n'existe pas)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Création de la table 'clients' si elle n'existe pas déjà
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        "Clients_ID" INTEGER NOT NULL UNIQUE,
        "Nom" TEXT NOT NULL,
        "Prénom" TEXT NOT NULL,
        "Email" TEXT NOT NULL,
        "Téléphone" TEXT,
        "Date_Naissance" DATE,  
        "Adresse" TEXT,
        "Consentement_Marketing" BOOLEAN NOT NULL,
        PRIMARY KEY("Clients_ID")
    )
''')

# Création de la table 'commandes' si elle n'existe pas déjà
cursor.execute('''
    CREATE TABLE IF NOT EXISTS commandes (
        "Commande_ID" INTEGER NOT NULL UNIQUE,
        "Client_ID" INTEGER NOT NULL,
        "Date_Commande" DATE NOT NULL,  
        "Montant_Commande" NUMERIC NOT NULL,
        PRIMARY KEY("Commande_ID"),
        FOREIGN KEY ("Client_ID") REFERENCES clients("Clients_ID")
        ON UPDATE NO ACTION ON DELETE NO ACTION
    )
''')

# Fonction pour insérer les données du fichier CSV dans la table 'clients'
def inserer_clients_depuis_csv(csv_fichier):
    with open(csv_fichier, 'r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)  # Ignorer la ligne d'en-tête si elle existe
        for ligne in lecteur:
            cursor.execute('''
                INSERT INTO clients (Clients_ID, Nom, Prénom, Email, Téléphone,
                            Date_Naissance, Adresse, Consentement_Marketing) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', ligne)
    conn.commit()

# Fonction pour insérer les données du fichier CSV dans la table 'commandes'
def inserer_commandes_depuis_csv(csv_fichier):
    with open(csv_fichier, 'r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)  # Ignorer la ligne d'en-tête si elle existe
        for ligne in lecteur:
            cursor.execute('''
                INSERT INTO commandes (Commande_ID, Client_ID, Date_Commande, Montant_Commande)
                VALUES (?, ?, ?, ?)
            ''', ligne)
    conn.commit()

# Utilisation des fonctions pour insérer les données des CSV
inserer_clients_depuis_csv('clients.csv')
inserer_commandes_depuis_csv('commandes.csv')

# Fermeture de la connexion à la base de données
conn.close()
