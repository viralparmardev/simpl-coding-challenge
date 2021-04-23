import re

email_regex = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
email_pattern = re.compile(email_regex)


def email(email_address):
    if not re.match(email_pattern, email_address):
        return False
    else:
        return True


def discount(discount_percentage_string):
    if discount_percentage_string[-1] != '%':
        return False
    else:
        return True
