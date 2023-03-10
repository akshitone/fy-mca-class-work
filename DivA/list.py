# what is list
# list: ordered, mutable, allows duplicate elements
numbers = [10, 20, 30, 40, 50, 60]
# print(numbers)

# for number in numbers:
#     print(number)

# indexing
# print(numbers[0])
# print(numbers[2])
# print(numbers[3])

# reverse indexing
last_element_index = len(numbers)-1
# print("Last element index:", last_element_index)
# print("Last element:", numbers[last_element_index])

# print("Last element:", numbers[-1])

# length
# print(len(numbers))

# delete element
# print("Before delete:", numbers)
# del numbers[2]
# print("After delete:", numbers)

# list remove
# numbers.remove(40)
# print("After deleting value 40:", numbers)


# pop
# print("Before pop:", numbers)
# deleted_value = numbers.pop()
# print("Deleted value:", deleted_value)
# print("After pop:", numbers)

# clear
# numbers.clear()
# print(numbers)

# append
# print("Before append:", numbers)
# numbers.append(100)
# numbers.append(200)
# numbers.append(300)
# print("After append:", numbers)

# extend
# numbers.extend([1000, 2000, 3000])
# print("After extend:", numbers)

# insert
# numbers.insert(2, 500)
# print(numbers)

# multiply elements
# zeros = [0]*10
# print(zeros)

# numbers.reverse()
# print(numbers)

# copy list
# print(numbers)
copied_numbers = numbers.copy()

# print("Copied numbers:", copied_numbers)
# print("Original numbers:", numbers)

numbers.append(1000)
# print("Original numbers:", numbers)
# print("Copied numbers:", copied_numbers)

# append two list
# new_numbers = numbers + copied_numbers
numbers.extend(copied_numbers)
# print("New numbers:", numbers)

# one liner
square_list = list()
# square_list = []

for number in range(1, 10):
    result = number*number
    square_list.append(result)

print(square_list)

mutliply_by_2 = [number*number for number in range(1, 10)]
print(mutliply_by_2)


# slicing


# for value in enumerate(numbers):
#     print(value)
# if index == 3:
#     print(number)
