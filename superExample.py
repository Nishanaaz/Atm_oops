class phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera


class smartphone(phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("inside smartphone constructor")

s=smartphone(20000,"apple",12,"Android",3)
print(s.os)
print(s.brand)