import random
from datetime import datetime
from firebase_admin.firestore import DocumentReference

from faker import Faker
from config.firestore_db import db

fake = Faker()

users_ids: list[str] = [user.id for user in db.collection(u"users").get()]

def random_timestamp(start_date: datetime) -> str:
  end_date: datetime = datetime.now()
  random_date = start_date + (end_date - start_date) * random.random()
  return random_date.isoformat()

posts: list[dict[str, str | list[DocumentReference]]] = []

for _ in range(20):
  post: dict[str, str | list[DocumentReference]] = {
    "title": fake.sentence(),
    "body": fake.paragraph(nb_sentences=5),
    "created_at": random_timestamp(datetime(2025, 2, 17)),
    "authors": [db.document(f'users/{user_id}') for user_id in random.sample(users_ids, random.randint(1, len(users_ids)))]
  }
  db.collection("random_posts").add(post)
