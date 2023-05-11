print("Welcome to our bank")
trials = 3
userPin = 2415
while trials != 0:
    pin =  int(input("Please enter the Pin number :"))
    if pin != userPin:
        trials -= 1
        print("Wrong Number, You have", trials ," Trials left")
    else:
        desiredOperation = input("D: for Deposit, W:for Withdraw : ")
        if desiredOperation == "D":
            deposit = input("enter the amount you wish to add: ")
            print(deposit, "$ has been added!")
        if desiredOperation == "W":
            withdraw = input("enter the amount you wish to withdraw: ")
            print(withdraw, "$ has been withdrawn!")
    userExit = input("would you like to continue? Y/N : ")
    if userExit == "N":
        print("THANK YOU!, have a great day!")
        break
    else:
        continue