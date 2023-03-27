try:
    phone_number = int(input("Enter your phone number: "))
    # user_name = i_dont_know
except ValueError as error:
    print("Please enter a valid phone number")
except NameError as error:
    print("Please check your code once....")
except Exception as error:
    print("Please check your code")
else:
    print("Successfully entered phone number")
finally:
    print("Welcome to MIT")

# print("That's what she said!!")
