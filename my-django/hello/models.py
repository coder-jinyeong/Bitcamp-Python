import random

def main():
    while 1:
        menu = input("0.Exit 1.계산기 2.BMI 3.성적표 4. 5.주사위 6.랜덤숫자 7.랜덤이름추출 "
                     "8.Rps 9.GetPrime 10.LeapYear\n입력 : ")
        if menu == "0":
            break
        elif menu == "1":
            calc = Quiz01Calculator(int(input("첫번째 수 : ")),int(input("두번째 수 : ")),input("연산자 입력(+, -, *, /) : "))
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
            print()
            break;
        elif menu == "5":
            print(f'주사위 나온 값 :  {Quiz05Dice.num()}')
        elif menu == "6":
            rd = Quiz06RandomGenerator(int(input("원하는 시작 범위 : ")),int(input("원하는 끝나는 범위 :" )))
            print(f'{rd.num1} 부터 {rd.num2} 까지 중 나온 랜덤 숫자 : {rd.rand()}')
        elif menu == "7":
            ch = Quiz07RandomChoice()
            print(f'803호에서 랜덤으로 추출한 사람 : {ch.choice()}')
        elif menu == "8":
            break
        else:
            print("잘못 입력하였습니다.")

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
            res = f'{self.num1} {self.opcode} {self.num2} = {Quiz01Calculator.add(self)}'
        elif self.opcode == "-":
            res = f'{self.num1} {self.opcode} {self.num2} = {Quiz01Calculator.sub(self)}'
        elif self.opcode == "*":
            res = f'{self.num1} {self.opcode} {self.num2} = {Quiz01Calculator.mul(self)}'
        elif self.opcode == "/":
            res = f'{self.num1} {self.opcode} {self.num2} = {Quiz01Calculator.div(self)}'
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
        return self.weight / (Quiz02Bmi.meter(self) * Quiz02Bmi.meter(self))

    def res(self):
        if Quiz02Bmi.sum(self) < 18.5:
            res = "저체중"
        elif 18.5 <= Quiz02Bmi.sum(self) and Quiz02Bmi.sum(self) < 23:
            res = "정상"
        elif 23 <= Quiz02Bmi.sum(self) and Quiz02Bmi.sum(self) < 25:
            res = "과체중"
        elif 25 <= Quiz02Bmi.sum(self):
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

class Quiz05Dice:
    @staticmethod
    def num():
        return random.randint(1, 6)

class Quiz06RandomGenerator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def rand(self):
        return random.randint(self.num1,self.num2)

class Quiz07RandomChoice:
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
    def choice(self):
        return self.members[random.randint(0, 23)]

class Quiz08Rps:
    def __init__(self):
        pass

class Quiz09GetPrime:
    def __init__(self):
        pass

class Quiz10LeapYear:
    def __init__(self):
        pass

class Quiz11NumberGolf:
    def __init__(self):
        pass

class Quiz12Lotto:
    def __init__(self):
        pass

class Quiz13Bank: # 이름, 입금, 출금만 구현
    def __init__(self):
        pass

class Quiz14Gugudan: # 책받침구구단
    def __init__(self):
        pass


if __name__ == '__main__':
    main()