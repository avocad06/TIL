a=int(input())
b=int(input())
c=int(input())
num = a*b*c

dic={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
while 1:
    n1 = num % 10
    if n1 not in dic:
        dic[n1] =1
    else:
        dic[n1] += 1
    num = num//10
    if num == 0:
        break
for number in dic:
    print(dic[number])