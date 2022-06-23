# Program to illustrate Synchronous.

import threading
from evenNumberFunction import evenNumber
from oddNumberProgram import oddNumber

# import evenNumberFunction.py
# def printEven():
# 	for num in range(2,21,2):
# 		print(num)
# def printOdd():
# 	for num in range(1,21,2):
# 		print(num)
def main():
	tasks = [evenNumber(), oddNumber()]
	# print("-"*5)

if __name__ == '__main__':
	main()