# Program to illustrate Asynchronous.

import threading
import evenAndOddFunction
# from evenAndOddFunction import printEven, printOdd, printEvenAndOddList

def main():
	threading.Thread(target=evenAndOddFunction.printEven).start()
	threading.Thread(target=evenAndOddFunction.printOdd).start()

	# print(evenAndOddFunction.evenAndOddList)


	# printEvenAndOddList()

if __name__ == '__main__':
	main()
	evenAndOddFunction.printEvenAndOddList()



# # Program to illustrate Asynchronous.

# import threading
# from evenAndOddFunction import printEven, printOdd, printEvenAndOddList
# # from evenNumberFunction import printEven
# # from oddNumberProgram import printOdd
# # evenNumbersList = []
# # oddNumbersList = []
# # evenAndOddList = []

# # def printEven():
# # # global evenNumbersList
# # 	for num in range(2,21,2):
# # 		print(num)
# # 		evenNumbersList.append(num)
# # 	print(evenNumbersList)

# # def printOdd():
# # 	# global oddNumbersList
# # 	for num in range(1,21,2):
# # 		print(num)
# # 		oddNumbersList.append(num)
# # 	print(oddNumbersList)

# def main():
# 	threading.Thread(target=printEven).start()
# 	threading.Thread(target=printOdd).start()

# 	printEvenAndOddList()
	
# 	# print(evenNumbersList)
# 	# print(oddNumbersList)
# 	# evenAndOddList.append(evenNumbersList)
# 	# evenAndOddList.append(oddNumbersList)
# 	# print(evenAndOddList)

# if __name__ == '__main__':
# 	main()