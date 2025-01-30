from datetime import datetime
from datetime import date


class Transaction:
    """
    This class represents Transaction object
    """

    def __init__(self, amount, desc, label=None):
        self.amount = amount
        self.date = date.today()
        self.desc = desc
        self.label = label if label else "other"

    def update_date(self, new_date):
        self.date = datetime.strptime(new_date, "%Y-%m-%d")

    def update_label(self, new_label):
        self.label = new_label

    def update_amount(self, new_amount):
        self.amount = new_amount

    def to_dict(self):
        return {
            'amount': self.amount,
            'date': self.date.strftime('%Y-%m-%d'),
            'desc': self.desc,
            'label': self.label
        }

    def __str__(self):
        return f"{{'amount': {self.amount}, 'date': '{self.date.strftime('%Y-%m-%d')}', 'description': '{self.desc}', 'label': '{self.label}'}}"


class Income(Transaction):
    """
    A subclass of Transaction class that represents Income object
    """

    income_labels = ["salary income", "passive income", "capital gains", "other"]

    def __init__(self, amount, description, label=None):
        super().__init__(amount, description, label)
        if label:
            Income.income_labels.append(label)


class Expense(Transaction):
    """
    A subclass of Transaction class that represents Expense object
    """

    expense_labels = ["utility", "grocery", "transportation", "entertainment", "healthcare", "other"]

    def __init__(self, amount, description, label=None):
        super().__init__(amount, description, label)
        if label:
            Income.income_labels.append(label)
