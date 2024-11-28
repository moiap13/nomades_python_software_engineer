import os
CURR_DIR = os.path.dirname(__file__)

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.firestore import DocumentReference, DocumentSnapshot

cred = credentials.Certificate(os.path.join(CURR_DIR, 'pse_2024_1112.json'))
firebase_admin.initialize_app(cred)

db = firestore.client()
