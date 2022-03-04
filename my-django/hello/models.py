import random
def myRandom(start, end):
    return random.randint(start,end)

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
    @staticmethod
    def getBmi(member):
        this = member
        bmires = this.weight / (this.height * this.height) * 10000
        if bmires > 25:
            return f'비만'
        elif bmires > 23:
            return f'과체중'
        elif bmires > 18.5:
            return f'정상'
        else:
            return f'저체중'

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
        if self.avg() >= 90:
            res = "A"
        elif self.avg() >= 80:
            res = "B"
        elif self.avg() >= 70:
            res = "C"
        elif self.avg() >= 60:
            res = "D"
        else:
            res = "F"
        return res
    def chkPass(self):
        if self.getGrade() == "F":
            res = "불합격"
        else:
            res = "합격"
        return res

class Quiz05Dice:
    @staticmethod
    def num():
        return myRandom(1, 6)

class Quiz06RandomGenerator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def rand(self):
        return myRandom(self.num1,self.num2)

class Quiz07RandomChoice:
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
    def choice(self):
        return self.members[myRandom(0, 23)]

class Quiz08Rps:
    def __init__(self,user):
        self.user = user
        self.com = myRandom(1,3)
    def res(self):
        if self.user == 1 or self.user == 2:
            res = "Draw" if (self.user == self.com) else "Win" if (self.user > (self.com + 1) % 3) else "Lose"
        elif self.user == 3:
            res = "Draw" if (self.user == self.com) else "Win" if (self.user > self.com + 1)else "Lose"
        return res

class Quiz09GetPrime:
    def __init__(self,num):
        self.num = num

    def res(self):
        count = 0
        res = ''
        for i in range(2, self.num):
            for j in range(1, i):
                if i % j == 0:
                    count += 1
            if count == 1:
                res += f'{i}\t'
            count = 0
        return res

class Quiz10LeapYear:
    def __init__(self,year):
        self.year = year

    def result(self):
        if self.year % 4 == 0 : res = f'윤년입니다.'
        else: res = f'윤년이 아닙니다'
        return res

class Quiz11NumberGolf:
    @staticmethod
    def result():
        rand = myRandom(0,100)
        while(1):
            num = int(input("숫자 입력 : "))
            if num == rand:
                res = '맞췄습니다.'
                return res
            elif num < rand:
                print(f'{num} 보다 더 큽니다.')

            elif num > rand:
                print(f'{num} 보다 더 작습니다')
            else:
                print('잘못 입력하였습니다.')

class Quiz12Lotto:
    def __init__(self, num):
        self.num = num
    def result(self):
        pass

class Quiz13Bank: # 이름, 입금, 출금만 구현
    def __init__(self):
        pass

class Quiz14Gugudan: # 책받침구구단
    def __init__(self):
        pass

