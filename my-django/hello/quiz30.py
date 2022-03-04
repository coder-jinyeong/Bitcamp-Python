class Quiz30 :
    @staticmethod
    def quiz30list():
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

        a = [1,2]
        b = [0,5]
        c = [a,b]
        print(c)
        print(c[0][1])

        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)

        print(sum(a))

        b = [2, 10, 0 -2]
        print(sorted(b))

        print(b.index(0), len(b))
        return ''

    @staticmethod
    def quiz31Tuple():
        a = (1, 2)
        print(a, type(a))
        return ''

    @staticmethod
    def quiz32Dict():
        a = {"class":['deep learning', 'machine learning'], "num_students":[40,20]}
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
        return ''