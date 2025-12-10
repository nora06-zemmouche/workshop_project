Mini-projet : Suivi et analyse de la consommation énergétique
1. Contexte

Ce mini-projet vise à simuler un dispositif de suivi et d’analyse de la consommation énergétique.
Il met en pratique les notions de programmation orientée objet (POO), de simulation de capteurs IoT, de détection d’anomalies, et d’utilisation de MongoDB pour le stockage des données.

2. Objectifs

Mettre en place une architecture POO.

Simuler des capteurs IoT générant des valeurs aléatoires.

Stocker les mesures dans une base MongoDB.

Détecter automatiquement les anomalies dans la consommation.

Assurer la qualité logicielle via Pytest et flake8.

3. Structure du projet
workshop_project/
├─ src/
│  ├─ anomaly_detector.py
│  ├─ mongodb_client.py
│  └─ sensor.py
├─ tests/
│  ├─ test_anomaly.py
│  ├─ test_mongodb.py
│  └─ test_sensor.py
├─ venv/ (environnement virtuel, ignoré par Git)
├─ requirements.txt
├─ setup.cfg (configuration flake8)
└─ README.md

4. Installation

Cloner le dépôt :

git clone <URL_DU_DEPOT>
cd workshop_project


Créer et activer l'environnement virtuel :

python -m venv venv
.\venv\Scripts\Activate.ps1  # sur Windows PowerShell


Installer les dépendances :

pip install -r requirements.txt

5. Utilisation

Lancer les tests unitaires :

pytest -v -s


Vérifier le style du code :

flake8 src tests

6. Fonctionnalités

Génération aléatoire de mesures par capteurs.

Détection d’anomalies via des seuils prédéfinis.

Stockage des données dans MongoDB.

Structure POO modulable pour ajouter facilement de nouveaux capteurs.

Tests unitaires pour chaque composant.

Vérification automatique du style du code avec flake8.

7. Auteur

Nom : zemmouche nora

Email : nzemouche@yahoo.com