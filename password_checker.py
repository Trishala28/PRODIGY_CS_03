import re

def check_password_strength(password):
    # Initialize strength score
    score = 0
    feedback = []

    # Length check
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif length >= 8 and length < 12:
        feedback.append("Password length is acceptable, but longer passwords are stronger.")
        score += 1
    else:
        feedback.append("Password length is strong.")
        score += 2

    # Uppercase letter check
    if re.search(r'[A-Z]', password):
        feedback.append("Password contains uppercase letters.")
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Lowercase letter check
    if re.search(r'[a-z]', password):
        feedback.append("Password contains lowercase letters.")
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        feedback.append("Password contains digits.")
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Special character check
    if re.search(r'[\W_]', password):
        feedback.append("Password contains special characters.")
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Strength determination
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback.append(f"Password strength: {strength} ({score}/6)")

    return "\n".join(feedback)

# Example usage
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))

