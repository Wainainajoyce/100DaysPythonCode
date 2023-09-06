""" 
Write a Python program that simulates a basic ATM (Automated Teller Machine). The program should have the following features:

It should initially ask the user for their account balance (a positive integer).
Then, it should provide a menu with the following options:
Check Balance
Deposit Funds
Withdraw Funds
Quit
The program should continue running until the user selects the "Quit" option.
If the user selects "Check Balance," it should display their current account balance.
If the user selects "Deposit Funds," it should ask for the amount to deposit and update the account balance accordingly.
If the user selects "Withdraw Funds," it should ask for the amount to withdraw. Ensure that the withdrawal amount is not greater than the account balance. If it is, display an error message; otherwise, update the account balance accordingly.
If the user selects an invalid option, display an error message.
After each operation, display the updated account balance.
You can implement this program using functions, loops, and conditional statements. It's a great way to practice user input handling, conditional logic, and basic control flow in Python. Feel free to give it a try, and if you have any questions or need further assistance, please let me know!
"""
accountbalance = int(input("Enter your account balance: "))
balance = 0
deposit = 0
withdrawal_amount = 0



print("""
Menu:
      1)Check balance
      2)Deposit funds
      3)Withdraw funds
      4)Quit
"""
      )

userselection = input("Enter your selection according to the menu: ")

while accountbalance != (accountbalance*-1):
    if userselection == "1":
        accountbalance += accountbalance
        print(accountbalance)
    elif userselection == "2":
        deposit = int(input("Enter your deposit amount: "))
        accountbalance == deposit + accountbalance
        print(accountbalance)
    elif userselection == "3":
        withdrawal_amount == int(input("Enter amount you want to withdraw: "))
        accountbalance == accountbalance - withdrawal_amount
    elif userselection == "4":
        break
else:
    print("Sorry,You do not have sufficient funds in your account to continue with the operation")
        


