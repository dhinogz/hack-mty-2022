from core.schemas import CoreModel


class BalanceBase(CoreModel):

    quantity: int

class BalanceRead(BalanceBase):
    user_id: int # TODO: Poner user schema aqui
    id: int

    class Config:
        orm_mode = True

class BalanceInUserRead(BalanceBase):
    
    class Config:
        orm_mode = True

class BalanceCreate(BalanceBase):
    user_id: int
