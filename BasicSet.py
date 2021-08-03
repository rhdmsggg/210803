#BasicSet.py
languages = {'C++','JAVA','Python','Python'}
print(languages)

color = set()
print(color)

color_list = []
print(color_list)

color = set()
color.add('red')
color.add('blue')
color.add('gray')
print(color)

color.add('red')
print(color)

print('red' in color)
print('black' in color)

color.remove('red')
print(color)

color.discard('black')
print(color)
color.discard('blue')
print(color)

print(color.pop())

print(color)


