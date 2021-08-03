#BasicDictionary.py
#딕셔너리 타입이란 전체 항목이 정렬되지 않은 키와 값의 쌍으로 구성된 데이터의 모
#키(key) 값(Value)
programmers = {'Python':13,'Ruby':5,'C++':10}
print(programmers)
print(len(programmers))

print(programmers['Python'])
programmers['Python'] = 44
print(programmers)

print(programmers.keys())
print(list(programmers.keys()))
print(list(programmers.values()))

print('Python' in programmers)
print('C' in programmers)
print('C' not in programmers)

print(programmers.clear())
programmers_list = [('Python',10),('Ruby',5),('C++',10)]
print(programmers_list)
print(dict(programmers_list))
print(programmers['Ruby'])

nums = 4,2,5,7,1,3
print(sorted(nums))
print(nums)
print(sorted(nums), reversed=True)

print(sorted(programmers))
print(sorted(programmers),reversed=True)
print(sorted(programmers.values()))

