# Projet : Création d'une base de données et gestion des Données Clients pour une Campagne Marketing

## Description

Ce projet consiste à concevoir une base de données pour une entreprise collectant des données clients dans le cadre d'une campagne marketing. Deux tables sont fournies : 
- La table **client**
- La table **commande**

Le projet vise à intégrer ces tables dans une base de données, puis à extraire diverses informations pertinentes.

## Objectifs

- Créer une base de données à partir des tables fournies.
- Extraire des informations spécifiques à l'aide de requêtes SQL.

## Extraction des Données

Les informations à extraire sont les suivantes :
1. Les clients ayant consenti à recevoir des communications marketing.
2. Les commandes d'un client spécifique.
3. Le montant total des commandes du client avec l'ID n° 61.
4. Les clients ayant passé des commandes de plus de 100 euros.
5. Les clients ayant passé des commandes après le 01/01/2023.

## Structure du Dépôt

Ce dépôt contient les fichiers suivants :
1. `script.py` : Script de création de la base de données et des tables **client** et **commande** ainsi que l'insertion des données dans les tables.
2. `script1.py` : Script Pyhton pour selectionner les clients ayant consenti à recevoir des communications marketing.
3. `script2.py` : Script Pyhton pour selectionner les commandes d'un client spécifique.
4. `script3.py` : Script Pyhton pour selectionner le montant total des commandes du client avec ID n° 61 .
5. `script4.py` : Script Pyhton pour selectionner les clients ayant passé des commandes après le 01/01/2023.
6. `script5.py` : Script Pyhton pour selectionner les clients ayant passé des commandes de plus de 100 euros.
