from starlette.testclient import TestClient
#import pandas as pd
#from fastapi import FastAPI, HTTPException
#import joblib

#import sys
#sys.path.append("..")

# charger les données
# df_sample = pd.read_csv('api_prediction/df_sample.csv')
#  # définir SK_ID_CUR en index
# df_sample = df_sample.set_index('SK_ID_CURR')
# # charger le scaler
# scaler = joblib.load('../api_prediction/scaler.pkl')
# # charger le modele
# modele_retenu = joblib.load('../api_prediction/modele_retenu.pkl')
# # récupérer le meilleur seuil retenu
# meilleur_seuil_value = 0.5050505050505051


from .fonction_api_prediction import app

client = TestClient(app)

def test_prediction_du_client_127494():
  response = client.get("/predict/127494")
  assert response.status_code == 200
  response_data = response.json()
  # arrondir la probabilité à 8 decimales
  response_data["probability"] = round(response_data["probability"], 8)
  # comparer avec la valeur attendue également arrondie à 8 décimales
  assert response_data == {
           "client_id": 127494,
           "prediction": 0,
           "probability": round(0.08933094542391484, 8)
       }


def test_client_inconnu_326316():
  response = client.get("/predict/326316")
  assert response.status_code == 404

