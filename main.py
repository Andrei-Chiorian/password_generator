import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a password string with the given length and constraints.

    :param length: The length of the password
    :param nums: The minimum number of numbers in the password
    :param special_chars: The minimum number of special characters in the password
    :param uppercase: The minimum number of uppercase letters in the password
    :param lowercase: The minimum number of lowercase letters in the password
    """
    # Define the possible characters for the password
    letters = string.ascii_letters
    # Digits are the numbers 0-9
    digits = string.digits
    # Symbols are the special characters
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            # Randomly select one of the characters and add it to the password
            password += secrets.choice(all_characters)

        # The constraints are the minimum number of each type of character
        constraints = [
            # Require at least one number
            (nums, r'\d'),
            # Require at least one special character
            (special_chars, fr'[{symbols}]'),
            # Require at least one uppercase letter
            (uppercase, r'[A-Z]'),
            # Require at least one lowercase letter
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        # If all the constraints are satisfied, break out of the loop
        if all(
                # Check if the constraint is satisfied
                constraint <= len(re.findall(pattern, password))
                # For each constraint
                for constraint, pattern in constraints
        ):
            break

    return password


new_password = generate_password()
print('Generated password:', new_password)