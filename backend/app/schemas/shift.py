from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ShiftBase(BaseModel):
    identifier: int
    start_shift: datetime
    end_shift: datetime
    start_lunch: datetime
    end_lunch: datetime


class ShiftCreate(ShiftBase):
    pass


class ShiftUpdate(ShiftBase):
    pass


class ShiftInDBBase(ShiftBase):
    identifier: int
    start_shift: datetime
    end_shift: datetime
    start_lunch: datetime
    end_lunch: datetime

    class Config:
        orm_mode = True


class Shift(ShiftInDBBase):
    pass
