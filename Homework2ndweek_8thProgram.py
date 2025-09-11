prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# a) Middle five primes
middle_five = prime_numbers[2:7]
print("Middle five primes:", middle_five)

# b) Every second prime
every_second = prime_numbers[::2]
print("Every second prime:", every_second)

# c) Last three primes (negative indexing)
last_three = prime_numbers[-3:]
print("Last three primes:", last_three)

# d) Reverse the list
reversed_list = prime_numbers[::-1]
print("Reversed list:", reversed_list)

# e) Sort in descending order
descending = sorted(prime_numbers, reverse=True)
print("Sorted in descending order:", descending)
