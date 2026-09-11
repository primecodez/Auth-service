from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from utils.security import hash_password

def create_user(db, username, email, password):
    hashed_password = hash_password(password)

    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_id(
    db: Session,
    user_id: int,
) -> User | None:

    statement = select(User).where(User.id == user_id)

    return db.scalars(statement).first()


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:

    statement = select(User).where(User.email == email)

    return db.scalars(statement).first()


def get_users(
    db: Session,
) -> list[User]:

    statement = select(User)

    return list(db.scalars(statement).all())


def update_user(
    db: Session,
    user_id: int,
    username: str | None = None,
    email: str | None = None,
    hashed_password: str | None = None,
) -> User | None:

    statement = select(User).where(User.id == user_id)
    user = db.scalars(statement).first()

    if user is None:
        return None

    if username is not None:
        user.username = username

    if email is not None:
        user.email = email

    if hashed_password is not None:
        user.hashed_password = hashed_password

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int,
) -> bool:

    statement = select(User).where(User.id == user_id)
    user = db.scalars(statement).first()

    if user is None:
        return False

    db.delete(user)
    db.commit()

    return True