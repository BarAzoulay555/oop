import sqlite3
from stock import Stock  # ייבוא מחלקת Stock
from bond import Bond    # ייבוא מחלקת Bond


class dbmodel:
    def __init__(self):
        print("DB connect")
        # אתחול החיבור למסד הנתונים
        self.conn = sqlite3.connect('investments.db')
        self.cursor = self.conn.cursor()
        
        # יצירת טבלה אם היא לא קיימת
        self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='investments';''')
        if not self.cursor.fetchone():
            self.cursor.execute('''CREATE TABLE investments (id INTEGER PRIMARY KEY, name TEXT NOT NULL, base_value REAL NOT NULL, amount REAL NOT NULL)''')
            self.conn.commit()
    
    def insert(self, whatsecurity, amount):   
        # הוספת נייר ערך למסד
        self.cursor.execute('''INSERT INTO investments (name, base_value, amount) VALUES (?, ?, ?)''', (whatsecurity.name, whatsecurity.base_value, amount))
        self.conn.commit()
        print(f"Inserting {whatsecurity.name}...")
    
    def delete(self, identifier):
        """
        מוחק רשומה מהטבלה לפי שם נייר הערך
        """
        if isinstance(identifier, str):  # מחיקה לפי שם
            self.cursor.execute('DELETE FROM investments WHERE name = ?', (identifier,))
        else:
            print("Invalid identifier type. Only string (name) is accepted.")
            return
        self.conn.commit()
        print(f"Deleted {identifier} from portfolio.")

    def get_data(self):
        """
        מחזיר את כל הנתונים מהטבלה
        """
        self.cursor.execute('SELECT * FROM investments')
        rows = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]
        dictanswer = {row[0]: dict(zip(columns, row)) for row in rows}
        return dictanswer

    def calculate_portfolio_risk(self):
        self.cursor.execute('SELECT name, base_value, amount FROM investments')
        rows = self.cursor.fetchall()

        if not rows:
            return 0  # אם אין נתונים

        total_value = 0
        total_risk = 0
        for row in rows:
            name, base_value, amount = row
            if "bond" in name.lower():
                security = Bond(name, base_value, amount, "Government", "Government")
            else:
                security = Stock(name, base_value, amount, "Technology", "High")
            
            security_value = security.get_value()
            security_risk = security.get_risk_level()

            total_value += security_value
            total_risk += security_value * security_risk

        if total_value == 0:
            return 0  # לא ניתן לחלק ב-0

        weighted_risk = total_risk / total_value
        return round(weighted_risk, 2)

    def __del__(self):
        self.conn.close()  # סגירת החיבור למסד הנתונים
        print("DB disconnect")
