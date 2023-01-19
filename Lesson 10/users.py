from faker import Faker

fake = Faker('uk_UA')  # for generating ukrainian name


def create_user(name: str, password: str) -> tuple:
    def is_valid_name(name: str) -> bool:
        return all(word.isalpha() for word in name.split()) if name else False

    def is_valid_password(password: str) -> bool:
        one_digit_check = any(1 for c in password if c.isdigit())
        length_check = len(password) >= 8
        repeated_characters_check = not any(1 for i in range(len(password[1:-1]))
                                            if password[i - 1] == password[i] and password[i + 1] == password[i])
        alphabetic_chars_check = sum(1 for c in password if c.isalpha()) >= 4
        lower_and_upper_check = any(1 for c in password if c.isupper()) and any(1 for c in password if c.islower())

        return one_digit_check and length_check and repeated_characters_check and alphabetic_chars_check and lower_and_upper_check

    if not is_valid_name(name):
        name = fake.name()
    if not is_valid_password(password):
        password = fake.password(length=8, special_chars=False)

    print(f"Created new user:\nname: {name}, password: {password}")
    return name, password
