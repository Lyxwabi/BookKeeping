import json
from transactions.Transaction import Income
from transactions.Transaction import Expense


class Book:
    """
    This class represents the Book object that keeps records of
    all transactions of users
    """

    def __init__(self):
        self.book = {"expense": [],
                     "income": []}
        self.load_data()

    def save_data(self):
        with open("data.json", 'w') as file:
            json.dump(self.book, file, indent=2)

    def load_data(self):
        try:
            with open("data.json", 'r') as file:
                self.book = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book = {"expense": [],
                         "income": []}

    def add_transaction(self, transaction):
        transaction_dict = transaction.to_dict()
        if isinstance(transaction, Income):
            self.book["income"].append(transaction_dict)
        elif isinstance(transaction, Expense):
            self.book["expense"].append(transaction_dict)
        self.save_data()

    def remove_transaction(self, t_type, index):
        index -= 1
        if t_type in self.book and index < len(self.book[t_type]):
            del self.book[t_type][index]
            self.save_data()

    def display_by_label(self, label):
        print(f"Transactions with label '{label}':")

        for t_type in ['income', 'expense']:
            index = 1
            print(f"{t_type}:")
            for transaction in self.book[t_type]:
                if transaction['label'] == label:
                    print(f"{index}. {transaction}")
                    index += 1

    def display_by_date(self, date):
        print(f"Transactions on '{date}':")

        for t_type in ['income', 'expense']:
            index = 1
            print(f"{t_type}:")
            for transaction in self.book[t_type]:
                if transaction['date'] == date:
                    print(f"{index}. {transaction}")
                    index += 1

    def display_all(self):
        print(f"All transactions:")
        for t_type in ['income', 'expense']:
            index = 1
            print(f"{t_type}:")
            for transaction in self.book[t_type]:
                print(f"{index}. {transaction}")
                index += 1



book = Book()
t = Income(100, "wage", "salary income")
e = Expense(100, "dinner", "entertainment")
book.add_transaction(t)
book.add_transaction(e)
book.display_by_label("salary income")
book.display_all()
book.display_by_date('2023-11-20')