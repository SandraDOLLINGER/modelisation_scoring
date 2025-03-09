import pandas as pd
from fastapi import FastAPI, HTTPException
import joblib

# Créer l'application FastAPI
app = FastAPI()

# charger les données
#df_cleaned = pd.read_csv('df_cleaned.csv')
# définir SK_ID_CUR en index
#df_cleaned = df_cleaned.set_index('SK_ID_CURR')
# charger le scaler
#scaler = joblib.load('scaler.pkl')
# charger le modele
#modele_retenu = joblib.load('modele_retenu.pkl')
# récupérer le meilleur seuil retenu
#meilleur_seuil_value = 0.5050505050505051


# @app.get("/")
# def read_root():
#     return {"message": "Bienvenue sur l'API de prédiction Prêt à dépenser"}

@app.get("/test")
def test_route():
    return{"message": "hello world"}

# @app.get("/predict/{client_id}")
# async def predict(client_id: int):
#     """
#         Fonction de prédiction pour un client spécifique basé sur son ID.
#     param :
#         client_id : identifiant du client pour lequel faire la prédiction
#     return :
#         client_proba : probabilité de la classe positive
#         client_pred : prédiction binaire (0 ou 1)
#     """
#     # Vérifier si l'ID client existe dans le DataFrame
#     if client_id in df_cleaned.index:
#         # Sélectionner les données du client
#         X_client = df_cleaned.loc[client_id]
#         # Supprimer la colonne TARGET si elle est présente
#         if 'TARGET' in X_client.index:
#             X_client = X_client.drop('TARGET')
#         # Préparer les données (reshape et normalisation)
#         X_client = X_client.values.reshape(1, -1)  # Pour adapter à l'entrée du modèle
#         X_client_scaled = scaler.transform(X_client)

#         # Prédiction des probabilités et de la classe
#         client_proba = modele_retenu.predict_proba(X_client_scaled)[:, 1]
#         client_pred = (client_proba >= meilleur_seuil_value).astype(int)
    
#         return {
#             "client_id": client_id,
#             "prediction": int(client_pred[0]),  # classe prédite (0 ou 1)
#             "probability": float(client_proba[0])  # probabilité de la classe positive
#         }

#     else:
#         raise HTTPException(status_code=404, detail="Client ID not found")