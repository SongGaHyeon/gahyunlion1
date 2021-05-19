#문자열(내장함수)
#덧셈

str="'멋쟁이, 사자'처럼"
print(str[1])
print(str[0])

#[x:y] --> x번째 인덱스부터 y인덱스까지
#len(문자열변수)
#문자열 내에서 특정 문자의 등장 횟수:count('특정문자')
#print(str.count('새'))
#문자열을 (특정 기준으로) 나누기: 문자열 변수.split()
print(str.split("'"))
#find() index()
print(str.index('사'))
