num = int(input("Enter your number :- "))
binary = 0
temp = 1

while num > 0:
    rem = num % 2
    binary += rem * temp
    num //= 2
    temp *= 10

print("Binary number is:", binary)
