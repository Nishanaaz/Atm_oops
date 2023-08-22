class parent:
    def __init__(self,num) :
        self.__num=num
    def  get_num(self):
        return self.__num
class child(parent):
    def __init__(self,val,num):
        //super().__init__(num)    #solution to access the value of num using super
        self.__val=val
    def get_val(self):
        return self.__val


son=child(100,2)
print(son.get_val())
# print(son.get_num())  it will show an error as it didn't go to 
# parent constructor as it has its own aur agar
# and it here doesn't initial the num value so it will show an error.