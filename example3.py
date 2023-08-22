class a:
    def __init__(self):
        self.var1=100
    def display1(self,var1):
        print("class a: ",self.var1)
class b(a):
    def display2(self,var1):
        print("class b: ",self.var1)
obj=b()
obj.display1(200)
# it will print 100 as already defined in the constructor  