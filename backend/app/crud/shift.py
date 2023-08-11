from datetime import datetime
from typing import Optional

from app.crud.crud_base import CRUDBase
from app.helpers import compute_10_minute_intervals
from app.models.shift import ImportShiftReference, Shift
from app.schemas.shift import ImportShiftCreate, ImportShiftUpdate, ShiftCreate, ShiftUpdate
from sqlalchemy import extract, func
from sqlalchemy.orm import Session, joinedload


class CRUDShift(CRUDBase[Shift, ShiftCreate, ShiftUpdate]):
    def get_by_identifier(self, db: Session, *, identifier: int) -> Optional[Shift]:
        return db.query(Shift).filter(Shift.identifier == identifier).first()

    def get_group_by_month(self, db: Session) -> list:
        month_year_data = (
            db.query(
                extract("year", Shift.start_shift).label("year"),
                extract("month", Shift.start_shift).label("month"),
                func.count(Shift.id).label("records"),
                ImportShiftReference.file,
                ImportShiftReference.import_date,
            )
            .join(ImportShiftReference, Shift.import_shift_id == ImportShiftReference.id)
            .group_by(
                extract("year", Shift.start_shift),
                extract("month", Shift.start_shift),
                ImportShiftReference.file,
                ImportShiftReference.import_date,
            )
            .order_by(
                extract("year", Shift.start_shift),
                extract("month", Shift.start_shift),
                ImportShiftReference.import_date,
            )
            .all()
        )

        result = [
            {
                "year": record.year,
                "month": record.month,
                "records": record.records,
                "import_data": datetime.strftime(record.import_date, "%Y-%m-%d"),
                "import_time": datetime.strftime(record.import_date, "%H:%M:%S"),
                "import_file": record.file,
            }
            for record in month_year_data
        ]

        return result

    def get_by_month_range(self, db: Session, year: int, month: int) -> list:
        shifts = (
            db.query(Shift)
            .filter(extract("month", Shift.start_shift) == month)
            .filter(extract("year", Shift.start_shift) == year)
            .options(joinedload(Shift.employer), joinedload(Shift.import_shift))
            .order_by(Shift.start_shift)
            .all()
        )
        return shifts

    def get_shift_graph(self, db: Session, year: int, month: int, day: int) -> list:
        # Get shifts for the given day
        shifts_for_day = (
            db.query(Shift)
            .filter(extract("year", Shift.start_shift) == year)
            .filter(extract("month", Shift.start_shift) == month)
            .filter(extract("day", Shift.start_shift) == day)
            .all()
        )

        # Compute the counts for each 10-minute interval
        data = compute_10_minute_intervals(shifts_for_day)
        return data


class CRUDImportShiftReference(CRUDBase[ImportShiftReference, ImportShiftCreate, ImportShiftUpdate]):
    pass


crud_shift = CRUDShift(Shift)
crud_import_shift_reference = CRUDImportShiftReference(ImportShiftReference)
