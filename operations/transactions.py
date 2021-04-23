from models import user, merchant, transaction
from controllers import purchase, payback


def new_purchase(arguments):
    user_name = arguments[2]
    merchant_name = arguments[3]
    amount = int(arguments[4])
    user_object = user.get_object_by_name(user_name)
    merchant_object = merchant.get_object_by_name(merchant_name)
    transaction_object = transaction.Transaction(txn_type="purchase", user=user_object,
                                                 merchant=merchant_object, txn_amount=amount)
    transaction.add_transaction(transaction_object)
    result = purchase.purchase_entry(transaction_object)
    print(result)


def payback_dues(arguments):
    user_name = arguments[1]
    amount = int(arguments[2])
    user_object = user.get_object_by_name(user_name)
    transaction_object = transaction.Transaction(txn_type="payback", user=user_object,
                                                 payback_amount=amount)
    transaction.add_transaction(transaction_object)
    result = payback.payback_dues(transaction_object)
    print(result)
