# Reading and printing Multiplication Tables.

tableNumber = int(input("Enter a number to print its Multiplication Table: "))
for number in range(1, 11):
	print("{0:2d} X {1:2d} = {2:3d}" .format(tableNumber, number, (tableNumber*number)))