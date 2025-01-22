import re

def check_password_strength(password):
    # Define criteria for a strong password
    min_length = 16
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Check length
    if len(password) < min_length:
        return "Weak: Strong Password must be at least 16 characters long."
    
    if len(password) < min_length and not has_digit:
        return "Weak: Strong Password Must be at least 16 characters long with digit."
    
    if len(password) < min_length and not has_special:
        return "Weak: Strong Password Must be at least 16 characters long with Special Character."
    
    
    
    # Check if all criteria are met
    if has_upper and has_lower and has_digit and has_special:
        return "Strong: Your password is strong."
    
    # Provide feedback for missing criteria
    missing = []
    if not has_upper:
        missing.append("an uppercase letter")
    if not has_lower:
        missing.append("a lowercase letter")
    if not has_digit:
        missing.append("a digit")
    if not has_special:
        missing.append("a special character")
    
    return f"Medium: Your password is missing {', '.join(missing)}."

# Example usage
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
