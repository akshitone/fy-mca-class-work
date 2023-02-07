def sum_of_numbers(number_01, *number_02):
    # result = number_01
    # print(number_01)
    # print(number_02)
    # for number in number_02:
    #     result += number
    result = number_01+sum(number_02)
    print(result)


sum_of_numbers(10, 20, 30, 40, 50)
