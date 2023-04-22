# def check_3_digits(number):
#     return number in range(100, 1000)


# result = check_3_digits(45)
# print(result)

# def check_3_digits(number):
#     return number in range(100, 1000)


# sum = 26+31
# result = check_3_digits(sum)
# print(result)


# number of series to check

def check_3_digits(list1):
    three_digit_list = []
    for n in list1:
        if n in range(100, 1000):
            three_digit_list.append(n)
        else:
            pass
    return three_digit_list


result = check_3_digits([555, 99, 6000])
print(result)
