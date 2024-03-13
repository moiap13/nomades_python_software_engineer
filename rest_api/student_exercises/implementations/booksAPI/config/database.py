import os
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(f"{os.path.dirname(os.path.realpath(__file__))}/books-cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
