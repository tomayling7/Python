#1)
gen0b = False
def menu():
    passed = False
    choices = "1 2 3 4 5"
    while not passed:
        choice = input("Please choose an option from the following list:\n1) Set Generation 0 value\n2) Display Generation 0 values\n3) Run the model\n4) Export data\n5) Quit\n")

        if choice not in choices:
            print("Please enter one of the displayed options.")
            continue
        try:
            choice = int(choice)
        except(ValueError):
            print("Please enter one of the displayed options.")
            continue
        passed = True
        print("")
    if choice == 1:
        gen0()
    elif choice == 2:
        display()
    elif choice == 3:
        run()
    elif choice == 4:
        export()
    elif choice == 5:
        if input("Are you sure(Y/N)\n") == 'Y':
            quit()
        else:
            menu()


def gen0():
    global juv, adult, seniles, surv, birth, gen
    while True:
        try:
            juv = int(input("Please enter the number of juveniles to start with: "))
            break
        except(ValueError):
            continue
    while True:
        try:
            adult = int(input("Please enter the number of adults to start with: "))
            break
        except(ValueError):
            continue
    while True:
        try:
            seniles = int(input("Please enter the number of seniles to start with: "))
            break
        except(ValueError):
            continue
    while True:
        try:
            surv = int(input("Please enter the survival rate: "))
            break
        except(ValueError):
            continue
    while True:
        try:
            birth = int(input("Please enter the birth rate: "))
            break
        except(ValueError):
            continue
    while True:
        try:
            gen = int(input("How many generations should be modeled: "))
            break
        except(ValueError):
            continue
    gen0b = True
    print("")
    menu()

def display():
    print("Generation 0 values:\nJuveniles: "+str(juv)+"\nAdults: "+str(adult)+"\nSeniles "+str(seniles)+"\nBirth Rate: "+str(birth)+"\nSurvival Rate: "+str(surv)+"\n")
    menu()
menu()
