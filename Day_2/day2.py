# custom error for tipping option validation
class InvalidTipOption(Exception):
    def __init__(self, tip_option: str):
        self.tip_option = tip_option
        super().__init__(f'Invalid tipping option: "{tip_option}". It has to be "p" or "a".')


print("Welcome to the tip calculator!")
init_bill = int(input("What was the total bill? (PLN) "))
tip_option = input("How much tip would you like to give – percentage (p) or a specific amount (a)? ")

if tip_option == "p":
        tip_percent = int(input("What percentage of the bill do you want to tip? (%) "))
        tip = (tip_percent / 100) * init_bill
        print("You will tip " + str(tip) + " PLN.")
elif tip_option == "a":
    tip = int(input("How much do you want to tip? (PLN) "))
    tip_percent = tip / init_bill * 100
    print("You will tip " + str(tip_percent) + " %.")
else:
    raise InvalidTipOption(tip_option)

final_bill = init_bill + tip
people_nb = int(input("How many people to split the bill? "))
final_bill_per_person = final_bill / people_nb
print("Each person should pay: " + str(final_bill_per_person) + " PLN.")
