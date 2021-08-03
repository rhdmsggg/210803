#defEX1.py
#def 함수이름():
#   재사용할 소스 코드 블럭

def hello():
    name = input('이름 : ')
    print(name,'님 안녕하세요.')
print(hello())

def hello(name):
    print(name, '님 반갑습니다.')

print(hello('안나'))

def hello(name, greeting):
    print(name, '님',greeting)

print('고은','반가워')

def add_suffix(name):
    return name + '님'

print(add_suffix('냥이'))

name_whit_suffix = add_suffix('냥이')
print(name_whit_suffix)

def sum(a,b):
    return a+b
print(sum(3,5))
print(sum(4545,8745))


