import random
import urllib

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Quiz20:

    def quiz20list(self) -> str:
        list = [1, 2, 3, 4]
        print(list)
        print(list[0], list[-1], list[-2], list[1:3])

        list2 = ['math', 'english']
        print(list2[0])

        list3 = [1, '2', [1, 2, 3]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])

        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)

        print(sum(a))

        b = [2, 10, 0 - 2]
        print(sorted(b))

        print(b.index(0), len(b))

    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))

    def quiz22dict(self) -> str:
        a = {"class": ['deep learning', 'machine learning'], "num_students": [40, 20]}
        print(a)
        print(type(a))
        print(a["class"])
        a['grade'] = ['A', 'B', 'C']
        print(a)
        print(a.keys())
        print(list(a.keys()))
        print(a.values())
        print(a.items())
        print(a.get('class'))
        print('class' in a)

    def quiz23listcom(self) -> str:
        print('-----Legacy-----')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-----List Comprension-----')
        a2 = [i for i in range(5)]
        print(a2)

        return None

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        '''
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        #print(''.join(i for i in artists))
        title = soup.find_all('p', {'class': 'title'})
        title = [i.get_text() for i in title]
        print(''.join((i for i in title)))
        '''
        topic = ['artist', 'title']
        res = [self.bugs(soup, i) for i in topic]
        # res = [self.bugs(soup, j) for i,j in enumerate(topic)]
        print(res)
    @staticmethod
    def bugs(soup,name):
        names = soup.find_all('p', {'class': name})
        names = [i.get_text() for i in names]
        print('\n'.join((i for i in names)))


    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0' }
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030815'
        req = urllib.request.Request(url, headers= headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        artists = soup.find_all('div', {'class': 'ellipsis rank01'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None
