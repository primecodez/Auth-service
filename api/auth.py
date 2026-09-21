from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.routers.user import router
from app.schemas.user import UserLogin 
from app.database.session import get_db
from app.crud import user as crud
from utils.security import verify_password, create_access_token

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
    
    if not verify_password(login.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }