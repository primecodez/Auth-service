from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserUpdate
from app.database.session import get_db
from app.crud import user as crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return crud.create_user(
        db,
        user.username,
        user.email,
        user.password,
    )


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


@router.get("/email/{email}")
def get_user_by_email(
    email: str,
    db: Session = Depends(get_db),
):
    return crud.get_user_by_email(db, email)


@router.put("/{user_id}")
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    return crud.update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud.delete_user(db, user_id)