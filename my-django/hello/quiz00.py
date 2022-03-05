import random

from domains import my100, myRandom, Member, memberlist


class Quiz00:
    def quiz00calculator(self)->float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        o2 = o[myRandom(0, 4)]
        res = ''
        if o2 == '+':
            res = f'{a} {o2} {b} = {self.add(a, b)}'
        elif o2 == '-':
            res = f'{a} {o2} {b} = {self.sub(a, b)}'
        elif o2 == '*':
            res = f'{a} {o2} {b} = {self.mul(a, b)}'
        elif o2 == '/':
            res = f'{a} {o2} {b} = {self.div(a, b)}'
        elif o2 == '%':
            res = f'{a} {o2} {b} = {self.mod(a, b)}'
        print(res)
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 120.8
        res = this.weight / (this.height * this.height) * 10000
        if res > 25:
            res = '비만'
        elif res > 23:
            res = '과체중'
        elif res > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(res)
    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        com = myRandom(1, 3)
        user = myRandom(1, 3)
        rps = ['바위', '가위', '보']
        res = ''
        if user == 1 or user == 2:
            res = f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Draw" if (user == com) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Win" \
                if (user > (com + 1) % 3) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Lose"
        elif user == 3:
            res = f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Draw" if (user == com) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Win" \
                if (user > com + 1) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Lose"
        print(res)
    def quiz04leap(self):
        year = myRandom(0, 10001)
        if year % 4 == 0:
            res = f'{year}은 윤년입니다.'
        else:
            res = f'{year}은 윤년이 아닙니다'
        print(res)

    def quiz05grade(self):
        kor = my100()
        eng = my100()
        math = my100()
        sum = self.sum(kor, eng, math)
        avg = self.avg(sum)
        grade = self.grade(avg)
        passChk = self.passChk(grade)
        print(f'국어 : {kor} \n영어 : {eng} \n수학 : {math} \n합계 : {sum} '
              f'\n평균 : {avg} \n등급 : {grade} \n합격여부 : {passChk}')

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, sum):
        return sum / 3

    def grade(self, avg):
        if avg >= 90:
            res = "A"
        elif avg >= 80:
            res = "B"
        elif avg >= 70:
            res = "C"
        elif avg >= 60:
            res = "D"
        else:
            res = "F"
        return res

    def passChk(self, grade):
        if grade == "F":
            res = "불합격"
        else:
            res = "합격"
        return res

    def quiz06memberChoice(self):
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
        return members[myRandom(0, 23)]

    def quiz07lotto(self):
        num =myRandom(1,10)
        res = []
        for i in range(0,num):
            li = random.sample(range(1,46), 6)
            li.sort()
            res.append(li)
        print(li)
    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        name = memberlist()[myRandom(0,23)]
        money = myRandom(1000, 100000)
        while 1:
            menu = int(input(f"{name}님의 현재 잔액 : {money} \n0.종료 1.입금 2.출금 \n입력 : "))
            plus = myRandom(1000, 100000)
            minus = myRandom(1000, 100000)
            if menu == 0:
                print('종료')
                break
            elif menu == 1:
                money = money + plus
                print(f'이름 : {name} 입금한 금액 : {plus} 잔액 : {money}')
            elif menu == 2:
                money = money - minus
                if money < 0 :
                    print("잔액보다 출금할 금액이 더 큽니다.")
                print(f'이름 : {name} 출금한 금액 : {minus} 잔액 : {money}')
    def quiz09gugudan(self):  # 책받침구구단
        pass
