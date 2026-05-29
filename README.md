# 🏥 US Hospitals - Quality of Care Data Analysis

## 📌 Project Overview
L'objectif de ce projet est d'analyser la qualité des soins dans plus de 4 000 hôpitaux américains en utilisant **SQL Server (SSMS)**. Ce projet démontre des compétences en nettoyage de données, en gestion de types complexes et en agrégation statistique pour l'aide à la décision.

* **Source des données :** [Centers for Medicare & Medicaid Services (via Kaggle)](https://www.kaggle.com/)
* **Volume :** Plus de 120 000 lignes de données brutes.

---

## 🛠️ Technical Challenges & Data Cleaning
Le principal défi de ce dataset résidait dans la qualité des données brutes (Data Quality) :
* **Problématique des types :** Les colonnes `Score` et `Sample` (nombre de patients) étaient stockées au format `NVARCHAR` (Texte) en raison de la présence de valeurs manquantes textuelles (*"Not Available"*). Un `CAST` classique provoquait des erreurs d'exécution (*Arithmetic overflow*).
* **Solution implémentée :** Utilisation de la fonction avancée **`TRY_CAST(... AS FLOAT/INT)`**. Cela permet de forcer la conversion numérique des données valides tout en transformant automatiquement les anomalies textuelles en `NULL`, sécurisant ainsi l'exécution des requêtes.
* **Fiabilisation statistique :** Filtrage des données via un seuil métier (`Sample > 100`) pour exclure le bruit statistique des micro-établissements et garantir la pertinence des moyennes calculées.

---

## 🔍 Requêtes Clés & Analyses

### 1. Top 10 des hôpitaux les plus performants pour les AVC (`Stroke Care`)
Cette requête agrège les scores par établissement, applique le nettoyage des données en temps réel et trie les meilleurs hôpitaux ayant un volume d'activité représentatif.

```sql
SELECT TOP 10
    Hospital_Name,
    State,
    City,
    AVG(TRY_CAST(Score AS FLOAT)) AS ScoreMoyenAVC,
    SUM(TRY_CAST(Sample AS INT)) AS TotalPatientsEvalues
FROM 
    hospitals
WHERE 
    Condition LIKE '%Stroke_Care%'
    AND TRY_CAST(Sample AS INT) > 100 
GROUP BY 
    Hospital_Name, 
    State, 
    City
ORDER BY 
    ScoreMoyenAVC DESC;
