try:
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
except ValueError:
    print("Invalid input. Please enter a numerical value.")
    exit()

monthly_savings = monthly_income - monthly_expenses

annual_savings_without_interest = monthly_savings * 12
interest_earned = annual_savings_without_interest * 0.05
projected_savings = annual_savings_without_interest + interest_earned

print(f"Your monthly savings are ${monthly_savings:,.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:,.2f}.")
