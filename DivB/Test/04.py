numbers = [10, 30, 20, 30, 20, 30]  # true

occurance = dict()

for number in numbers:
    if number not in occurance:
        occurance[number] = 1
    else:
        occurance[number] += 1

print(occurance)

number_of_occurance = list(occurance.values())
print(number_of_occurance)

output = []
result = True

for number in number_of_occurance:
    if number not in output:
        output.append(number)
    else:
        result = False
        break

print(result)
