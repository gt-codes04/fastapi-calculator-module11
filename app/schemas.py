from pydantic import BaseModel, validator, root_validator
from typing import Optional, Set


class CalculationBase(BaseModel):
    a: float
    b: float
    type: str

    @validator("type")
    def validate_type(cls, v):
        allowed: Set[str] = {"add", "sub", "mul", "div"}
        if v.lower() not in allowed:
            raise ValueError(f"type must be one of {allowed}")
        return v.lower()


class CalculationCreate(CalculationBase):

    @root_validator
    def check_division(cls, values):
        type_ = values.get("type")
        b = values.get("b")

        if type_ == "div" and b == 0:
            raise ValueError("b cannot be zero for division")

        return values


class CalculationRead(CalculationBase):
    id: int
    result: Optional[float] = None
    user_id: Optional[int] = None

    class Config:
        orm_mode = True
