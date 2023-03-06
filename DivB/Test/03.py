input = [3, 4, 10, 1, 10, 8, 2, 4, 1, 8, 3]
output = []

for number in input:
    if number not in output:
        output.append(number)
    else:
        output.remove(number)

print(output)
