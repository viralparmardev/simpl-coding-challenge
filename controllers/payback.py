from responses import failure, success


def payback_dues(transaction):
    user = transaction.get_user()
    amount = transaction.get_payback_amount()

    if user is None:
        return failure.failure("no such user exists")

    elif amount == 0:
        return failure.failure("amount can not be zero")

    dues = user.get_dues()
    if amount > dues:
        return failure.failure("amount can not be more than dues")

    user.set_dues(dues - amount)

    transaction.mark_successful()
    return success.success()
