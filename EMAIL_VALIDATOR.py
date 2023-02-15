import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email = input("Enter email address: ")
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
