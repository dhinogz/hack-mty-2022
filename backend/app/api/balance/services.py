from fastapi import HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session
from .schemas import BalanceRead, BalanceCreate
from db.models.balance import Balance


def get(*, db_session: Session, user_id: int) -> Balance:

    balance = db_session.query(Balance).filter(Balance.user_id==user_id).order_by(desc('created_at')).first()

    return balance


def create(*, db_session: Session, balance_in: BalanceCreate) -> Balance:

    balance = Balance(**balance_in.dict())

    db_session.add(balance)
    db_session.commit()

    return balance
    

"""
Balance: {
    "quantit"
}

"""
