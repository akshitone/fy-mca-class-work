# declare
student_name = "Rutvik"
student_roll_no = 63
student_height = 5.11

# type
# print(type(student_name))
# print(type(student_roll_no))
# print(type(student_height))

# address
print("Current Address:", id(student_roll_no))
akshit_roll_no = 63
student_roll_no = 65
print("New Address:", id(student_roll_no))
print("Akshiit Roll No:", id(akshit_roll_no))

# how variable stored in a memory location

# global / local variable
counter = 10


def increment_of_counter():
    global counter
    counter += 1
    print(counter)


increment_of_counter()

print(counter)
