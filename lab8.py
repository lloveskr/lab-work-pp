from functools import reduce
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)

num_list = [2, 3, 4, 5]
result = multiply_list(num_list)
print("Multiplication of numbers in the list:", result)


def count_case_letters(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count
test_string = "Hello World"
upper, lower = count_case_letters(test_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)



def is_palindrome(input_string):
    return input_string == input_string[::-1]
test_string = "madam"
if is_palindrome(test_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


import time
from math import sqrt
def calculate_sqrt_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = sqrt(number)
    return result
input_number = 25100
wait_time = 2123
result_sqrt = calculate_sqrt_after_milliseconds(input_number, wait_time)
print(f"Square root of {input_number} after {wait_time} milliseconds is {result_sqrt}")


def all_elements_true(input_tuple):
    return all(input_tuple)
test_tuple_1 = (True, True, True)
test_tuple_2 = (True, False, True)
print(all_elements_true(test_tuple_1))  
print(all_elements_true(test_tuple_2))

