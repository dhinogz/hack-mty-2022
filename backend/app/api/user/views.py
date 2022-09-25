
from fastapi import APIRouter, Depends, Query
from .schemas import UserRead, UserCreate

from db.db import get_db
from sqlalchemy.orm import Session

from .services import get, create

router = APIRouter()

@router.get(
    "",
    name="user:get-user-by-email",
    response_model=UserRead,
)
async def get_user_by_email(
    *, db_session: Session = Depends(get_db), email: str = Query(...),
):

    return get(db_session=db_session, email=email)

@router.post(
    "",
    name="user:create-user",
    response_model=UserRead,
)
async def create_user(
    *, db_session: Session = Depends(get_db), user_in: UserCreate
):
    return create(db_session=db_session, user_in=user_in)

