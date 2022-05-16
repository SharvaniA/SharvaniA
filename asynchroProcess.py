# Program to illustrate Asynchronous.

from multiprocessing import Process
import evenAndOddFunction
# from evenAndOddFunction import printEven, printOdd, printEvenAndOddList

def main():
	evenProcess = Process(target=evenAndOddFunction.printEven())

	oddProcess = Process(target=evenAndOddFunction.printOdd())

	evenProcess.start()
	oddProcess.start()
	evenProcess.join()
	oddProcess.join()

	# print(evenAndOddFunction.evenAndOddList)

if __name__ == '__main__':
	main()
	evenAndOddFunction.printEvenAndOddList()


# # Program to illustrate Asynchronous.

# from multiprocessing import Process
# from evenAndOddFunction import printEven, printOdd, printEvenAndOddList
# # from evenNumberFunction import evenNumber
# # from oddNumberProgram import oddNumber
# # evenNumbersList = []
# # oddNumbersList = []
# # evenAndOddList = []

# # def printEvenNumber():
# # 	for evenNumber in range(2,21,2):
# # 		print(evenNumber)
# # 		evenNumbersList.append(evenNumber)
# # 	print(evenNumbersList)

# # def printOddNumber():
# # 	for oddNumber in range(1,21,2):
# # 		print(oddNumber)
# # 		oddNumbersList.append(oddNumber)
# # 	print(oddNumbersList)

# def main():
# 	evenProcess = Process(target=printEven)

# 	oddProcess = Process(target=printOdd)

# 	evenProcess.start()
# 	oddProcess.start()
# 	evenProcess.join()
# 	oddProcess.join()

# 	printEvenAndOddList()

# 	# print(evenNumbersList)
# 	# print(oddNumbersList)
# 	# evenAndOddList.append(evenNumbersList)
# 	# evenAndOddList.append(oddNumbersList)
# 	# print(evenAndOddList)


# if __name__ == '__main__':
# 	main()