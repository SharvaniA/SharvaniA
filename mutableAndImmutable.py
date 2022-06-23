# Demostrating Mutable and Immutable objects.

#Mutable

# 1. List

# studentNames = ['Keerthi', 'Anusha', 'Kulsum', 'Mani', 'Hari']
# for studentName in studentNames:
# 	print(studentName, end = ', ')
# print(hex(id(studentNames)))
# studentNames.append('Sharvani')
# for studentName in studentNames:
# 	print(studentName, end = ', ')
# print(hex(id(studentNames)))

# 2. Tuples

# namesInTuple = ('Sharvani', 'Keerthi', 'Anusha')
# # namesInTuples[0] = 'Kulsum'
# print(hex(id(namesInTuple)))
# namesInTuple += 'Kulsum',
# print(namesInTuple)
# print(hex(id(namesInTuple)))


# 3. Numbers

# number1 = 9
# print(number1)
# print(hex(id(number1)))
# number2 = 9
# print(number2)
# print(hex(id(number2)))

# 4. Sets

# set of integers
# numbersSet = {1, 2, 3}
# print(numbersSet)
# print(hex(id(numbersSet)))
# numbersSet.add(5)
# print(numbersSet)
# numbersSet.discard(5)
# print(numbersSet)

# 5. Dictioniers

dictionary1 = {1: 'Keerthi', 2: 'Anusha', }
dictionaryToBeAdded = {3: 'Sharvani'}
 
# Dictionary before Updation
print("Original Dictionary:")
print(dictionary1)
 
# update the value of key 3
dictionary1.update(dictionaryToBeAdded)
print("Dictionary after updation:")
print(dictionary1)