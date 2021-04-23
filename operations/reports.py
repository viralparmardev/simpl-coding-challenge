from models import user, merchant
from controllers import report


def get_discount_received(arguments):
    merchant_name = arguments[2]
    merchant_object = merchant.get_object_by_name(merchant_name)
    result = report.get_discount_received(merchant_object)
    print(result)


def get_dues_for_user(arguments):
    user_name = arguments[2]
    user_object = user.get_object_by_name(user_name)
    result = report.get_dues(user_object)
    print(result)


def get_users_at_credit_limit():
    result = report.users_at_credit_limit()
    print(result)


def get_total_dues():
    result = report.total_dues()
    print(result)
