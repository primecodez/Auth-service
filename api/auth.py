from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.user import router
from app.schemas.user import UserLogin 
from app.database.session import get_db
from app.crud import user as crud

@router.post("/login")
def login(
    login: UserLogin,
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, login.email)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )