class Pet:
    def __init__(self):
        self.name = None
        self.age =  None
        self.animal_type = None

    def set_name(self, new_name):
        self.name = new_name

    def set_animal_type(self, new_animal_type):
        self.animal_type = new_animal_type

    def set_age(self, new_age):
        self.age = new_age

    def get_name(self):
        return print(f"Вашего питомца зовут {self.name}")

    def get_animal_type(self):
        return print(f"У Вас {self.animal_type}")

    def get_age(self):
        return print(f"Вашему питомцу {self.age} лет")


tom = Pet()
tom.set_name(input("Как зовут Вашего питомца? "))
tom.set_animal_type(input("Какой он породы? "))
tom.set_age(input("Сколько лет питомцу? "))
tom.get_name()
tom.get_animal_type()
tom.get_age()