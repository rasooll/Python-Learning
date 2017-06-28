# Your function for calculating payment goes here
def rasool(principal, annual_interest_rate, duration):
	r = (annual_interest_rate/100)/12
	n = duration*12
	if r == 0:
		monthly = principal/n
	else:
		monthly = (principal * (r*((1+r)**n)))/(((1+r)**n)-1)
	return monthly
# Your function for calculating remaining balance goes here
def rasool1(principal, annual_interest_rate, duration, number_of_payment):
	r = (annual_interest_rate/100)/12
	n = duration*12
	p = number_of_payment
	if r == 0:
		rlb = principal*(1-(p/n))
	else:
		rlb = (principal * (((1+r)**n)-((1+r)**p)))/(((1+r)**n)-1)
	return rlb       
# Your main program goes here
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
pardakht_mahane = rasool(principal, annual_interest_rate, duration)
print ("LOAN AMOUNT:",int(principal),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
print ("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(pardakht_mahane))
pardakht_shode = 0
i = 1
while i <= duration:
	pardakht_shode = pardakht_shode + (pardakht_mahane*12)
	baghimande = rasool1(principal, annual_interest_rate, duration, (i*12))
	print("YEAR:",i,"BALANCE:",int(baghimande),"TOTAL PAYMENT",int(pardakht_shode))
	i = i + 1