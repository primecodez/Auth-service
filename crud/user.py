from sqlalchemy.orm import Session

from app.models.user import User


def create_user(
    db: Session,
    username: str,
    email: str,
    hashed_password: str,
) -> User:
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user