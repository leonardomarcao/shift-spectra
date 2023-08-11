from typing import Optional

from app.crud.crud_base import CRUDBase
from app.models.employer import Employer
from app.schemas.employer import EmployerCreate, EmployerUpdate
from sqlalchemy.orm import Session


class CRUDEmployer(CRUDBase[Employer, EmployerCreate, EmployerUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Employer]:
        return db.query(Employer).filter(Employer.name == name).first()

    def get_by_identifier(self, db: Session, *, identifier: int) -> Optional[Employer]:
        return db.query(Employer).filter(Employer.identifier == identifier).first()


# Instantiate the CRUDEmployer for use
employer = CRUDEmployer(Employer)
