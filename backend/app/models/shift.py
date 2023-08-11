from datetime import datetime

from app.db.base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class ImportShiftReference(Base):
    __tablename__ = "import_shift"
    id = Column(Integer, primary_key=True, index=True)
    file = Column(String(255), nullable=False)
    import_date = Column(DateTime, nullable=False, index=True, default=datetime.utcnow)


class Shift(Base):
    __tablename__ = "shift"
    id = Column(Integer, primary_key=True, index=True)
    employer_id = Column(Integer, ForeignKey("employer.identifier"), nullable=False)
    employer = relationship("Employer", back_populates="shifts")
    start_shift = Column(DateTime, nullable=False)
    end_shift = Column(DateTime, nullable=False)
    start_lunch = Column(DateTime, nullable=False)
    end_lunch = Column(DateTime, nullable=False)
    import_shift_id = Column(Integer, ForeignKey("import_shift.id"), nullable=False)
    import_shift = relationship("ImportShiftReference", viewonly=True)
