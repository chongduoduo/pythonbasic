##this is a program to learn how does generator work
import math

def is_prime(number):
    """judge a number if it is a prime or not"""
    if number > 1:  ## the number should be > 1
        if number == 2:
            return True  ## if the number == 2, return the True, and jump out the function
        if number % 2 == 0:
            return False   ## if the number can be divided by 2, return a False and jump out the function
        for current in range(3, int(math.sqrt(number)+1), 2):
            if number % current == 0:
                return False  ## if the number can be devided by other numbers except 2, return a False and jump out the function
        return True ## if the number(>1) isn't 2, can't be devided by 2 and other numbers, it means that it's a prime, return True and jump out the function
	return False  ## if the number <= 1, return a False

def get_primes(input_list):
    result_list = list()
    for element in input_list: ##draw out every element of input list.
        if is_prime(element):
            result_list.append() ## if the element is prime, add it into the result list. Or throw it away.
    return result_list ## finally, return a long and clean list.

def get_primes_gen(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_number_10():
    total = 2
    for next_prime in get_primes_gen(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

solve_number_10()