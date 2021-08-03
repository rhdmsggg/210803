#BasicClass.py
#클래스는 여러 개의 변수와 함수들을 모아서 재사용 할 수 있는 기능을 제공
#클래스는 객체를 생성하기 위하여 변수와 함수를 모은 설계도 이며
#이 설계도에 의해 유일한 식별자를 가진 객체들이 생성되고 사용된다.

from _typeshed import Self


class BookReader:
    name = ""
    def read_book(self):
        print(self.name + '님이 책을 읽습니다!')

reader = BookReader()
reader.name = '우진'
print(reader.read_book())

class BookReader():
    name = ''
    def read_book(self):
        print(self.name, '님은 책을 읽는다.')

reader = BookReader()
reader.name = '우진'
print(reader.read_book())

class BookReader():
    def __init__(self, name):
        self.name = name

    def read_book(self):
        print(self.name, '님은 책을 읽는다.')

reader = BookReader('신후')
print(reader.read_book())

#클래스 바로밑에 있는 변수는 클래스 변수라함
#초기화 함수의  self변수는 인스턴스 변수라고 함


