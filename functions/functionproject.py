#list of variables in input
#Income
salary = int(input("Enter your salary income: "))
side_hustle = int(input("Enter your side_hustle income: "))

#Expenses
utilitybills = int(input("Enter your bills cost: "))
grocery = int(input("Enter your grocery cost: "))
allowances = int(input("Enter your allowances cost: "))

#Goals
goal1 = "improve coding setup"
goal2 = "vacation"
goal3 = "Start a business"
goal4 = "Education bills"
mygoal = ""

#If elif for the goals
if (mygoal == goal1):
    newincome = salary + side_hustle
    if (newincome  >= 40000):
       expense_net = newincome * 0.5
       allowance_net = newincome * 0.3
       savings_net = newincome * 0.2
       print(expense_net)
       print(allowance_net)
       print(savings_net)
    elif(newincome >= 50000):
          expense_net = newincome * 0.3
          allowance_net = newincome * 0.3
          savings_net = newincome * 0.3
          leisure_net = newincome * 0.1
          print(expense_net)
          print(allowance_net)
          print(savings_net)
          print(leisure_net)

        
    else:
        print("Sorry,your income category is not listed")
elif(mygoal == goal2):
       newincome = salary + side_hustle
       expense_net = newincome * 0.5
       allowance_net = newincome * 0.3
       savings_net = newincome * 0.2
       print(expense_net)
       print(allowance_net)
       print(savings_net)





