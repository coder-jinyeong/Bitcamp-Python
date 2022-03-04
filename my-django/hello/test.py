import random
import numpy as np
if __name__ == '__main__':
    num = int(input("입력 : "))
    li = []
    for i in range(0, num):
        li += random.sample(range(1, 46), 6)
    print(li)
    print(li[2])

