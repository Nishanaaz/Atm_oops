class phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price=price
        self.__brand=brand
        self.__camera=camera

    def buy(self):
        print("Buying a phone")
class smartphone(phone):
    def buy(self):
        print("buying a smartphone")
        super().buy()
s=smartphone(20000,"apple",12)
s.buy()