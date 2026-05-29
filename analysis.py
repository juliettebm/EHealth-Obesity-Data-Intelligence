import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# =============================================================================
# EXERCICE 6 : CHARGEMENT ET NETTOYAGE FORCÉ DES DONNÉES
# =============================================================================
chemin = "F:\SQL exo\Obesity-Data-Analysis\Data\obesity_clean.csv"
df = pd.read_csv(chemin, sep="\t")

# --- Logique de nettoyage : On force le remplacement des "," par des "." ---
# On applique cela sur toutes les colonnes numériques qui nous servent dans le script
for col in ['TUE', 'CH2O', 'Weight_kg', 'FAF']:
    # 1. On s'assure que la colonne est lue comme du texte pour pouvoir remplacer la virgule
    df[col] = df[col].astype(str).str.replace(',', '.')
    # 2. On transforme de force en vrai nombre (float). Les erreurs deviennent des NaN
    df[col] = pd.to_numeric(df[col], errors='coerce')

# On supprime les éventuelles lignes vides ou corrompues s'il y en a après conversion
df = df.dropna(subset=['TUE', 'CH2O', 'Weight_kg', 'FAF'])


# =============================================================================
# EXERCICE 7 : LOGIQUE MÉTIER
# Logique : Maintenant que TUE et CH2O sont de vrais floats (ex: 2.0), la 
# comparaison va fonctionner parfaitement !
# =============================================================================
def evaluate_behavioral_risk(row):
    screen_time = row['TUE']
    water_intake = row['CH2O']
    if screen_time > 2.0 and water_intake < 2.0:
        return "High Risk"
    elif screen_time > 2.0 or water_intake < 2.0:
        return "Moderate Risk"
    else:
        return "Balanced Profile"

df['Behavioral_Risk_Profile'] = df.apply(evaluate_behavioral_risk, axis=1)


# =============================================================================
# EXERCICE 10 : GRAPH DE CORRÉLATION (SCATTER PLOT)
# =============================================================================
plt.figure(figsize=(8, 5))

plt.scatter(df['FAF'], df['Weight_kg'], color='#3498db', alpha=0.5, edgecolor='none')

plt.title("Correlation Analysis: Physical Activity vs Weight", fontsize=13, fontweight='bold', pad=15)
plt.xlabel("Physical Activity Level (FAF)", fontsize=11)
plt.ylabel("Weight (kg)", fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()


# =============================================================================
# EXERCICE 11 : TEST STATISTIQUE DE RIGUEUR (T-TEST)
# =============================================================================
weight_balanced = df[df['Behavioral_Risk_Profile'] == 'Balanced Profile']['Weight_kg']
weight_moderate = df[df['Behavioral_Risk_Profile'] == 'Moderate Risk']['Weight_kg']

t_stat, p_value = stats.ttest_ind(weight_balanced, weight_moderate, equal_var=False)

print("\n=== EXERCISE 11 STATISTICAL TEST RESULTS ===")
print(f"Average Weight - Balanced Profile: {weight_balanced.mean():.2f} kg")
print(f"Average Weight - Moderate Risk: {weight_moderate.mean():.2f} kg")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("\n👉 Conclusion: The difference is STATISTICALLY SIGNIFICANT (p < 0.05).")
    print("The behavioral risk profile genuinely impacts weight. It is NOT due to random chance.")
else:
    print("\n👉 Conclusion: The difference is NOT statistically significant (p >= 0.05).")
    print("The observed trend could be purely due to random chance.")