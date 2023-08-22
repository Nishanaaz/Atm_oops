class product:
    def review(self):
        print("Product customer review")
class phone(product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price #can't access private 
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying phones")
class smartphone(phone):
    # def buy(self):
    #     print("buying phone own my own")
    pass
s=smartphone(20000,"Apple",12)
p=phone(10000,"samsung",1)
print(s.brand,s.camera)
s.buy()
s.review()
p.review()