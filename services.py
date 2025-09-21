def get_available_loans(age: int, income: float, location: str):
    """Determines the available loan types for a customer based on their age, income, and location.

    Args:
        age (int): The customer's age in years.
        income (float): The customer's monthly income.
        location (str): The customer's location, typically a Brazilian state code (e.g., 'SP', 'RJ').

    Returns:
        list: A list of dictionaries, each containing the loan type and its interest rate.

    Example:
        ```python
        loans = get_available_loans(age=25, cpf="123.456.789-00", income=4000.0, location="SP")
        # Returns: [
        #     {"type": "PERSONAL", "interest_rate": 4},
        #     {"type": "GUARANTEED", "interest_rate": 3}
        # ]
        ```
    """
    
    loans = []
    
    if income <= 3000 or ((income >= 3000 and income <= 5000) and age < 30 and location.upper() == "SP"):
        loans.append(
            {
                "type": "PERSONAL",
                "interest_rate": 4
            },
        )
        
    if income >= 5000:
        loans.append(
            {
                "type": "CONSIGNMENT",
                "interest_rate": 2
            },
        )
        
    if income <= 3000 or ((income >= 3000 and income <= 5000) and age < 30 and location.upper() == "SP"):
        loans.append(
            {
                "type": "GUARANTEED",
                "interest_rate": 3
            },
        )
    
    return loans
