from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)   # shortened url slug
    secret_key = Column(String, unique=True, index=True)    # metadata view
    target_url = Column(String, index=True)     # redirect url
    is_active = Column(Boolean, default=True)   # allow deactivation of old urls
    clicks = Column(Integer, default=0)         # keep track of usage, might add ip storage later