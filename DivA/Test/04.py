numbers = [-3, 1, -1, -3, -1, 1, -3, 2, -1, -3]

dict_number = dict()

for number in numbers:
    if number not in dict_number:
        dict_number[number] = 1
    else:
        dict_number[number] += 1

print(dict_number)

occurance = list(dict_number.values())
print(occurance)

check_for_repeat = dict()

no_repeat = True

for number in occurance:
    if number not in check_for_repeat:
        check_for_repeat[number] = 1
    else:
        no_repeat = False

print(no_repeat)
