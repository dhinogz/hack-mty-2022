from sqlalchemy import Column, Integer, String, ForeignKey


from .core import CoreBaseModel


class Auth(CoreBaseModel):
    """Auth database model linking to different profiles"""
    __tablename__ = "auth"

    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)

class Child(CoreBaseModel):
    """Child user profile"""

    __tablename__ = "child"

    name = Column(String, nullable=False)
    birthday = Column(Integer, nullable=False)

    auth_id = Column(Integer, ForeignKey("auth.id"))
    father_id = Column(Integer, ForeignKey("parent.id"))
    mother_id = Column(Integer, ForeignKey("parent.id"))


class ParentsChildren(CoreBaseModel):

    __tablename__ = "parents_child"

    child_id = Column(Integer, ForeignKey("child.id"))
    parent_id = Column(Integer, ForeignKey("parent.id"))


class Parent(CoreBaseModel):
    """Parent user profile"""
    __tablename__ = "parent"

    name = Column(String, nullable=False)
    auth_id = Column(Integer, ForeignKey("auth.id"))

    