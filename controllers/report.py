from models.user import get_users
from responses import failure


def get_discount_received(merchant):
    if merchant is None:
        return failure.failure("no such merchant exists")

    return merchant.get_discount_received()


def get_dues(user):
    if user is None:
        return failure.failure("no such user exists")

    return user.get_dues()


def users_at_credit_limit():
    users = []

    for candidate in get_users():
        if candidate.get_dues() == candidate.get_credit_limit():
            users.append(candidate.get_name())

    if not users:
        return "none"
    else:
        output_string = ""
        for user in users:
            output_string += user + "\n"
        return output_string


def total_dues():
    items = []
    total = 0

    for candidate in get_users():
        user_name = candidate.get_name()
        user_dues = candidate.get_dues()
        total += user_dues
        add_line = user_name + ": " + str(user_dues)
        items.append(add_line)

    items.append("total: " + str(total))

    output_string = ""
    for item in items:
        output_string += item + "\n"
    return output_string
