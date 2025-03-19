from dbmodel import dbmodel

# יצירת חיבור למסד הנתונים
db = dbmodel()

# הוספת ניירות ערך לדוגמה
db.insert("Apple", 150, 10)  # מניה
db.insert("Israel Gov Bond", 100, 5)  # אג"ח

# הצגת התיק בטבלה
print("\n📊 Portfolio Table:")
db.display_portfolio()

# חישוב והצגת רמת הסיכון
portfolio_risk = db.calculate_portfolio_risk()
print(f"\n⚠️ Portfolio Risk Level: {portfolio_risk}")
