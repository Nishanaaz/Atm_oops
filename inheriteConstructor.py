class phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price #can't access private 
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying phones")
class smartphone(phone):
    def buy(self):
        print("buying phone own my own")
s=smartphone(20000,"Apple",12)
print(s.brand,s.camera)
s.buy()
#this is called method overriding means parent has the same method
# as the cild has, but it will use his own rather to inherit from parents 