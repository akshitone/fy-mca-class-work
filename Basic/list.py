# akshit_name = "akshit"
# fawziya_name = "fawziya"
# vatsal_name = "vatsal"

# print(akshit_name + " " + fawziya_name + " " + vatsal_name)

# first_list = [1, 2, 3]

students_name = ["akshit", "fawziya", "vatsal"]
# print(students_name)

# for name in students_name:
#     print(name)

students_name.append("shreyang")
students_name.extend(["aditya", "aditi"])
students_name.sort()
students_name.insert(3, "chaitali")
# students_name.remove("aditya")
students_name.append("rana")

print(students_name[0])
print(students_name)
print(len(students_name))
print(students_name[len(students_name)-1])
print(students_name[-2])
