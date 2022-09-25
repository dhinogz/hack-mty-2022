from fastapi import HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session
from .schemas import GoalCreate, GoalCreate
from db.models.goal import Goal



def get_goals(db_session: Session, user_id: int):

    return db_session.query(Goal).filter(Goal.user_id==user_id).order_by(desc('created_at')).all()


def create_goal(db_session: Session, goal_in: GoalCreate):

    goal = Goal(**goal_in.dict())

    db_session.add(goal)
    db_session.commit()

    return goal