# tuples: ordered, immutable, allows duplicate elements
# can not be changed after its creation

# initilization of tuple
import timeit
import sys
max_details = ("Max", 22, "Norway")
print(max_details)
print(type(max_details))

# optional
john_details = tuple(["John", 23, "Sweden"])
print(john_details)


# max_details = ("John", 23, "Sweden")

print(max_details)

# single value tuple
value_of_pi = (3.14,)
print(type(value_of_pi))

# indexing

# check using in
if 23 in max_details:
    print(True)
# for value in max_details:
#     print(value)

for index in range(len(max_details)):
    print(max_details[index])

# length

# how many elements are there
new_tuple = (10, 20, 30, 20)
print(new_tuple.count(20))

# packing - unpacking
max_details = ("Max", 22, "Norway")
max_name, max_age, max_country = max_details


# separate data
print(max_name)
print(max_age)
print(max_country)

# pointer data
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90)
first_value, *remaining_value, last_value = numbers

print(first_value)
print(remaining_value)
print(last_value)

# size
# max_details_in_list = ["Max", 22, "Norway"]
# print(sys.getsizeof(max_details_in_list))
# print(sys.getsizeof(max_details))

# time
# print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]", number=1000000))
# print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)", number=1000000))
