input = [45, 67, 32, 87, 92, 100, 20]
# index = 0

# while index < len(input)-1:
#     input[index], input[index + 1] = input[index + 1], input[index]
#     index += 2

for index in range(0, len(input)-1, 2):
    input[index], input[index + 1] = input[index + 1], input[index]

print(input)
