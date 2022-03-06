import random
from domains import memberlist
if __name__ == '__main__':
    res = ''
    for i in range(1,10,3):
        for j in range(1,10):
            for k in range(i, (i+3)):
                res += f'{k} * {j} = {k * j}\t'
            res += '\n'
        res += '\n'
    print(res)