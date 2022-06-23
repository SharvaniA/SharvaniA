# Reading and Printing Tables Book.

n = int(input("How many tables do you want: "))
print("Tables Book")
for tablesCounter in range(1, n + 1):
	print("Table Number:", tablesCounter, "\n", "="*15)
	for tableNumber in range(1, 11):
		print("{0:2d} X {1:2d} = {2:3d}" .format(tablesCounter, tableNumber, (tablesCounter * tableNumber)))