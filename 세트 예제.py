#세트 예제.py

langeuages = set()  #세트 변수 초기화
langeuages.add("python")    #항목 최초 추가
langeuages.add("java")      #항목 최초 추가
print(langeuages)       #세트 변수 값 1차 확인
langeuages.add("python")    #기존 항목 추가 재시도
print(langeuages)   #세트 변수 값 2차 확인(중복 유무 확인)