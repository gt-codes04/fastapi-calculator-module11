from sqlalchemy.orm import Session
import pytest

from app.schemas import CalculationCreate
from app.crud.calculation import create_calculation
from app.models import Calculation


def test_create_calculation_add(db_session: Session):
    """
    Integration test:
    - Uses the real SQLAlchemy session from conftest.py
    - Calls create_calculation (which uses the factory)
    - Verifies the row is stored correctly in the DB
    """
    calc_in = CalculationCreate(a=10, b=5, type="add")

    calc = create_calculation(db_session, calc_in)

    # Check returned object
    assert calc.id is not None
    assert calc.a == 10
    assert calc.b == 5
    assert calc.type == "add"
    assert calc.result == 15

    # Check directly via DB query
    stored = db_session.query(Calculation).filter_by(id=calc.id).first()
    assert stored is not None
    assert stored.result == 15


def test_create_calculation_sub(db_session: Session):
    """
    Another integration test to confirm subtraction is persisted correctly.
    """
    calc_in = CalculationCreate(a=20, b=8, type="sub")

    calc = create_calculation(db_session, calc_in)

    assert calc.id is not None
    assert calc.type == "sub"
    assert calc.result == 12


def test_invalid_type_raises(db_session: Session):
    """
    This verifies that an invalid type coming through the CRUD layer
    will raise a ValueError from the factory.
    NOTE: The Pydantic schema already blocks invalid types at the API
    layer, but this is an extra defensive check at the data layer.
    """
    # We bypass Pydantic here by constructing a fake object that looks
    # like CalculationCreate but with an invalid type.
    class FakeCalc:
        def __init__(self):
            self.a = 2
            self.b = 3
            self.type = "pow"  # not supported

    fake_input = FakeCalc()

    with pytest.raises(ValueError):
        create_calculation(db_session, fake_input)  # type: ignore[arg-type]
