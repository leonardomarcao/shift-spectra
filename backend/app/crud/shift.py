import calendar
from typing import Optional

from app.crud.crud_base import CRUDBase
from app.helpers import compute_10_minute_intervals
from app.models.shift import Shift
from app.schemas.shift import ShiftCreate, ShiftUpdate
from sqlalchemy import extract, func
from sqlalchemy.orm import Session, joinedload


class CRUDShift(CRUDBase[Shift, ShiftCreate, ShiftUpdate]):
    def get_by_identifier(self, db: Session, *, identifier: int) -> Optional[Shift]:
        return db.query(Shift).filter(Shift.identifier == identifier).first()

    def get_group_by_month(self, db: Session) -> list:
        month_year_data = (
            db.query(
                extract('year', Shift.start_shift).label('year'),
                extract('month', Shift.start_shift).label('month'),
                func.count(Shift.id).label('total_records'),
            )
            .group_by(extract('year', Shift.start_shift), extract('month', Shift.start_shift))
            .order_by(extract('year', Shift.start_shift), extract('month', Shift.start_shift))
            .all()
        )

        result = [
            {"year": record.year, "month": record.month, "total_records": record.total_records}
            for record in month_year_data
        ]

        return result

    def get_by_month_range(self, db: Session, year: int, month: int) -> list:
        shifts = (
            db.query(Shift)
            .filter(extract('month', Shift.start_shift) == month)
            .filter(extract('year', Shift.start_shift) == year)
            .options(joinedload(Shift.employer))
            .order_by(Shift.start_shift)
            .all()
        )
        return shifts

    def get_shift_graph(self, db: Session, year: int, month: int, day: int) -> list:
        # Get shifts for the given day
        shifts_for_day = (
            db.query(Shift)
            .filter(extract('year', Shift.start_shift) == year)
            .filter(extract('month', Shift.start_shift) == month)
            .filter(extract('day', Shift.start_shift) == day)
            .all()
        )

        # Compute the counts for each 10-minute interval
        data = compute_10_minute_intervals(shifts_for_day)
        return data


crud_shift = CRUDShift(Shift)
