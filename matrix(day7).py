matrix = [
    [1,2,3],#Remember the commas Joyce, They are essential
    [4,5,6],
    [7,8,9]
]
print(matrix[2][1])#Each row is an item and each item in a row is an item hence the for loop is a nested loop

for row in matrix:
    for item in row:
        print(item)

matrix[2][1]=20
print(matrix[2][1])#Changing the value of item in the matrix

print("Congrats Joyce")