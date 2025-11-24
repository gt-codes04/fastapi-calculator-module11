import pytest
from app.services.calculation_factory import CalculationFactory

def test_add():
    assert CalculationFactory.create("add").compute(2,3) == 5

def test_sub():
    assert CalculationFactory.create("sub").compute(5,2) == 3

def test_mul():
    assert CalculationFactory.create("mul").compute(2,4) == 8

def test_div():
    assert CalculationFactory.create("div").compute(10,2) == 5

def test_invalid_type():
    with pytest.raises(ValueError):
        CalculationFactory.create("random")

def test_div_zero():
    div = CalculationFactory.create("div")
    with pytest.raises(ValueError):
        div.compute(10,0)
