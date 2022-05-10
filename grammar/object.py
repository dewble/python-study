# Class 선언
class Qurd():
    height = 0
    width = 0
    color = 0
    def get_area(self):
        return self.height * self.width

# 객체 생성
qurd1 = Qurd()
qurd2 = Qurd()

# 객체 기능 호출
qurd1.height = 5
qurd1.width = 7

qurd2.height = 2
qurd2.width = 2
print(qurd1.get_area())
print(qurd2.get_area())

