def get(c, n):
    def new():
        for i in range(n):
         c()

    return new

def say_hi():
    print("Привет")


a = get(say_hi, 5)()
print(a)



