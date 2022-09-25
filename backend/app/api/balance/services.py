from fastapi import HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session
from .schemas import BalanceCreate, TransactionCreate
from db.models.balance import Balance, Transaction


def get_balance(*, db_session: Session, user_id: int) -> Balance:

    balance = db_session.query(Balance).filter(Balance.user_id==user_id).order_by(desc('created_at')).first()

    return balance


def create_balance(*, db_session: Session, balance_in: BalanceCreate) -> Balance:

    balance = Balance(**balance_in.dict())

    db_session.add(balance)
    db_session.commit()

    return balance
    

def get_transactions(*, db_session: Session, user_id: int):

    transactions = db_session.query(Transaction).filter(Transaction.user_id==user_id).all()
    if not transactions:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User has no transactions.")
        
    return transactions


def create_transaction(*, db_session: Session, transaction_in: TransactionCreate) -> Transaction:

    transaction = Transaction(**transaction_in.dict())

    db_session.add(transaction)
    db_session.flush()

    users_balance = get_balance(db_session=db_session, user_id=transaction.user_id)
    users_balance.quantity += transaction.quantity

    db_session.commit()

