# tuples: ordered, immutable, allows duplicate elements
# can not be changed after its creation

# import timeit
# import sys

first_tuple = ("Max", 23, "Canada")
# print(first_tuple)

# print(type(first_tuple))

# initilization of tuple

# optional
second_tuple = tuple(["naruto", "suits", "friends", 100])
# print(second_tuple)

# single value tuple
single_value = ("That's what she said",)
single_value = (100)
# print(type(single_value))

# indexing
print(first_tuple[1])

# check using in
if 23 in first_tuple:
    print("23 is in tuple")
else:
    print("23 is not in tuple")

# length

# how many elements are there
second_tuple = (10, 20, 30, 10, 40, 50, 20, 30, 70)
# second_list = [10, 20, 30, 10, 40, 50, 20, 30, 70]
print(second_tuple.count(20))
# print(second_list.count(20))

# packing - unpacking
mark01, mark02, mark03 = input("Enter three subjects marks:").split(",")
# print(mark01)
# print(mark02)
# print(mark03)

# separate data
name, age, country = ("Max", 23, "Canada")

print(name)
print(age)
print(country)

# pointer data
first, *remaining, last = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(first)
print(last)
print(remaining)

# size

# first_list = ["Max", 23, "Canada"]

# print(sys.getsizeof(first_list))
# print(sys.getsizeof(first_tuple))

# time
# print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]", number=1000000))
# print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)", number=1000000))
