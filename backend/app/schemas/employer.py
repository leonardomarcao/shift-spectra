from typing import Optional

from pydantic import BaseModel


class EmployerBase(BaseModel):
    identifier: int


class EmployerCreate(EmployerBase):
    name: str


class EmployerUpdate(EmployerBase):
    name: Optional[str]


class EmployerInDBBase(EmployerBase):
    identifier: int
    name: str

    class Config:
        orm_mode = True


class Employer(EmployerInDBBase):
    pass


class EmployerInDB(EmployerInDBBase):
    pass
