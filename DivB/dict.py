# Dictionary: Key-value pair, unordered, mutable
# user_details = [
#     ["Vatsal", 23, "Light of red"],
#     ["Shadow of blue", 25, "Shreyang"]
# ]

# initialize 01
user_details = {
    "name": "Vatsal",
    "age": 22,
    "area": "Light of red"
}

# new_data = [
#     {"name": "Vatsal", "age": 22, "area": "Light of red"},
#     {"name": "Vatsal", "age": 22, "area": "Light of red"},
# ]

# for data in new_data:
#     print(data["name"], data["age"], data["area"])


# initialize 02
# user_details = dict(name="Vatsal", age=22, area="Light of red")

# print(user_details)
# print(type(user_details))

# add new key value pair
user_details["amt"] = 80000
# print(user_details)

# new value to key
# user_details["name"] = "Shreyang"
# print(user_details)

# delete
# del user_details["amt"]
# print(user_details)

# delete by pop
# deleted_value = user_details.pop("age")
# print(deleted_value)

print(user_details)

# popitem
# user_details.popitem()
# print(user_details)

# check key is in dict
if "lastname" in user_details:
    print("true")
else:
    print("false")

# retrive
for key in user_details:
    print(key, user_details[key])

# keys
for key in user_details.keys():
    print(key, user_details[key])

# values
for value in user_details.values():
    print(value)

# items
for key, value in user_details.items():
    print(key, value)
    # print(data)

# updates

update_details = {"name": "Shreyang", "age": 21, "gender": "Male"}

# user_details["name"] = update_details["name"]

user_details.update(update_details)
print(user_details)
