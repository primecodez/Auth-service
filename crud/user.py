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
    

"""crud/user.py

create_user()      ✅
get_user_by_id()   ⬜ ← NEXT
get_user_by_email()⬜
get_users()        ⬜
update_user()      ⬜
delete_user()      ⬜
"""