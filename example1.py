class parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class child(parent):
    def show(self):
        print("this is a child class")
son=child(200)
print(son.get_num())
son.show()