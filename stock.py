class Stock:
    def __init__(self, name, base_value, amount, industry, volatility):
        self.name = name
        self.base_value = base_value
        self.amount = amount
        self.industry = industry
        self.volatility = volatility

    def get_value(self):
        """
        מחשב את הערך של המניה על פי הכמות והערך הבסיסי
        """
        return self.base_value * self.amount

    def get_risk_level(self):
        """
        מחזיר את רמת הסיכון של המניה
        """
        industry_risk = {
            "Technology": 6,
            "Transportation": 5,
            "Energy & Health": 4,
            "Industry & Finance": 3,
            "Real Estate": 2,
            "Consumer": 1
        }
        risk_score = industry_risk.get(self.industry, 1) * (2 if self.volatility == "High" else 1)
        return risk_score
