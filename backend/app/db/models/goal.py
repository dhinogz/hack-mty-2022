from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from db.db import Base

from .core import CoreBaseModel
from sqlalchemy.orm import relationship

class Goal(CoreBaseModel, Base):

    __tablename__ = "goal"

    name = Column(String)
    quantity = Column(Integer)
    status = Column(Boolean)
    
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")

