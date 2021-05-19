li=[3,4,'배가',4,'고파요',5,1,2,2,2]
#인덱싱 슬라이싱
print(li[0:3])

#리스트의 길이를 구해주는 함수: len(변수)
print(len(li))
#리스트의 원소 오름차순 정렬해주는 함수: sort()

#print(li.sort()) 정렬된 리스트 반환하지 않음
#print(li) 해줘야함
#리스트 내 특정 원소 인덱스 반환:.index()
print(li.index('움칫'))
print(li.count(2))