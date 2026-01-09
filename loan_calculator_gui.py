import tkinter as tk
from tkinter import ttk, messagebox

class LoanCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Loan Calculator")
        self.root.geometry("400x300")

        # Create input fields
        self.principal_label = ttk.Label(root, text="Principal:")
        self.principal_label.grid(row=0, column=0, pady=5, sticky=tk.W)
        self.principal_entry = ttk.Entry(root)
        self.principal_entry.grid(row=0, column=1, pady=5)

        self.rate_label = ttk.Label(root, text="Annual Rate (%):")
        self.rate_label.grid(row=1, column=0, pady=5, sticky=tk.W)
        self.rate_entry = ttk.Entry(root)
        self.rate_entry.grid(row=1, column=1, pady=5)

        self.term_label = ttk.Label(root, text="Term (years):")
        self.term_label.grid(row=2, column=0, pady=5, sticky=tk.W)
        self.term_entry = ttk.Entry(root)
        self.term_entry.grid(row=2, column=1, pady=5)

        # Create calculate button
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_loan)
        self.calculate_button.grid(row=3, columnspan=2, pady=10)

        # Create results display
        self.monthly_label = ttk.Label(root, text="Monthly Payment:")
        self.monthly_label.grid(row=4, column=0, pady=5, sticky=tk.W)
        self.monthly_value = ttk.Label(root, text="0.00")
        self.monthly_value.grid(row=4, column=1, pady=5)

        self.total_payment_label = ttk.Label(root, text="Total Payment:")
        self.total_payment_label.grid(row=5, column=0, pady=5, sticky=tk.W)
        self.total_payment_value = ttk.Label(root, text="0.00")
        self.total_payment_value.grid(row=5, column=1, pady=5)

        self.total_interest_label = ttk.Label(root, text="Total Interest:")
        self.total_interest_label.grid(row=6, column=0, pady=5, sticky=tk.W)
        self.total_interest_value = ttk.Label(root, text="0.00")
        self.total_interest_value.grid(row=6, column=1, pady=5)

    def calculate_loan(self):
        try:
            principal = float(self.principal_entry.get())
            annual_rate = float(self.rate_entry.get()) / 100
            years = int(self.term_entry.get())

            monthly_rate = annual_rate / 12
            num_payments = years * 12

            # Monthly payment calculation
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
            total_payment = monthly_payment * num_payments
            total_interest = total_payment - principal

            # Update display
            self.monthly_value.config(text=f"{monthly_payment:.2f}")
            self.total_payment_value.config(text=f"{total_payment:.2f}")
            self.total_interest_value.config(text=f"{total_interest:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for principal, rate, and term.")


def main():
    root = tk.Tk()
    app = LoanCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
