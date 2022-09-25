from fastapi import APIRouter, status, HTTPException, Depends, Body, Query
from db.db import get_db
from sqlalchemy.orm import Session

from .services import get, create
from .schemas import BalanceCreate, BalanceRead

router = APIRouter()

@router.get(
    "",
    name="balance:get-balance-from-current-user",
    status_code=status.HTTP_200_OK,
    response_model=BalanceRead,
)
async def get_balance_from_current_user(
    db_session: Session = Depends(get_db), 
    user_id: int = Query(...),
):
    return get(db_session=db_session, user_id=user_id)


@router.post(
    "",
    name="balance:create-balance",
    status_code=status.HTTP_201_CREATED,
)
async def create_balance(
    db_session: Session = Depends(get_db),
    balance_in: BalanceCreate = Body(...),
):
    return create(db_session=db_session, balance_in=balance_in)
