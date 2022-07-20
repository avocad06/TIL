number = 12
number_s = number%10


while number > 10:
    number = number//10
    number_s += number%10
    
print(number_s)

