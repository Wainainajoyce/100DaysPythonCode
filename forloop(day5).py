#A for loop is used to iterate over a string, a list a couple of times.
#It contains a loop variable whereby the loop variable holds a different item per iteration.
grade = [18,20,19,30,45,12]
for age in grade:
    print(age)

for names in ["mercy", "kiptoo", "korir" , "mary"]:
    print(names)

for item in range(10):
    print(item)
for number in range(4,9):
    print(number)

for numbers in range(2,8,2):#the 2 is a step
    print(numbers)

#Exercise to calculate total cost of items in a shopping cart
prices = [10,20,30]
total = 0
for shopping_cost in prices:
    total += shopping_cost
print(f"Total: {total}")

#A program to list coordinates
for x in range(5):
    for y in range (4):
        print(f"({x},{y})")

print("congratulations Joyce")