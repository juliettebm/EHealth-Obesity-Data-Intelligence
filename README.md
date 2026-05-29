# 🏥 E-Health Analytics: Tracking Obesity Levels and Digital Lifestyle Habits

## 📝 1. Project Overview & Context
* **Project Title:** E-Health Analytics: Tracking Obesity Levels and Digital Lifestyle Habits
* **Goal of the project:** Analyser l'impact du mode de vie, de l'utilisation des technologies (applications connectées, temps d'écran) et de l'alimentation sur l'Indice de Masse Corporelle (IMC) pour concevoir un modèle de médecine préventive.
* **Business Value:** Permettre aux acteurs de la santé numérique (applications de e-santé, mutuelles, prévoyance) d'identifier les profils d'utilisateurs à risque et de personnaliser les recommandations automatisées.
* **Stack Technique:** **SQL Server (SSMS)** (Ingénierie & Cleaning) ➡️ **Python (Pandas)** (Logique & Feature Engineering) ➡️ **R (Tidyverse)** (Statistiques avancées & Dataviz).

## 📁 2. Data Overview & Infrastructure
* **Source of the Data:** *Estimation of Obesity Levels Based on Eating Habits and Physical Condition* (UC Irvine Machine Learning Repository).
* **Data Size:** 2 111 profils de patients / 17 variables cliniques et comportementales.
* **Infrastructure Checklist:**
  - [x] Télécharger les données brutes.
  - [ ] Créer la base de données dédiée sur SQL Server.
  - [ ] Importer le fichier brut sous le nom de table `obesity_raw`.
  - [ ] Exécuter une requête de crash-test (`SELECT COUNT(*)`).

---

## 🔧 3. Data Engineering & Cleaning (Phase SQL Server)
### 🚀 Défis Techniques & Choix d'Ingénierie Réalisés

* **Sécurisation et Typage des Données :** Le dataset brut ayant été importé au format texte, chaque colonne numérique a été convertie de manière sécurisée en utilisant `TRY_CAST` pour éviter les plantages de requêtes en cas de données corrompues (les anomalies sont transformées en `NULL`).
* **Gestion médicale des âges (`FLOOR`) :** Pour coller à la réalité clinique, l'âge a été arrondi à l'entier inférieur. Un utilisateur de 24 ans et 11 mois conserve légalement ses 24 ans tant qu'il n'a pas fêté son anniversaire.
* **Calcul automatisé de l'IMC :** Implémentation de la formule mathématique officielle $Poids / Taille^2 via la fonction `POWER()`, arrondie à 1 décimale.
* **Classification OMS (`CASE WHEN`) :** Automatisation de la segmentation des utilisateurs selon les seuils officiels de l'OMS (`Underweight`, `Normal Weight`, `Overweight`, `Obesity`).
* **Persistance via une Vue (`ALTER VIEW`) :** L'intégralité du pipeline a été encapsulée dans une vue SQL (`v_obesity_cleaned`). Cela permet de figer la logique de nettoyage directement côté serveur, offrant un accès direct, propre et performant (2 111 lignes prêtes) pour nos futurs scripts Python ou R.
