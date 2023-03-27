
try:
    names = int(input("Enter roll no: "))
    names = user
    print(names)

except ValueError as err:
    print(err)
    print("Please enter proper roll no")

# except NameError:
#     print("You have declared unnecessary variables")

except Exception as err:
    print(err)

else:
    print("Something went wrong")

finally:
    print("Finally something went wrong...")
