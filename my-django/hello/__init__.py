from models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz06RandomGenerator, Quiz07RandomChoice, \
    Quiz08Rps, Quiz04GradeAuto, Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf,Quiz12Lotto,Quiz13Bank,Quiz14Gugudan
from quiz30 import Quiz30
from domains import Member

if __name__ == '__main__':
    while 1:
        menu = input("0.Exit 1.계산기 2.BMI 3.성적표 4.합격여부 성적표 5.주사위 6.랜덤숫자 7.랜덤이름추출 "
                     "8.가위바위보 9.소수구하기 10.윤년 11.숫자 맞추기 12.로또 생성 \n입력 : ")
        if menu == "0":
            print("Exit")
            break
        elif menu == "1":
            calc = Quiz01Calculator(int(input("첫번째 수 : ")), int(input("두번째 수 : ")), input("연산자 입력(+, -, *, /) : "))
            print(calc.res())

        elif menu == "2":
            member = Member()
            member.name = input('이름 : ')
            member.height = float(input('키 : '))
            member.weight = float(input('몸무게 : '))
            res = Quiz02Bmi.getBmi(member)
            print(f'이름: {member.name}, 키: {member.height}, 몸무게: {member.weight}, BMI상태: {res} ')

        elif menu == "3":
            grade = Quiz03Grade(input("이름 : "), int(input("국어 점수 : ")), int(input("영어 점수 : ")), int(input("수학 점수 : ")))
            print(f'이름 : {grade.name} \n국어 점수 : {grade.kor} \n영어 점수 : {grade.eng} \n수학 점수 : {grade.math} '
                  f'\n종합점수 : {grade.sum()} \n평균 : {grade.avg()}')

        elif menu == "4":
            grade = Quiz04GradeAuto(input("이름 : "), int(input("국어 점수 : ")), int(input("영어 점수 : ")), int(input("수학 점수 : ")))
            print(f'이름 : {grade.name} \n국어 점수 : {grade.kor} \n영어 점수 : {grade.eng} \n수학 점수 : {grade.math} '
                  f'\n종합점수 : {grade.sum()} \n평균 : {grade.avg()} \n등급 : {grade.getGrade()} \n합격 여부 : {grade.chkPass()}')

        elif menu == "5":
            print(f'주사위 나온 값 :  {Quiz05Dice.num()}')

        elif menu == "6":
            rd = Quiz06RandomGenerator(int(input("원하는 시작 범위 : ")), int(input("원하는 끝나는 범위 :")))
            print(f'{rd.num1} 부터 {rd.num2} 까지 중 나온 랜덤 숫자 : {rd.rand()}')

        elif menu == "7":
            ch = Quiz07RandomChoice()
            print(f'803호에서 랜덤으로 추출한 사람 : {ch.choice()}')

        elif menu == "8":
            rps = Quiz08Rps(int(input("1 : 주먹 2: 가위 3: 보자기 \n입력 : ")))
            print(f'사용자 : {rps.user} \n컴퓨터 : {rps.com} \n결과 : {rps.res()}')

        elif menu == "9":
            prime = Quiz09GetPrime(int(input("0부터 몇까지의 소수를 구하십니까 ? : ")))
            print(f"{prime.res()}")

        elif menu == "10":
            year = Quiz10LeapYear(int(input("확인하고싶은 년도 : ")))
            print(f'{year.result()}')

        elif menu == '11':
            print(Quiz11NumberGolf.result())

        elif menu == '12':
            lotto = Quiz12Lotto(int(input('생성하고싶은 로또 개수 : ')))
            print(f'생성된 로또\n{lotto.result()}')

        elif menu == '30':
            print(Quiz30.quiz30list())

        elif menu == '31':
            print(Quiz30.quiz31Tuple())

        elif menu == '32':
            print(Quiz30.quiz32Dict())

        else:
            print("잘못 입력하였습니다.")