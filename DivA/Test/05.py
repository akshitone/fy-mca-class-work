input = [1, 2, 3, 4, 5]
sum = 5
dict_sum = dict()

for number in input:
    remaining = abs(sum - number)
    if remaining in input:
        dict_sum[number] = remaining
        input.remove(remaining)

print(dict_sum)

new_values = [[key, value] for key, value in dict_sum.items()]
print(new_values)
