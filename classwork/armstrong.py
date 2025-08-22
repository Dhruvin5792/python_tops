# for num in range(100, 999):

#     d1 = num // 100
#     d2 = (num // 10) % 10
#     d3 = num % 10

#     if (d1**3 + d2**3 + d3**3) == num:
#         print(num)
sum=0
for num in range(100, 1000):
    rem = num%10
    sum +=rem**3
    num = num // 10




