# 리스트가지고놀기.py
score = [85,71,77,90]
print(score)

print(score[1:3])
print(score[2:4])
print(score[2:])
print(score[:])
append_score = score 
print(append_score)
append_score.append(98)
print(append_score)
print(score)
very_new_score = append_score.copy()
very_new_score.append(0)
print(very_new_score)
print(append_score)

color = ['green','yello','white']
color.extend(['red','black'])
print(color)