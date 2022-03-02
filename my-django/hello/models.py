class Quiz01Calculator:
    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def res(self):
        if self.opcode == "+":
            res = f'{calc.num1} {calc.opcode} {calc.num2} = {calc.add()}'
        elif self.opcode == "-":
            res = f'{calc.num1} {calc.opcode} {calc.num2} = {calc.sub()}'
        elif self.opcode == "*":
            res = f'{calc.num1} {calc.opcode} {calc.num2} = {calc.mul()}'
        elif self.opcode == "/":
            res = f'{calc.num1} {calc.opcode} {calc.num2} = {calc.div()}'
        else:
            res = "잘못입력하였습니다."
        return res
class Quiz02Bmi:
    def __init__(self,name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def meter(self):
        return self.height / 100

    def sum(self):
        b = Quiz02Bmi(self.name, self.weight, self.height)
        return self.weight / (b.meter() * b.meter())

    def res(self):
        b = Quiz02Bmi(self.name, self.weight, self.height)
        if b.sum() < 18.5:
            res = "저체중"
        elif 18.5 <= b.sum() and bmi.sum() < 23:
            res = "정상"
        elif 23 <= b.sum() and bmi.sum() < 25:
            res = "과체중"
        elif 25 <= b.sum():
            res = "비만"
        else:
            res = "잘못입력하였습니다."
        return res
class Quiz03Grade:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def sum(self):
        return self.kor + self.eng + self.math
    def avg(self):
        return (self.kor + self.eng + self.math) / 3

class Quiz04GradeAuto:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def sum(self):
        return self.kor + self.eng + self.math
    def avg(self):
        return (self.kor + self.eng + self.math) / 3
    def getGrade(self):
        pass
    def chkPass(self):
        pass

class Dice:
    def __int__(self):
        pass

if __name__ == '__main__':
    while 1:
        menu = input("0.Exit 1.계산기 (+, -, *, /) 2.BMI 3.성적표 \n입력 : ")
        if menu == "0":
            break
        elif menu == "1":
            calc = Quiz01Calculator(int(input("첫번째 수 : ")),int(input("두번째 수 : ")),input("연산자 입력 : "))
            print(calc.res())
            break
        elif menu == "2":
            bmi = Quiz02Bmi(input("이름 : "), float(input("몸무게 입력 : ")),float(input("키(cm) 입력 : ")))
            print(f'{bmi.name} 님의 BMI 지수 : {bmi.sum():.2f} \n{bmi.name} 님은 {bmi.res()} 입니다.')
            break
        elif menu == "3":
            grade = Quiz03Grade(input("이름 : "), int(input("국어 점수 : ")), int(input("영어 점수 : ")),int(input("수학 점수 : ")))
            print(f'이름 : {grade.name} \n국어 점수 : {grade.kor} \n영어 점수 : {grade.eng} \n수학 점수 : {grade.math} '
                  f'\n종합점수 : {grade.sum()} \n평균 : {grade.avg()}')
            break
        elif menu == "4":
            pass
        else:
            print("잘못 입력하였습니다.")