from fastapi import HTTPException, status
from .schemas import UserRead, UserCreate
from sqlalchemy.orm import Session
from db.models.auth import User




def get(*, db_session: Session, email: str):

    user = db_session.query(User).where(User.email==email).one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with that email does not exist.")

    return user


def create(*, db_session: Session, user_in: UserCreate):

    if db_session.query(User).where(User.email==user_in.email).one_or_none():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A user with that email already exists.")
    
    user = User(**user_in.dict())
    
    db_session.add(user)
    db_session.commit()

    return user


def login(*, db_session: Session, user_in: UserCreate):

    user = db_session.query(User).where(User.email==user_in.email).one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that email does not exist."
        )
    if user.password != user_in.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unsuccesful login" 
        )
    return user