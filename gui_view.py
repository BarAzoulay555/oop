import tkinter as tk
from tkinter import messagebox, simpledialog
from view import view
from stock import Stock
from bond import Bond
from tabulate import tabulate

class GUIView:
    def __init__(self, root):
        self.root = root
        self.root.title("Investment Portfolio")
        self.portfolio = view()

        tk.Label(root, text="📊 Investment Portfolio Menu", font=("Arial", 14)).pack(pady=10)

        tk.Button(root, text="Buy Security", width=30, command=self.buy_security).pack(pady=5)
        tk.Button(root, text="Sell Security", width=30, command=self.sell_security).pack(pady=5)
        tk.Button(root, text="Get Investment Advice (AI)", width=30, command=self.get_advice).pack(pady=5)
        tk.Button(root, text="Show Portfolio (Table)", width=30, command=self.display_table).pack(pady=5)
        tk.Button(root, text="Show Portfolio Risk Level", width=30, command=self.display_risk).pack(pady=5)
        tk.Button(root, text="Exit", width=30, command=self.root.quit).pack(pady=10)

    def buy_security(self):
        options = {
            1: Stock(name="Apple", base_value=150, amount=10, industry="Technology", volatility="High"),
            2: Stock(name="Tesla", base_value=360, amount=8, industry="Transportation", volatility="Medium"),
            3: Bond(name="Israel Gov Bond", base_value=100, amount=5, issuer="Government", bond_type="Government"),
            4: Bond(name="Corporate Bond X", base_value=90, amount=12, issuer="Corporate", bond_type="Corporate"),
        }

        choices_text = "\n".join([f"{k}. {v.name}" for k, v in options.items()])
        choice = simpledialog.askinteger("Buy Security", f"Choose a security to buy:\n{choices_text}")

        if choice in options:
            amount = simpledialog.askinteger("Amount", "How much do you want to buy?")
            if amount:
                self.portfolio.controller.buy(options[choice], amount)
                messagebox.showinfo("Success", f"Bought {amount} of {options[choice].name}")
        else:
            messagebox.showerror("Error", "Invalid choice.")

    def sell_security(self):
        data = self.portfolio.db.get_data()
        if not data:
            messagebox.showwarning("No Investments", "⚠️ No investments found.")
            return

        choices = {k: v['name'] for k, v in data.items()}
        choices_text = "\n".join([f"{k}. {v}" for k, v in choices.items()])
        choice = simpledialog.askinteger("Sell Security", f"Choose a security to sell:\n{choices_text}")

        if choice in choices:
            self.portfolio.controller.sell(choices[choice])
            messagebox.showinfo("Sold", f"Sold {choices[choice]}")
        else:
            messagebox.showerror("Error", "Invalid choice.")

    def get_advice(self):
        question = simpledialog.askstring("Ask AI", "Enter your investment question:")
        if question:
            answer = self.portfolio.controller.get_advice(question)
            messagebox.showinfo("AI Advice", answer)

    def display_table(self):
        data = self.portfolio.db.get_data()
        if not data:
            messagebox.showwarning("Portfolio", "⚠️ No investments found in the portfolio.")
            return

        table_data = [[k] + list(v.values()) for k, v in data.items()]
        headers = ["Key", "ID", "Name", "Base Value", "Amount"]
        text = tabulate(table_data, headers=headers, tablefmt="grid")
        self._show_large_text("Portfolio Table", text)

    def display_risk(self):
        risk = self.portfolio.db.calculate_portfolio_risk()
        messagebox.showinfo("Portfolio Risk", f"⚠️ Risk Level: {risk}")

    def _show_large_text(self, title, content):
        window = tk.Toplevel(self.root)
        window.title(title)
        text_widget = tk.Text(window, wrap="word", width=80, height=20)
        text_widget.insert("1.0", content)
        text_widget.pack(expand=True, fill="both")
        tk.Button(window, text="Close", command=window.destroy).pack(pady=5)
