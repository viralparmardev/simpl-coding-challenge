from models import merchant
from controllers import update


def update_merchant_discount_percentage(arguments):
    name = arguments[2]
    discount_percentage_string = arguments[3]
    discount_percentage = int(discount_percentage_string[0: -1])
    merchant_object = merchant.get_object_by_name(name)
    result = update.update_discount(merchant_object, discount_percentage)
    print(result)
