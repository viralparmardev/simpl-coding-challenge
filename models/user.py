users = []


def get_users():
    return users


def add_user(user_object):
    users.append(user_object)


def get_object_by_name(name):
    for user_object in users:
        if user_object.name == name:
            return user_object
    return None


class User:
    def __init__(self, name=None, email=None, credit_limit=None):
        self.name = name
        self.email = email
        self.credit_limit = credit_limit
        self.dues = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_credit_limit(self):
        return self.credit_limit

    def set_credit_limit(self, credit_limit):
        self.credit_limit = credit_limit

    def get_dues(self):
        return self.dues

    def set_dues(self, dues):
        self.dues = dues

    def __repr__(self):
        if not (self.name and self.email and self.credit_limit):
            return "User not completely initialized"
        else:
            return self.name + " (" + str(self.credit_limit) + ")"
