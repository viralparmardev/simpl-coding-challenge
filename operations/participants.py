from models import user, merchant
from responses import exceptions
from utilities import validate


def new_user(arguments):
    name = arguments[2]
    email = arguments[3]
    if not validate.email(email):
        exceptions.invalid_argument("email")

    credit_limit = int(arguments[4])
    if credit_limit < 1:
        exceptions.invalid_argument("credit limit")

    user_object = user.User(name, email, credit_limit)
    user.add_user(user_object)
    print(user_object)


def new_merchant(arguments):
    name = arguments[2]
    discount_percentage_string = arguments[3]
    if not validate.discount(discount_percentage_string):
        exceptions.invalid_argument("discount")

    discount_percentage = int(discount_percentage_string[0: -1])
    if discount_percentage < 1:
        exceptions.invalid_argument("discount percentage")

    merchant_object = merchant.Merchant(name, discount_percentage)
    merchant.add_merchant(merchant_object)
    print(merchant_object)
