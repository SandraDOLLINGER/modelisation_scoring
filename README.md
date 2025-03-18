# Implémentation d'un modèle de scoring de crédit
## Contexte
La société financière **"Prêt à dépenser"** propose des **crédits à la consommation** à des personnes ayant **peu ou pas d'historique de prêt**. Pour mieux évaluer le risque, ce projet vise à mettre en place une **API de scoring crédit** permettant de :

- Estimer la **probabilité** que le client présente des incidents de paiement.
- **Classifier** une demande de crédit en "acceptée" ou "refusée", selon un **seuil optimal** basé sur un modèle de prédiction entraîné sur des données déséquilibrées.

Une **interface utilisateur** a également été développée avec Streamlit pour faciliter l'interaction avec l'API. Le code correspondant est disponible dans le **repository GitHub "interface_streamlit"** (https://github.com/SandraDOLLINGER/interface_streamlit).

## Sélection du modèle
La démarche de modélisation comprend plusieurs étapes, comparant différents modèles et stratégies de **gestion du déséquilibre des classes** (92% de crédits remboursés sans incident de paiement vs. 8% de crédits ayant présenté des incidents de paiements) :

### Modèles testés :

- *Dummy Classifier* → utilisé comme baseline.
- *Régression Logistique* → modèle intermédiaire.
- *LightGBM* → modèle plus complexe.
### Optimisation et gestion du déséquilibre :

Tous les modèles ont été **optimisés avec une recherche d’hyperparamètres**.
Chacun a été testé avec et sans gestion du déséquilibre.
Les modèles intégrant la **gestion du déséquilibre** se sont révélés **plus performants**.
### Méthodes de gestion du déséquilibre :

- Au niveau des données :
    - Undersampling
    - Oversampling
    - SMOTETomek
    - SMOTEENN
- Au niveau des modèles :
    - class_weight="balanced" (Régression Logistique)
    - scale_pos_weight (LightGBM)
### Sélection finale du modèle :

Le LightGBM avec oversampling et num_leaves=50 offrait le score métier le plus bas (le score métier prend en compte le fait qu’un faux négatif – crédit accordé à un client qui fera défaut – coûte 10 fois plus qu’un faux positif – crédit refusé à tort).

Problème : Overfitting détecté
- AUC sur train : 0.84
- AUC sur test : 0.78

La différence significative indiquait un risque d’overfitting
### Choix final :
Un modèle plus simple, la **Régression Logistique avec class_weight="balanced"**, a été retenu car :
- Son score métier était légèrement supérieur mais restait **compétitif**.
- Il ne montrait **pas de signe d’overfitting** :

    - AUC sur train : 0.77
    - AUC sur test : 0.77
## Structure du projet
### API de prédiction

- fonction_api_prediction.py → Contient le code principal de l'API.
- df_sample.csv → Exemple de clients utilisés pour tester l’API.
- modele_retenu.pkl → Modèle final entraîné et sauvegardé.
- scaler.pkl → Standardisation des données pour la prédiction.
### Tests et validation

- test.py → Contient 2 tests unitaires :
    - Vérification de la prédiction pour un client connu (résultat attendu).
    - Vérification du retour 404 pour un client inconnu.
### Déploiement CI/CD

- .github/workflows/*.yaml → Contient le pipeline d’intégration continue.
- Procfile & requirements.txt → Fichiers nécessaires au déploiement sur Heroku.

Le fichier requirements.txt, présent dans le dossier du projet, liste l'ensemble des packages nécessaires au bon fonctionnement de l'API
### Modélisation & tracking

- notebook/ → Contient le notebook MLflow retraçant l'entraînement du modèle et l'analyse des performances.
## Utilisation de l'API
- Accès brut à l’API

L’API fonctionne en effectuant une requête GET avec un numéro de client :

    https://application-prediction-scoring-b81541cc2c3b.herokuapp.com/predict/numero_client

Le numéro de client est un identifiant à 6 chiffres.

- Utilisation via l’interface Streamlit

Une interface utilisateur a été développée avec Streamlit pour simplifier l'accès à l’API (https://interface-streamlit-f6c6cf4200cb.herokuapp.com/).

Dans cette interface, l’utilisateur peut saisir directement le numéro de client dans un champ prévu à cet effet.

Le code de l'interface est disponible dans un autre repository GitHub : https://github.com/SandraDOLLINGER/interface_streamlit

## Déploiement sur Heroku
L’API est déployée sur Heroku en utilisant :
- Un pipeline CI/CD via **GitHub Actions**.
- Un **Procfile** pour définir l’exécution de l’API.
- Un fichier **requirements.txt** listant les dépendances nécessaires.

*L’installation et le déploiement se font automatiquement après validation des tests unitaires*.