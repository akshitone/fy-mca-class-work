# open file
# default mode
# file name
# file close
# file mode

# with
# check file is closed
# read file
# read lines
# read line
# specific characters
# seek

# write file
# seek


# test_file = open('test.txt')
# test_data = test_file.read()
# print(test_file.name)

# print(test_file.closed)

# test_file.close()


with open('test.txt', 'r') as test_file:
    # test_data = test_file.read()
    # print(test_data)

    # test_data = test_file.readlines()
    # print(test_data)

    # for user in test_data:
    #     print(user.split(','))

    test_data = test_file.readline()
    print(test_data, end="")

    test_data = test_file.readline()
    print(test_data, end="")
