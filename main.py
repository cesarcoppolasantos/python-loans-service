from fastapi import FastAPI, HTTPException
from models import Customer
from services import get_available_loans
from brutils import is_valid_cpf, remove_symbols_cpf


app = FastAPI()

BRAZILIAN_STATES = [
    "AC", "AL", "AP", "AM", 
    "BA", "CE", "DF", "ES", 
    "GO", "MA", "MT", "MS", 
    "MG", "PA", "PB", "PR", 
    "PE", "PI", "RJ", "RN", 
    "RS", "RO", "RR", "SC", 
    "SP", "SE", "TO"
]

@app.post("/customer-loans")
def customer_loans(customer: Customer):
    """Processes the request for available loans for a customer based on their information 
    and the requirements of the Backend <Brazil> challenge.

    Args:
        customer (Customer): Object containing the customer's information, 
        including name, CPF, age, income, and location.

    Returns:
        dict: A dictionary containing the customer's name and the list of available loans.

    Raises:
        HTTPException: 
            - If the CPF is invalid, returns status 400 with the message "Invalid CPF."
            - If the location does not correspond to a valid Brazilian state, 
            returns status 400 with the message "Invalid State."
            - If the customer's age is under 18, returns status 400 with the message "Age must be over 18."

    Example:
        ```python
        customer = Customer(name="João Silva", cpf="123.456.789-00", age=21, income=5000.0, location="SP")
        response = customer_loans(customer)
        # Returns: {"customer": "João Silva", "loans": [...]}
        ```
    """
        
    cpf_without_symbols = remove_symbols_cpf(customer.cpf)
    
    if not is_valid_cpf(cpf_without_symbols):
        raise HTTPException(
            status_code=400,
            detail="Invalid CPF."
        )
    
    if customer.location.upper() not in BRAZILIAN_STATES:
        raise HTTPException(
                status_code=400,
                detail="Invalid State."
            )
    
    if customer.age < 18:
        raise HTTPException(
            status_code=400,
            detail="Age must be over 18."
            
        )
    
    loans = get_available_loans(customer.age, customer.cpf, customer.income, customer.location)
    
    return {
        "customer": customer.name, 
            "loans": loans
    }
