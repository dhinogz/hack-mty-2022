from typing import List
from fastapi import APIRouter, status, HTTPException, Depends, Body, Query
from db.db import get_db
from sqlalchemy.orm import Session

from .services import get_goals, create_goal
from .schemas import GoalCreate, GoalRead

router = APIRouter()

@router.get(
    "",
    name="goal:get-goals-from-current-user",
    status_code=status.HTTP_200_OK,
    response_model=List[GoalRead],
)
async def get_list_of_goals(
    *,
    db_session: Session = Depends(get_db),
    user_id: int = Query(...),
):

    return get_goals(db_session=db_session, user_id=user_id)


@router.post(
    "",
    name="goal:create-goal",
    status_code=status.HTTP_201_CREATED,
    response_model=GoalRead,
)
async def register_goal(
    *, db_session: Session = Depends(get_db), goal_in: GoalCreate = Body(...)
):
  
    return create_goal(db_session=db_session, goal_in=goal_in)


