#list.py
score = [85,92,88,71]
print(score)
score.append(90)    #추가
print(score)
score.insert(3,77)  #지정자리에 추가
print(score)
score.remove(88)    #삭제
print(score)
score.pop(1)    #특정위치 항목 빼내기
print(score)
score.sort()    #오름차순으로 정렬
print(score)
score.sort(reverse=True)    #내림차순 정렬
print(score)
score.clear()   #리스트 초기화
print(score)