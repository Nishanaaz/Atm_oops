class customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print("I am ",self.name,"I am ",self.age)
c1=customer("Nitesh",45)
c2=customer("Muskan",54)
c3=customer("Anamika",90)
l=[c1,c2,c2]
for i in l:
    # print(i)  it will not print in a proper format as we haven't defined. 
    print(i.name,i.age)   #it will print as we have called it is an object.