def create_username(first_name, last_name, role):
    consonants = ''.join([c for c in first_name if c.lower() not in 'aeiou'])
    consonant_count = len(consonants)
    if role.lower() == 'pilot':
        username_prefix = 'P'
    elif role.lower() == 'cabin crew':
        username_prefix = 'C'
    else:
        username_prefix = ''
    username = f"{username_prefix}{consonants.lower()}{last_name.lower()}{consonant_count}"
    return username

# Function to create password
def create_password(first_name, last_name, role):
    vowels = ''.join([c for c in first_name if c.lower() in 'aeiou'])
    consonants = ''.join([c for c in first_name if c.lower() not in 'aeiou'])
    password_prefix = 'P' if role.lower() == 'pilot' else 'C' if role.lower() == 'cabin crew' else ''
    password = f"{last_name.lower()}{len(vowels) * len(consonants)}{first_name.capitalize()}{password_prefix}."
    return password
