#Basicfor.py
#단일 for 문과 함꼐 리스트 만들기
squares = []
for n in range(10):
    squares.append( n**2)

print(squares)

new_squares = [n**2 for n in range(10)] #for문과 함꼐 리스트선언
print(new_squares)

#중첩 for 문, if 문과 함께 리스트 만들기
items = '가위','바위','보'  #r가위바위보 튜플로 저장
results = []        #결과 저장을 위한 리스트생성
for a in items:
    for b in items:
        if a != b:
            results.append((a,b))   #튜플 괄호
print(results)

new_results = [(a,b) for a in items for b in items if a!= b]
print(new_results)

#for문, if문과 함께 새트 타입 만들기
a = set()   #set() 초기화
for x in 'avracadabra':
    if x not in 'abc':
        a.add(x)
print(a)

new_a = { x for in 'abracadabra' if x not in 'abracadabra'}
print(new_a)

#for문과 함께 딕셔너리 타입 만들기
squares = {}    #빈 딕셔너리 생성
for x in (2,4,6):   #for문 루프 시작
    squares[x] = x**2   #키는 x,값은 x제곱 항목 추가
 
print(squares)

squares = {x:x**2 for x in (2,4,6)} #딕셔너리 생성
print(squares)