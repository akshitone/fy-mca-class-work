# declare
student_name = "Harvey Specter"
student_roll_no = 27
student_height = 6.2

# type
print(student_name, type(student_name))
print(student_roll_no, type(student_roll_no))
print(student_height, type(student_height))

# address
age = 23
new_age = 23
print("current address:", id(age))


age = 25
print("new address:", id(age))
print("new age address:", id(new_age))

# how variable stored in a memory location

# global / local variable
counter = 0


def increment_counter():
    global counter
    # counter = 10
    counter += 1
    print("local counter: ", counter)


increment_counter()

print("global counter: ", counter)


student_name = "Akshit"
