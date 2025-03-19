from dbmodel import dbmodel
from ollamamodel import ollamamodel  # ייבוא מחדש של ollama

from dbmodel import dbmodel

class controller:
    def __init__(self):
        self.dbmodel = dbmodel()

    def buy(self, whatsecurity, amount):
        print("Buying...")
        if isinstance(amount, int) and isinstance(whatsecurity, str):
            self.dbmodel.insert(whatsecurity, amount)
        else:
            print("Invalid input for security or amount.")

    def sell(self, identifier):
        print(f"Selling {identifier}...")
        self.dbmodel.delete(identifier)

    def get_advice(self, question):
        return "Consulting the market... Here is some advice."
