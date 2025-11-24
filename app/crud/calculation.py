from sqlalchemy.orm import Session
from app import models, schemas
from app.services.calculation_factory import CalculationFactory

def create_calculation(db: Session, calculation_in: schemas.CalculationCreate, user_id: int | None = None):
    factory = CalculationFactory.create(calculation_in.type)
    result = factory.compute(calculation_in.a, calculation_in.b)

    db_calc = models.Calculation(
        a=calculation_in.a,
        b=calculation_in.b,
        type=calculation_in.type,
        result=result,
        user_id=user_id
    )
    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)
    return db_calc
