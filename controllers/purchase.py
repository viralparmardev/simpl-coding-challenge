from responses import success, failure


def purchase_entry(transaction):
    user = transaction.get_user()
    merchant = transaction.get_merchant()
    amount = transaction.get_txn_amount()

    if user is None:
        return failure.failure("no such user exists")

    elif merchant is None:
        return failure.failure("no such merchant exists")

    elif amount < 1:
        return failure.failure("amount can not be less than one")

    credit_limit = user.get_credit_limit()
    dues = user.get_dues()
    new_dues = dues + amount
    if new_dues > credit_limit:
        return failure.failure("credit limit")

    user.set_dues(new_dues)
    discount_percentage = merchant.get_discount_percentage()
    discount_received = merchant.get_discount_received()

    discounted_amount = (discount_percentage / 100) * amount
    merchant.set_discount_received(discount_received + discounted_amount)

    transaction.mark_successful()
    return success.success()
