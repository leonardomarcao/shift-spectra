from datetime import datetime
from typing import Any

from pydantic import BaseModel


class DefaultResponse(BaseModel):
    status: bool
    msg: str
    details: dict[Any, Any] | None = {}


class ShiftData(BaseModel):
    matricula: int
    data_marcacao: datetime
    hora_marcacao: datetime
