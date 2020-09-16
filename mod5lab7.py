''' the digit of life, you just need to sum all the digits of the date. 
If the result contains more than one digit, 
you have to repeat the addition until you get exactly one digit. 
For example:
1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3'''


def sum_of_digits(n):
    
    s = 0
    while n:
        s += n % 10
        n //= 10

    if s > 9:
        return sum_of_digits(s)

    return s

n = int(input("enter your B.Day in format YYYYMMDD: "))
print(sum_of_digits(n))

#solution 2 using divmod()
# def sum_digits_rec(integ):
#         if integ <= 9:
#             return integ
#         res = sum(divmod(integ, 10)) 
#         return sum_digits(res)
# print(sum_digits_rec(98765678912398))