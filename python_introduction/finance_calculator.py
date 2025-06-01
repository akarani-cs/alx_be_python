income = input("Enter your monthly income")

expenses = input("Enter your monthly expenses")

monthly_savings = float(income) - float(expenses)

print("Your monthly savings is", monthly_savings)

projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)

print("Your projected annual savings is", projected_savings)
