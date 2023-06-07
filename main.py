from fastapi import FastAPI
from typing import List
from models import Vehicle, Owner, Bill

app = FastAPI()

# Exemple de données de la flotte d'assurance 
vehicles = [
    Vehicle(immatriculation="BF 6874", categorie="voiture", proprietaire="Sœur Marie", cotation_assurance=100.0),
    Vehicle(immatriculation="BG 2016", categorie="moto", proprietaire="Sœur Louise", cotation_assurance=150.0),
    Vehicle(immatriculation="BU 6798", categorie="voiture", proprietaire="Communauté Sainte Claire", cotation_assurance=200.0),
    # ...
]

owners = [
    Owner(nom="Sœur Marie"),
    Owner(nom="Sœur Louise"),
    Owner(nom="Communauté Sainte Claire"),
    # ...
]

@app.get("/category/{category}")
async def get_vehicles_by_category(category: str) -> List[Vehicle]:
    # Filtrer les véhicules par catégorie
    filtered_vehicles = [v for v in vehicles if v.categorie == category]
    return filtered_vehicles

@app.get("/owner/{owner}")
async def get_vehicles_by_owner(owner: str) -> List[Vehicle]:
    # Filtrer les véhicules par propriétaire
    filtered_vehicles = [v for v in vehicles if v.proprietaire == owner]
    return filtered_vehicles

@app.get("/bills/{owner}")
async def generate_bill_for_owner(owner: str) -> Bill:
    # Filtrer les engins par propriétaire
    owner_vehicles = [v for v in vehicles if v.proprietaire == owner]

    # Calculer les totaux
    total_cotation = sum(v.cotation_assurance for v in owner_vehicles)
    total_majoration = total_cotation * 0.1  # Exemple de majoration de 10%
    montant_total_facture = total_cotation + total_majoration

    # Créer l'objet Bill
    bill = Bill(
        proprietaire=Owner(nom=owner),
        engins=owner_vehicles,
        total_cotation_assurance=total_cotation,
        total_majoration=total_majoration,
        montant_total_facture=montant_total_facture
    )
    return bill
