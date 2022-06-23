# Reading and Printing series [1, 4, 27, 256,...]

print("The first", (seriesCount := int(input("How many numbers do you want to print in a series of powers of their number? "))), "terms of the series of the powers of the number are: ", (series := [number**number for number in range(1, seriesCount + 1)]))
