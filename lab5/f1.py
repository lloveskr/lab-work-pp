 #1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if(2 * chickens + 4 * rabbits) == numlegs: return chickens, rabbits
    return None

#4
def is_prime(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True
def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

#5
from itertools import permutations
def string_permutations(input_string):
    perms = [''.join(p) for p in permutations(input_string)]
    return perms

#6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3: return True
    return False

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]: code.pop(0)
        if len(code) == 0: return True
    return False

#9
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

#10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list: unique_list.append(item)
    return unique_list

#11
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#13
import random
def guess_the_num():
    name = input("Your name: ")
    print(f"{name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses_taken += 1
        if guess < secret_number: print("too low.")
        elif guess > secret_number: print("too high.")
        else: print(f"{name}, you guessed my number in {guesses_taken} gueses!")
        break

#14
if __name__ == "__main__":
    print(grams_to_ounces(100))
    print(fahrenheit_to_celsius(68))
    print(solve(35, 94))
    print(filter_prime([2, 3, 5, 7, 10, 11, 13, 15]))
    print(string_permutations("abc"))
    print(reverse_words("We are ready"))
    print(has_33([1, 3, 3]))
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(sphere_volume(3))
    print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
    print(is_palindrome("madam"))
    histogram([4, 9, 7])
    guess_the_num()