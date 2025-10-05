def safe_divide(numerator, denominator):
    """
    Performs division robustly, handling ZeroDivisionError and ValueError.
    """
    try:
        # 1. Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # 2. Perform the division
        result = num / den
        
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
        
    except ValueError:
        # Handle non-numeric input (e.g., 'ten' or 'five')
        return "Error: Please enter numeric values only."
        
    else:
        # Executes only if no exceptions are raised (successful division)
        return f"The result of the division is {result}"