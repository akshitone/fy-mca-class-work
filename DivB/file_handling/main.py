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

    # print(test_file.closed)
    # test_data = test_file.readline()
    # print(test_data, end="")

    # test_file.seek(0)

    # test_data = test_file.readline()
    # print(test_data, end="")

    # test_data = test_file.read(10)
    # print(test_data, end="")

    # test_file.seek(0)

    # test_data = test_file.read(10)
    # print(test_data)
    pass

# print(test_file.closed)


with open('test.txt', 'r') as read_test_file:  # open file in read mode
    with open('test_copy.txt', 'w') as write_test_file:  # open file in write mode
        test_data = read_test_file.read()  # read file and store it in test_data
        write_test_file.write(test_data)


# 1 2 3 4 5 6 7 8 9 10 - 10000 lines

# 4 6 8


# 101,akshit,10000,
# 102,viral,20000,
# 103,rajan,30000,

# rollno: 101
# name: akshit
# salary: 10000

# rollno: 102
