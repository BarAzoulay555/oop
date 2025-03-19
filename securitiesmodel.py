# כדאי לבקש למלא בתכונות מסוכן וכך נוכל להגדיר סוגי ניירות ערך ולהגדיר קשרים ביניהם

class Security:
    """
    מחלקת בסיס לניירות ערך (אב למניות ואג"ח).
    """
    def __init__(self, name, base_value, amount):
        """
        אתחול תכונות כלליות של ניירות ערך.
        :param name: שם נייר הערך
        :param base_value: מחיר התחלתי
        :param amount: כמות ניירות הערך
        """
        self.name = name
        self.base_value = base_value
        self.amount = amount

    def get_value(self):
        """
        מחזירה את הערך הכולל של נייר הערך.
        """
        return self.base_value * self.amount

    def __str__(self):
        """
        מציגה את פרטי נייר הערך.
        """
        return f"Security: {self.name}, Value: {self.get_value()}"


class Stock(Security):
    """
    מחלקת מניה – יורשת מ-Security ומוסיפה שדה ענף ותנודתיות.
    """
    def __init__(self, name, base_value, amount, industry, volatility):
        """
        אתחול תכונות של מניה.
        :param industry: תחום ההשקעה של המניה
        :param volatility: רמת התנודתיות של המניה
        """
        super().__init__(name, base_value, amount)
        self.industry = industry
        self.volatility = volatility

    def get_risk_level(self):
        """
        קובעת את רמת הסיכון של המניה על פי הענף והתנודתיות.
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

    def __str__(self):
        """
        מציגה את פרטי המניה.
        """
        return f"Stock: {self.name}, Industry: {self.industry}, Risk Level: {self.get_risk_level()}"


class Bond(Security):
    """
    מחלקת אג"ח – יורשת מ-Security ומוסיפה סוג הנפקה.
    """
    def __init__(self, name, base_value, amount, issuer, bond_type):
        """
        אתחול תכונות של אג"ח.
        :param issuer: מי הנפיק את האג"ח (חברה/ממשלה)
        :param bond_type: סוג האג"ח (קונצרני/ממשלתי)
        """
        super().__init__(name, base_value, amount)
        self.issuer = issuer
        self.bond_type = bond_type

    def get_risk_level(self):
        """
        קובעת את רמת הסיכון של האג"ח לפי סוג ההנפקה.
        """
        if self.bond_type == "Government":
            return 1
        elif self.bond_type == "Corporate":
            return 5
        return 3  # ערך ברירת מחדל

    def __str__(self):
        """
        מציגה את פרטי האג"ח.
        """
        return f"Bond: {self.name}, Issuer: {self.issuer}, Type: {self.bond_type}, Risk Level: {self.get_risk_level()}"

