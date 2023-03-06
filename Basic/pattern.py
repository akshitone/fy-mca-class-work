
for counter_index in range(5):
    for index in range(1, 6-counter_index):
        print(index, end=" ")

    print("* "*counter_index*2, end="")

    for reverse_index in range(5-counter_index, 0, -1):
        print(reverse_index, end=" ")

    print()
