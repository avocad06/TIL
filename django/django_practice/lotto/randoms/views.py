import random
from django.shortcuts import render
# Create your views here.
def index(request):
    foods = [('족발', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxauf77KfBbl4ugiPhBzb8YoGXxvnSoESVsRF1ede2VyFxcFMc-dTthm8pXZZdCECdH5o&usqp=CAU'),
             ('피자', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Supreme_pizza.jpg/800px-Supreme_pizza.jpg'),
             ('짜장면', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/10/26/8f82be9c22ec2f4f9ab25363cc611b141.jpg'),
             ('김치찌개', 'https://i.ytimg.com/vi/PH_-nGRatgo/maxresdefault.jpg'),
             ('떡볶이', 'https://post-phinf.pstatic.net/MjAyMjA2MDhfMTA2/MDAxNjU0Njc3NzEzNDE1.Bz90mjWrQzruuYz49yvCZpiUEkFKQIN9mHvSlpneBFAg.sLRc47q00v_kZbhowDX9fByL61svnRtQGkzo3bJCi3og.PNG/image.png?type=w1200'),]
    
    pick = random.choice(foods)
    
    context = {
        'pick': pick,
    }
    return render(request, 'today-dinner.html', context)

def lotto(request):

    answers = []
    ranks = []
    numbering = random.sample(range(1, 46), 7)
    # numbering = [3, 1, 5, 6, 9, 10, 11,]
    # 보너스 숫자를 제외한 로또 번호
    numbers = numbering[:6]
    bonus = numbering[-1]
    ranking = [{"rank":1, "comment":"1등입니다."},
               {"rank":2, "comment":"2등입니다."},
               {"rank":3, "comment":"3등입니다."},
               {"rank":4, "comment":"4등입니다."},
               {"rank":5, "comment":"5등입니다."},
               {"rank":0, "comment":"낙첨입니다."},]

    lottos = [random.sample(range(1, 46), 6) for _ in range(5)]
    # lottos = [[3, 1, 5, 6, 7, 10, 11,]]

    for lotto in lottos:
        cnt = 0
        rank = 0
        # lottos.append(lotto)
        for num in numbers:
            if num in lotto:
                cnt += 1
        # 등수에 따라 rank 정하기
        if cnt == 6:
            rank = 1
        
        elif cnt == 5:
            if bonus in lotto:
                rank = 2
            
            else:
                rank = 3
        
        elif cnt == 4:
            rank = 4
            
        elif cnt == 3:
            rank = 5
        ranks.append((lotto, rank))
    
    context = {
        'answers' : answers,
        'ranking' : ranking,
        'ranks' : ranks,
        'numbers' : numbers,
        'bonus' : bonus
        # 'values': values,
        }
    
    
    return render(request, 'lotto.html', context)