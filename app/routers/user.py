from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate

from app.database.session import get_db
from app.crud import user as crud

router = APIRouter()

@router.get("/users/{user_id}")
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud.get_user_by_id(db, user_id)


"""POST   /users          → create_user()
GET    /users/{id}     → get_user_by_id()
GET    /users          → get_users()
PUT    /users/{id}     → update_user()
DELETE /users/{id}     → delete_user()"""

@router.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return crud.create_user(db, user)