from sqlalchemy import Column, Integer, ForeignKey
from db.db import Base

from .core import CoreBaseModel
from sqlalchemy.orm import relationship

class Balance(CoreBaseModel, Base):

    __tablename__ = "balance"

    quantity = Column(Integer, nullable=False)
    
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")