from responses import failure


def update_discount(merchant, discount_percentage):
    if merchant is None:
        return failure.failure("no such merchant exists")

    merchant.set_discount_percentage(discount_percentage)
    return merchant
