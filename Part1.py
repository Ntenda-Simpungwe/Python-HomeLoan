print("Hi there. I'm Ntenda, your home loan digital assistant :D ...\n")

sGross = input("Enter you Gross Salary: ")
sGross = sGross.strip('R')
fGross = float(sGross)

maxInstallment = round(fGross*0.3,2)

credScore = int(input("Now enter your credit score (0-1200): "))

sPrice = input("What is the purchase price of your property?: ")
sPrice = sPrice.strip('R')
pPrice = float(sPrice)

appStatus = 'Granted'

if credScore >= 800 :
    lPercent = '110%'
    deposit = 0.0
elif credScore >= 750 :
    lPercent = '100%'
    deposit = 0.0
elif credScore >= 700 :
    lPercent = '95%'
    deposit = pPrice*0.05
elif credScore >= 650 :
    lPercent = '90%'
    deposit = pPrice*0.1
elif credScore >= 600 :
    lPercent = '85%'
    deposit = pPrice*0.15
elif credScore >= 550 :
    lPercent = '80%'
    deposit = pPrice*0.2
else :
    lPercent = 'Declined'
    appStatus = 'Declined'
    deposit = 0.0


monthInstallment = round(pPrice*0.00785,2)

if monthInstallment > maxInstallment:
    appStatus = 'Declined'


print("\nThank you for your home loan application.\n")
print("Loan Application Status: ",appStatus)
print("Maximum Installment Amount: R"+str(maxInstallment))
print("Percentage Home Loan Granted: ",lPercent)
print("Deposit Required: R"+str(deposit))
print("Monthly Installment: R"+str(monthInstallment))

wait = input("Press Enter to continue...")

