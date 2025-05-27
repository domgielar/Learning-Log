    
def main():
    loan = float(input("Enter your loan payment per month: "))
    insurance = float(input("Enter your insurance per month: "))
    gas = float(input("Enter your gas per month: "))
    oil = float(input("Enter your oil per month: "))
    tires = float(input("Enter your tires per month: "))
    maintenance = float(input("Enter your maintenance per month: "))

    
    while True:
        monthOrYear = input("Would you like to see monthly or annual expenses, or exit to stop the program").lower().strip()
        if monthOrYear == "monthly":
            monthly(loan, insurance, gas, oil, tires, maintenance)
        elif monthOrYear == "annual":
            annual(loan, insurance, gas, oil, tires, maintenance)
        elif monthOrYear == "exit":
            break

        else:
            print("Invalid function")

def monthly(loan, insurance, gas, oil, tires, maintenance):
    total_monthly = loan + insurance + gas + oil + tires + maintenance
    print(total_monthly)
    return total_monthly


def annual(loan, insurance, gas, oil, tires, maintenance):
    total_annual = (loan + insurance + gas + oil + tires + maintenance)*12
    print(total_annual)
    return total_annual

if __name__ == "__main__":
    main()