def my_sum(*numbers_1):
    
    result = 0
    
    for number in numbers_1:
        result += number
    print(result)

my_sum(10, 10, 10, 30, 60, 240)


def str_to_int(str):

    new_str = int(str)

str_to_int('123456')