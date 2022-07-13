# treeHit=0
# while treeHit<10:  # treeHit이 10보다 작은 동안에
    #treeHit=treeHit+1 # while문 안의 문장을 계속 수행, treeHit의 값을 1씩 증가시킴. tree+=1
    #print("나무를 %d번 찍었습니다"%treeHit)
    #if treeHit == 10 :
    #    print("나무 넘어갑니다.")
    
coffee = 10
while True:
    money=int(input("돈을 넣어 주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다."%(money-300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break