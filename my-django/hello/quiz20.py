import random
import urllib
import pandas as pd

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

    def quiz24zip(self) -> []:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        #self.find_rank(soup)
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        #self.dict2(ls1,ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        #print(dict)
        return dict
    @staticmethod
    def dict1(ls1,ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def print_music_list(soup):
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self,soup):
        topic = ['artist', 'title']
        for i,j in enumerate(self.find_music(soup, topic)):
            print(f'{i} 위 : {j}')

    @staticmethod
    def find_music(soup, name) -> []:
        ls = soup.find_all('p', {'class': name})
        return [i.get_text() for i in ls]


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

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient = 'index')
        print(df)
        df.to_csv('./save/bugs.csv', sep = ',' , na_rep = 'NaN')

    def quiz29(self) -> str: return None
