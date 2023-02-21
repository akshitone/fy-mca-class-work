input = [3, 4, 1, 8, 2, 4, 1, 8, 3]
output = []

for number in input:
    if number in output:
        output.remove(number)
    else:
        output.append(number)

print(output)
