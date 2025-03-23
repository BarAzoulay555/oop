from dbmodel import dbmodel
from ollamamodel import ollamamodel
from stock import Stock  # הייבוא של מחלקת Stock
from bond import Bond    # הייבוא של מחלקת Bond

class controller:
    def __init__(self):
        self.dbmodel = dbmodel()
        self.ai_model = ollamamodel()  # יצירת אובייקט של המודל אולמה

    def buy(self, whatsecurity, amount):
        print("Buying...")
        if isinstance(amount, int):
             self.dbmodel.insert(whatsecurity, amount)
        else:
             print("Invalid amount. Please enter a valid number.")


    def sell(self, identifier):
        print(f"Selling {identifier}...")
        self.dbmodel.delete(identifier)

    def get_advice(self, question):
        """
        שואל את המודל אולמה ומחזיר תשובה
        """
        print("Consulting Ollama AI model...")
        answer = self.ai_model.get_advice(question)  # ← תיקון פה!
        return answer
