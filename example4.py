class parent:
    def __init__(self):
        self.__num=100
    def show(self):
        print("Parent",self.__num)
class child(parent):
    def __init__(self):
        super().__init__()
        self.__var=10
    def show(self):
        print("child",self.__var)
dad=parent()
dad.show()
son=child()
son.show()