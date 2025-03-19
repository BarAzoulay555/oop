class Bond:
    def __init__(self, name, base_value, amount, issuer, bond_type):
        self.name = name
        self.base_value = base_value
        self.amount = amount
        self.issuer = issuer
        self.bond_type = bond_type

    def get_value(self):
        """
        מחשב את הערך של האג"ח על פי הכמות והערך הבסיסי
        """
        return self.base_value * self.amount

    def get_risk_level(self):
        """
        מחזיר את רמת הסיכון של האג"ח
        """
        if self.bond_type == "Government":
            return 1  # סיכון נמוך
        elif self.bond_type == "Corporate":
            return 5  # סיכון גבוה יותר
        return 3  # סיכון ממוצע
