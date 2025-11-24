import pytest
from pydantic import ValidationError
from app.schemas import CalculationCreate

def test_valid_add():
    c = CalculationCreate(a=2,b=3,type="add")
    assert c.type == "add"

def test_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(a=1,b=2,type="wrong")

def test_div_zero_error():
    with pytest.raises(ValidationError):
        CalculationCreate(a=5,b=0,type="div")
