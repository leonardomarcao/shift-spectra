from app.db.base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Employer(Base):
    __tablename__ = "employer"
    identifier = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    active = Column(Boolean, default=True)
    shifts = relationship("Shift", back_populates="employer")
