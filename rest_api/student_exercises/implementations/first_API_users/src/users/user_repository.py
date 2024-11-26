"""
Repository for User using firebase database
"""
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.firestore_database import db, DocumentReference, DocumentSnapshot
from utils.exceptions import UserNotFound, UserNotComplete

from .user import User

class UserRepository():
  def __init__(self):
    self.collection = db.collection('users')
  
  def get_all(self) -> list[User]:
    users: list[User] = []
    for user in self.collection.get():
      user_data: dict = user.to_dict()
      user_data.update({"id": user.id})
      u: User = User.from_dict(user_data)
      # u.id = user.id
      users.append(u)
    return users
  
  def get_one(self, id: str) -> User:
    user_query: DocumentSnapshot = self.collection.document(id).get()

    if not user_query.exists:
      raise UserNotFound(f"User with id {id} not found")
    
    return User.from_dict(user_query.to_dict() | {"id": id})
  
  
  def add_user(self, user: User) -> User:
    """
    Insert a user in the database
    Note that, the received user in parameters doesn't have an id
    The id should be added to the retunred user after the creation in the database
    This function should check that the user is fully complete (no class attributes with "")

    Args:
        user (User): The user to add in database (without id)
    
    Returns:
        User: The user with the id added
    """
    # if (
    #   user.username == "" 
    #   or user.firstname == "" 
    #   or user.lastname == "" 
    #   or user.password == "" 
    #   or user.salt == ""
    # ):
    #   raise ValueError("User is not complete")

    user_dict: dict[str, str] = user.to_dict(with_id=False)
    for k, v in user_dict.items():
      if v == "":
        raise UserNotComplete(f"attribute {k} for user is missing")
    # if "" in user_dict.values():
    #   raise UserNotComplete()

        

    _, doc_ref = self.collection.add(user_dict)
    # created_user: dict = {"id": doc_ref.id, **doc_ref.get().to_dict()}
    # created_user: dict = {"id": doc_ref.id} | doc_ref.get().to_dict()
    user.id = doc_ref.id
    return user

  def update_user(self, user: User) -> User:
    """
    Update a user in the database, the user in parameters contains the id
    The user in parameters has some values set to "" these bvalues are not to be udpated

    Args:
        user (User): The user to update in database

    Raises:
        ValueError: If the user doesn't exist

    Returns:
        User: The user updated
    """
    if user.id == "":
      raise ValueError("user should have an id to be updated")
    
    new_user_dict: dict = {}
    for k, v in user.to_dict(with_id=False).items():
      if v == "":
        continue
      new_user_dict[k] = v
    
    self.collection.document(user.id).update(new_user_dict)
    # user.to_dict().update(new_user_dict)
    # return User.from_dict(user.to_dict())
    return self.get_one(user.id)

  def delete_user(self, id: str) -> None:
    self.collection.document(id).delete()

  def get_user_by_username(self, username: str) -> User:
    result: list[DocumentSnapshot] = self.collection.where("username", "==", username).get()
    if len(result) != 1:
      raise UserNotFound(f"user with username '{username}' doesn't exists")
    
    return User.from_dict(result[0].to_dict() | {"id": result[0].id})
