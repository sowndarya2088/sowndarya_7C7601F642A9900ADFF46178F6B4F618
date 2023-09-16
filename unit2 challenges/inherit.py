class a:
    def fun(self):
        print("house")

class b(a):
    def fu(self):
        print("car")

class c(a):
    def fun(self):
        print("bike")

class d(b,c):
    def fun(self):
        print("scooty")

obj=d()
obj.func()
