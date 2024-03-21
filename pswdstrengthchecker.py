
def check_password_strength(pswd):
    # Define criteria for strong password
    length_requirement = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[{]}\"|;:',<.>/?"
    
    # Check length requirement
    if len(pswd) < length_requirement:
        return "Password is too short. It must be at least {} characters long.".format(length_requirement)
    
    # Check for uppercase, lowercase, digit, and special characters
    for char in pswd:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    # Generate feedback based on missing criteria
    feedback = []
    if not has_uppercase:
        feedback.append("Password must contain at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password must contain at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password must contain at least one digit.")
    if not has_special:
        feedback.append("Password must contain at least one special character.")
    
    # Check if all criteria are met
    if feedback:
        return "Password is weak. " + " ".join(feedback)
    else:
        return "Password is strong."

# Test the function
password = input("Enter your password: ")
print(check_password_strength(password))
