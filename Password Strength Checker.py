#Defining Parameters 
def check_password_strength(password):
    print("\n=== Password Strength Checker ===")
    
    # Initialize strength level
    strength = 0
    
    # Check for password length
    if len(password) >= 16:
        strength += 1
    else:
        print("Password is too short. It should be at least 16 characters.")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        print("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        print("Password should contain at least one lowercase letter.")
    
    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        print("Password should contain at least one number.")
    
    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"
    if any(char in special_characters for char in password):
        strength += 1
    else:
        print("Password should contain at least one special character (e.g., !, @, #).")
    
    # Determine strength message
    if strength == 5:
        print("Your password is very strong!")
    elif 3 <= strength < 5:
        print("Your password is moderate. Consider making it stronger.")
    else:
        print("Your password is weak. Please improve it.")
    
# Get input from the user
user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)
 