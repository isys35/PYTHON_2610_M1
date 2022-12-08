"""Напишите программу, в которой описывается
функция, предназначенная для создания объекта. Объект
создается на основе уже существующего объекта, который
передается функции в качестве аргумента. В создаваемый
объект добавляются только те неслужебные
поля из исходного объекта, которые имеют целочисленное значение"""

class NumberList:

    def __init__(self, l, w, r):
        self.l = l
        self.w = w
        self.r = r
        self.list2 = {}

    def export(self):
        for a,b in self.__dict__.items():
            if isinstance(b,int):
                self.list2[a] = b

        print(self.list2)
        return self.list2

d = NumberList(10,5,6.5)
v = d.export()
print(v)

class NumberList2:

    def __init__(self, NumberList, z):
        self.__dict__ = NumberList
        self.z = z

    def export(self):
        r = self.__dict__
        print(r)


v = NumberList2(v, 5)
v.export()
