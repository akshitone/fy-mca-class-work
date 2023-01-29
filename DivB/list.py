# what is list
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers)
# print(type(numbers))

# indexing
print("1st element of the numbers list: ", numbers[0])
print("4th index element of the numbers list: ", numbers[4])
print("length of the numbers list: ", len(numbers))
print("last element of the numbers list: ", numbers[len(numbers)-1])

print("last element of the numbers list (using -1) : ", numbers[-1])
print("second last element of the numbers list (using -2) : ", numbers[-2])

# reverse indexing

# length

# delete element
del numbers[4]
# numbers =

print("numbers list after deleting 4th index element:", numbers)

# list remove
numbers.remove(70)
print("numbers list after removing particular value:", numbers)

# pop
numbers.pop()
numbers.pop()
numbers.pop()
print("numbers list after poping:", numbers)

# clear
# numbers.clear()
# print(numbers)

# append
numbers.append(40)
# numbers.append("Akshit")

print("After appending values into the numbers list:", numbers)


# extend
numbers.extend([50, 60, 70])
print("After extending elements into the list", numbers)

# insert
numbers.insert(2, 100)
print("After inserting value at the 2nd position:", numbers)

numbers.append(True)
numbers.append(5.23)
numbers.append(10)
numbers.append(False)

print(numbers)

print(numbers.index(100))


numbers.sort()
print(numbers)


students_height = [5, 6.2, 4.5, 5.2, 6, 5.11, 6.1, 5.9, 4.11, 5.7]
anuradhas_requirement = 3

students_height.sort()

print(students_height[-anuradhas_requirement])
