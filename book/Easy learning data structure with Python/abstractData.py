# 추상 자료형은 개념의 일종이며 이를 표현하는 방법으로는
# 인터페이스 < 추상 클래스 < 구체 클래스 이며 각 구현 상태는 0% < 1~99% < 100%이다
class human0:
    def __init__(self, sex, age, name):
        self.sex = sex
        self.age = age
        self.name = name
    # 생성자가 있으므로 추상 클래스에 해당된다
    # 그렇다고 생성자가 없다고 인터페이스는 아니다
    
    def say(self):pass
    def waving(self):pass
    # 추상 클래스처럼 보이지만 구체화 되어 있는 것이다
    # 파이썬은 인터페이스가 굳이 예약어로 만들어져 있지 않아서 abc를 선언해줘야 됨
    # 그래서 human0는 인터페이스가 아니며 abc를 해줘야 추상 클래스가 되고
    # human(abc)를 해줘도 @abstractmethod가 없으면 추상 메소드를 작성하지 못해서
    # 추상 클래스라고 보기 어렵다