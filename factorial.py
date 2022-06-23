# Reading and Printing factorial of a number.

product = 1
for number in range(1, (int(input("Enter a number to find its factorial: "))) + 1):
	product *= number
print(product)