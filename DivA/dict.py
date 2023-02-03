# Dictionary: Key-value pair, unordered, mutable

# initialize 01
user_details = {
    "name": "Mona darling",
    "age": 22,
    "area": "Wednesday"
}

# print(user_details)

# user_details_list = ["Mona", 22, "Wed"]

# print(user_details["age"])

# initialize 02

# add new key value pair
user_details["amt"] = 6000

print(user_details)


# new value to key
user_details["name"] = "Ocean"

print(user_details)

# delete

del user_details["amt"]
print("after deletion:", user_details)

# delete by pop
age = user_details.pop("age")
print(age)
print(user_details)

# popitem
user_details.popitem()
print(user_details)

# check key is in dict
# print(user_details["amount"])

key = "amount"

if key in user_details:
    print(user_details[key])
else:
    print("Key not found")

# retrive
for key in user_details:
    # print(user_details[key])
    print(key)

# keys
for key in user_details.keys():
    # print(user_details[key])
    print(key)

# values
for value in user_details.values():
    print(value)

# items
for key, value in user_details.items():
    print(key, value)

# updates

update_details = {"name": "Ocean", "age": 27, "gender": "Female"}
user_details.update(update_details)

# user_details["name"] = "Ocean"
# user_details["age"] = 27
# user_details["gender"] = "Female"

print(user_details)
