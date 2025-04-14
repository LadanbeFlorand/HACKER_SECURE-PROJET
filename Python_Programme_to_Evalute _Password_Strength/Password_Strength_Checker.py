import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*()_+{}\[\]:;\"'<>,.?/~`\\|-]", password)

    # Count how many rules are passed
    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Feedback based on score
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
