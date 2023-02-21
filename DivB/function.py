# declaration
def function_name():
    pass


# no arg, no return
def morning_wish():
    print("Good morning")


morning_wish()


# no arg, return
def afternoon_wish():
    return "Good afternoon"


wish = afternoon_wish()
print(wish)

# arg, no return


def evening_wish(name):
    print(f"Good evening, {name}")


evening_wish("John Doe")

# arg, return


def night_wish(name):
    return f"Good night, {name}"


wish = night_wish("John Doe")
print(wish)
