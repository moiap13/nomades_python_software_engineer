import os
CURR_DIR = os.path.dirname(__file__)

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('/etc/secrets/pse_2025_0103-creds.json')
firebase_admin.initialize_app(cred)

db = firestore.client()