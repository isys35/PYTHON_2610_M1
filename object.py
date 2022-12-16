"""Напишите программу, в которой описывается
функция, предназначенная для создания объекта. Объект
создается на основе уже существующего объекта, который
передается функции в качестве аргумента. В создаваемый
объект добавляются только те неслужебные
поля из исходного объекта, которые имеют целочисленное значение"""

class OldObj:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value


def new_obj(OldClass):
    new_dict = dict(filter(lambda item: isinstance(item[1],int), OldClass.__dict__.items()))
    return OldClass.__class__(**new_dict)

def main():
    old: OldObj = OldObj(s=2, r="abc", b=2, t="abc", u=2, o="abc")
    superman : OldObj = new_obj(old)
    print(old.__dict__)
    print(superman.__dict__)

if __name__ == '__main__':

    main()
