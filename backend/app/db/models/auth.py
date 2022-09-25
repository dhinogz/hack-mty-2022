from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.db import Base

from .core import CoreBaseModel



class User(CoreBaseModel, Base):
    """Auth database model linking to different profiles"""
    __tablename__ = "user"

    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    name = Column(String, nullable=False)
    parent_name = Column(String)

    # balance = relationship("Balance")

# class Child(CoreBaseModel, Base):
#     """Child user profile"""

#     __tablename__ = "child"

#     name = Column(String, nullable=False)
#     birthday = Column(Integer, nullable=False)

#     auth_id = Column(Integer, ForeignKey("user.id"))
#     parent_name = Column(String)


    