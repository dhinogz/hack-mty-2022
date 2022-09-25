from datetime import datetime

from sqlalchemy import Integer, Column, DateTime, Boolean

from db.db import Base


class IDMixin(object):
    id = Column(Integer, primary_key=True)


class TimeStampMixin(object):

    created_at = Column(
        DateTime,
        server_default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        server_default=datetime.utcnow,
        nullable=False,
    )

    active = Column(
        Boolean,
        server_default=True,
        # default=True,
        nullable=False,
    )


class CoreBaseModel(IDMixin, TimeStampMixin, Base):
    pass