from core.schemas import CoreModel


class GoalBase(CoreModel):

    name: str
    quantity: int
    status: bool


class GoalRead(GoalBase):

    user_id: int

    class Config:
        orm_mode = True


class GoalCreate(GoalBase):

    user_id: int