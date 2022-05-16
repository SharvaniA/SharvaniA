
# evenNumbersList = []
# oddNumbersList = []
evenAndOddList = []

def printEven():
	# global evenNumbersList
	for evenNumber in range(2,21,2):
		print(evenNumber)
		evenAndOddList.append(evenNumber)
	print(evenAndOddList)

def printOdd():
	# global oddNumbersList
	for oddNumber in range(1,21,2):
		print(oddNumber)
		evenAndOddList.append(oddNumber)
	print(evenAndOddList)

def printEvenAndOddList():
# 	print(evenNumbersList)
# 	print(oddNumbersList)
# 	evenAndOddList.append(evenNumbersList)
# 	evenAndOddList.append(oddNumbersList)
	print(evenAndOddList)