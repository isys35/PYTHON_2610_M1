class Pet:
    def __init__(self):
        self.__name = None
        self.__age =  None
        self.__animal_type = None

    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_animal_type):
        self.__animal_type = new_animal_type

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return print(f"Вашего питомца зовут {self.__name}")

    def get_animal_type(self):
        return print(f"У Вас {self.__animal_type}")

    def get_age(self):
        return print(f"Вашему питомцу {self.__age} лет")

