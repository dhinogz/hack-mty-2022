from core.schemas import CoreModel
from api.balance.schemas import BalanceInUserRead


class UserBase(CoreModel):

    email: str

class UserRead(UserBase):

    id: int
    name: str
    parent_name: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):

    password: str
    name: str
    parent_name: str