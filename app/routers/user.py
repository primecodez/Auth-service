from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate

from app.database.session import get_db
from app.crud import user as crud

router = APIRouter(prefix = "/users",tags=["Users"])

@router.post("")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return crud.create_user(db, user)

@router.get("/{user_id}")
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud.get_user_by_id(db, user_id)

@router.get("")
def get_users(
    db: Session = Depends(get_db),
):
    return crud.get_users(db)

@router.put("/{user_id}")
def update_user(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return crud.update_user(db, user_id, user)

@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud.delete_user(db, user_id)

"""POST   /users          → create_user()
GET    /users/{id}     → get_user_by_id()
GET    /users          → get_users()
PUT    /users/{id}     → update_user()
DELETE /users/{id}     → delete_user()"""

