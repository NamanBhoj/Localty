# data models

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base
from datetime import datetime 


class Transaction_Record(Base):
    __tablename__ = "transaction_record"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    amount = Column(Float)
    category = Column(String)
    timestamp = Column(DateTime)

class Loyalty_Record(Base):
    __tablename__ = "loyalty_record"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    points = Column(Float)


