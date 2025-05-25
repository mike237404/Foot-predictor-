import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Prédicteur Premier League", layout="wide")
st.title("⚽ Prédiction de Matchs - Premier League")

# Exemple de données historiques simplifiées
data = pd.DataFrame({
    'home_team': ['Arsenal', 'Chelsea', 'Liverpool', 'Man City'],
    'away_team': ['Tottenham', 'Man Utd', 'Leeds', 'Everton'],
    'home_odds': [1.8, 2.1, 1.7, 1.5],
    'draw_odds': [3.5, 3.3, 3.2, 3.0],
    'away_odds': [4.2, 3.0, 5.0, 6.0],
    'result': ['H', 'D', 'H', 'H']  # H=Home win, D=Draw, A=Away win
})

# Traitement des données
X = data[['home_odds', 'draw_odds', 'away_odds']]
y = data['result']
model = RandomForestClassifier()
model.fit(X, y)

st.subheader("Entrez les cotes du prochain match :")

home_team = st.text_input("Équipe à domicile", value="Arsenal")
away_team = st.text_input("Équipe à l'extérieur", value="Chelsea")
home_odds = st.number_input("Cote Victoire Domicile", value=1.8)
draw_odds = st.number_input("Cote Match Nul", value=3.4)
away_odds = st.number_input("Cote Victoire Extérieur", value=4.2)

if st.button("Prédire le résultat"):
    input_data = np.array([[home_odds, draw_odds, away_odds]])
    prediction = model.predict(input_data)[0]
    st.success(f"Résultat Prédit : **{prediction}**")
