from pydantic import BaseModel
from typing import List

class Vehicle(BaseModel):
    immatriculation: str
    categorie: str
    proprietaire: str
    cotation_assurance: float

class Owner(BaseModel):
    nom: str

class Bill(BaseModel):
    proprietaire: Owner
    engins: List[Vehicle]
    total_cotation_assurance: float
    total_majoration: float
    montant_total_facture: float
