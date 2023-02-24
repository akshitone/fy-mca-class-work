# age = int(input("Enter your age: "))
# while age < 0 and age > 100:
#     print("Inap")
#     age = int(input("Enter your age: "))


while True:
    age = int(input("Enter your age: "))
    if age > 0 and age < 100:
        break
    else:
        print("Inappropriate")
