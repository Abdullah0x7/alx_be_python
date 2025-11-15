inc = input("Enter your monthly income: ")
income = float(inc)
tme = input("Enter your total monthly expenses: ")
tot_monthly_exp = float(tme)
msavs = income - tot_monthly_exp
monthly_savings = float(msavs)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")
