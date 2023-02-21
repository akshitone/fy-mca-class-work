input = [45, 67, 32, 87, 92]
length = len(input)
index = 0

while True:
    if index + 1 < length:
        input[index], input[index + 1] = input[index + 1], input[index]
        index += 2
    else:
        break

print(input)
