from pydantic import BaseModel

class Customer(BaseModel):
    """Represents a customer with attributes required for loan eligibility assessment.

    Attributes:
        age (int): The customer's age in years.
        cpf (str): The customer's Brazilian CPF number.
        name (str): The customer's full name.
        income (float): The customer's monthly income.
        location (str): The customer's location, typically a Brazilian state code (e.g., 'SP', 'RJ').

    Example:
        ```python
        customer = Customer(
            age=21,
            cpf="123.456.789-00",
            name="João Silva",
            income=5000.0,
            location="SP"
        )
        ```
    """
    
    age: int
    cpf: str
    name: str
    income: float
    location: str
    