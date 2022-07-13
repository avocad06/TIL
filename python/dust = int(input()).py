dust = int(input())
if dust <= 30 :
    print('좋음')
elif 30 < dust <= 80 :
    print ('보통') 
elif 80 < dust <= 150 :
    print ('나쁨')
elif 150 < dust :
    print ('매우 나쁨')