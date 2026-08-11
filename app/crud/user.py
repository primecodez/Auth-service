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


def get_user_by_id(
    db: Session,
    user_id: int,
) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:

    return db.query(User).filter(User.email == email).first()

def get_users(
      db: Session,
) -> list[User]:

    return db.query(User).all()

def update_user(
    db: Session,
    user_id: int,
    username: str | None = None,
    email: str | None = None,
    hashed_password: str | None = None,
) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
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
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return False

    db.delete(user)
    db.commit()

    return True


    




