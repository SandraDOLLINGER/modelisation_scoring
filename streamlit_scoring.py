import streamlit as st
import requests

# URL de ton API FastAPI
API_URL = "http://127.0.0.1:8000/predict"

# Interface Streamlit
st.title("Prédiction du score de crédit")

# Saisie du numéro de client
client_id = st.text_input("Entrez le numéro client :")

# Fonction pour récupérer la prédiction de l'API FastAPI
def get_prediction(client_id):
    try:
        # Faire une requête GET à l'API
        response = requests.get(f"{API_URL}/{client_id}")
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 404:
            st.error("Client non trouvé, renseignez un numéro client")
            return None
        else:
            st.error("Erreur dans la requête à l'API")
            return None
    except Exception as e:
        st.error(f"Erreur : {e}")
        return None

if client_id:
    # vérifier si le client_id est valide
    if not client_id.isdigit():
        st.error("Le numéro client doit être un nombre entier, renseignez un numéro de client")
    elif len(client_id) != 6:
        st.error("Le numéro client doit avoir exactement 6 chiffres, renseignez un numéro de client")
    else:
        # convertir en entier
        client_id_int = int(client_id)    
        # Appeler la fonction pour obtenir la prédiction
        result = get_prediction(client_id_int)
    
        if result is not None:
            prediction_classe = result["prediction"]
            probability = result["probability"]

            st.write(f"### Client {client_id}")
            st.write(f'Prédiction : {prediction_classe}')
            st.write(f"**Prédiction :** {'Refusé' if prediction_classe == 1 else 'Accepté'}")
            st.write(f"**Probabilité de refus :** {probability:.2%}")

            # Affichage de la barre de progression en fonction de la probabilité
            st.progress(probability)
else:
    st.write("Veuillez entrer un numéro de client.")
