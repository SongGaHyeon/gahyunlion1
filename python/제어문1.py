# 제어문-분기문
#if(조건):

# 예제1

##85점 이상 PASS,FAIL

'''score= int(input("점수를 입력해 주세요 :"))
if(score>=85):
    print("PASS")
else:
    print("FAIL")'''
#예제
money=int(input('돈 얼마 있어?'))
if money>=5000:
    print("아웃백 가자")
else:
    if (money>=1000):
        print('컵라면 먹자')
    else:
        print("공기밥 가자")
