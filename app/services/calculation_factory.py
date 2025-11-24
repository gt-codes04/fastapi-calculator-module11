from typing import Protocol

class Operation(Protocol):
    def compute(self, a: float, b: float) -> float:
        ...

class AddOperation:
    def compute(self, a: float, b: float) -> float:
        return a + b

class SubOperation:
    def compute(self, a: float, b: float) -> float:
        return a - b

class MulOperation:
    def compute(self, a: float, b: float) -> float:
        return a * b

class DivOperation:
    def compute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b


class CalculationFactory:
    @staticmethod
    def create(operation_type: str) -> Operation:
        op = operation_type.lower()
        if op == "add": return AddOperation()
        if op == "sub": return SubOperation()
        if op == "mul": return MulOperation()
        if op == "div": return DivOperation()
        raise ValueError(f"Unsupported calculation type: {operation_type}")
