transactions = []


def get_transactions():
    return transactions


def add_transaction(transaction_object):
    transactions.append(transaction_object)


class Transaction:
    def __init__(self, txn_type=None, user=None, merchant=None, txn_amount=None, payback_amount=None):
        self.txn_type = txn_type  # purchase or payback
        self.user = user
        self.merchant = merchant
        self.txn_amount = txn_amount
        self.payback_amount = payback_amount
        self.is_successful = False

    def get_txn_type(self):
        return self.txn_type

    def set_txn_type(self, txn_type):
        self.txn_type = txn_type

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_merchant(self):
        return self.merchant

    def set_merchant(self, merchant):
        self.merchant = merchant

    def get_txn_amount(self):
        return self.txn_amount

    def set_txn_amount(self, txn_amount):
        self.txn_amount = txn_amount

    def get_payback_amount(self):
        return self.payback_amount

    def set_payback_amount(self, payback_amount):
        self.payback_amount = payback_amount

    def check_is_successful(self):
        return self.is_successful

    def mark_successful(self):
        self.is_successful = True
