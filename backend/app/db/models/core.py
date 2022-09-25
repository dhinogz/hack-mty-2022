from datetime import datetime

from sqlalchemy import Integer, Column, DateTime, Boolean
from sqlalchemy.sql import func

from db.db import Base


class IDMixin(object):
    id = Column(Integer, primary_key=True, autoincrement=True)


class TimeStampMixin(object):

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    is_active = Column(Boolean, unique=False, default=True)


class CoreBaseModel(IDMixin, TimeStampMixin):
    pass