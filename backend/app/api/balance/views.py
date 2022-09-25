from typing import List
from fastapi import APIRouter, status, HTTPException, Depends, Body, Query
from db.db import get_db
from sqlalchemy.orm import Session

from .services import get_balance, create_balance, get_transactions, create_transaction
from .schemas import BalanceCreate, BalanceRead, TransactionRead, TransactionCreate

balance_router = APIRouter()

@balance_router.get(
    "",
    name="balance:get-balance-from-current-user",
    status_code=status.HTTP_200_OK,
    response_model=BalanceRead,
)
async def get_balance_from_current_user(
    db_session: Session = Depends(get_db), 
    user_id: int = Query(...),
):
    return get_balance(db_session=db_session, user_id=user_id)


@balance_router.post(
    "",
    name="balance:create-balance",
    status_code=status.HTTP_201_CREATED,
)
async def register_balance(
    db_session: Session = Depends(get_db),
    balance_in: BalanceCreate = Body(...),
):
    return create_balance(db_session=db_session, balance_in=balance_in)


transaction_router = APIRouter()


@transaction_router.get(
    "",
    name="transaction:get-transactions",
    status_code=status.HTTP_200_OK,
    response_model=List[TransactionRead]
)
async def get_transactions_list_from_user(*, db_session: Session = Depends(get_db), user_id: int = Query(...)):

    return get_transactions(db_session=db_session, user_id=user_id)

@transaction_router.post(
    "",
    name="transaction:create-transaction",
    status_code=status.HTTP_201_CREATED,
)
async def register_balance(
    db_session: Session = Depends(get_db),
    balance_in: TransactionCreate = Body(...),
):
    return create_transaction(db_session=db_session, balance_in=balance_in)
