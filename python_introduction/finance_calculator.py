inc = input("Enter your monthly income: ")
income = int(inc)
tme = input("Enter your total monthly expenses: ")
tot_monthly_exp = int(tme)
monthly_savings = income - tot_monthly_exp
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")
