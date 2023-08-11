from app.db.base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Shift(Base):
    __tablename__ = "shift"
    id = Column(Integer, primary_key=True, index=True)
    employer_id = Column(Integer, ForeignKey("employer.identifier"), nullable=False)
    employer = relationship("Employer", back_populates="shifts")
    start_shift = Column(DateTime, nullable=False)
    end_shift = Column(DateTime, nullable=False)
    start_lunch = Column(DateTime, nullable=False)
    end_lunch = Column(DateTime, nullable=False)
