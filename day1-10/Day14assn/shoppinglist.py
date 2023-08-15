#A program to prompt the user to create a shopping list and calculate total cost

detergents = int(input("Enter cost of Detergent: "))
foodstuff = int(input("Enter cost of Foodstuff: "))
veges = int(input("Enter cost of Veges: "))
electronics = int(input("Enter cost of Electronics: "))
clothing = int(input("Enter cost of Clothing: "))

def cost(a,b,c,d,e):
    totalcost = a + b + c + d + e
    return totalcost
shopping_cost = cost(detergents,foodstuff,veges,electronics,clothing)
print(shopping_cost)


print("Congrats Joyce")

