merchants = []


def get_merchants():
    return merchants


def add_merchant(merchant_object):
    merchants.append(merchant_object)


def get_object_by_name(name):
    for merchant_object in merchants:
        if merchant_object.name == name:
            return merchant_object
    return None


class Merchant:
    def __init__(self, name=None, discount_percentage=None):
        self.name = name
        self.discount_percentage = discount_percentage
        self.discount_received = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_discount_percentage(self):
        return self.discount_percentage

    def set_discount_percentage(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def get_discount_received(self):
        return self.discount_received

    def set_discount_received(self, discount_received):
        self.discount_received = discount_received

    def __repr__(self):
        if not (self.name and self.discount_percentage):
            return "Merchant not completely initialized"
        else:
            return self.name + " (" + str(self.discount_percentage) + "%)"
