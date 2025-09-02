def fizzbuzz(n):
    for index in range(1, n + 1):  # include n as well
        if (index % 3 == 0) and (index % 5 == 0):
            print("FizzBuzz")
        elif (index % 3 == 0):
            print("Fizz")
        elif (index % 5 == 0):
            print("Buzz")
        else:
            print(index)


n = int(input("Enter a positive integer: "))
fizzbuzz(n)