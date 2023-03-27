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

# text_file = open('test.txt', 'r')
# print(text_file.read())
# text_file.close()

# with open('test.txt', 'r') as text_file:
# text_data = text_file.read() # will real all content at once
# print(text_data)

# will real all content at once and convert it to the list
# text_data = text_file.readlines()
# print(text_data)

# for data in text_data:
#     print(data)

# text_data = text_file.readline()
# print(text_data, end='')

# text_data = text_file.read(15)
# print(text_data)

# moving the pointer
# text_file.seek(0)

# text_data = text_file.read(10)
# print(text_data, end='')

# retrieving the pointer
# print(text_file.tell())

# pass


with open('test.txt', 'r') as read_file:
    with open('test_copy.txt', 'w') as write_file:
        file_data = read_file.read()
        write_file.write(file_data)


# 101,akshit,10000,
# 102,viral,20000,
# 103,rajan,30000,

# rollno: 101
# name: akshit
# salary: 10000

# rollno: 102


with open('test.txt', 'r') as read_file:
    test_data = read_file.read()
    second_line_index = test_data.index('\n')+1
    # print(second_line_index)
    read_file.seek(second_line_index)
    data = read_file.read()
    print(data)
