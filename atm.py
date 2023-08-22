class Atm:
    # Init is a constructor a special method that executes the code automatically
    __counter=1 
    # counter=1
    def __init__ (self):    
        self.__pin=""
        self.__balance=0
        self.s_no=Atm.__counter
        Atm.__counter+=1
        # type(self).counter+=1
        self.__menu()
    @staticmethod  
    def get_counter():
        return Atm.__counter 
    def set_counter(new_counter):
        if type(new_counter)==int:
            Atm.__counter=new_counter
        else:
            print("Not allowed ,should be an integer") 
        
    def __menu(self):
        user_input=int(input("""
                            Hello, how would you like to proceed?
                            1.Enter 1 to create pin
                            2.Enter 2 to deposit
                            3.Enter 3 to withdraw
                            4.Enter 4 to check balance
                            5.Enter 5 to exit 
                             """))
        


        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.Deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input==4:
            self.check_balance()
        elif user_input==5:
            print("Exit")
        else:
            print("Bye")
    def create_pin(self):
        self.__pin=int(input("Create a new pin"))
        print("Successfully created")


    def get_pin(self):
        return self.__pin

    def change_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin changed")
        else:
            print("Not allowed,should be a string")
    def Deposit(self):
        user_pin=int(input("Enter your pin here"))
    
        if user_pin==self.__pin:
            Amount=int(input("Enter the amount you want o deposit"))
            self.__balance+=Amount
            print("Successfully Deposited")
        else:
            print("Invalid pin ")

    def withdraw(self):
        user_pin=int(input("Enter your pin here"))
        if user_pin==self.__pin :
            Amount=int(input("Enter the amount you want to withdraw"))
            if Amount<self.balance:
                self.__balance-=Amount
                print("Successfully withdraw")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin ")
    def check_balance(self):
        user_pin=int(input("Enter your pin here"))
        if user_pin==self.__pin:
            print("The Total amount is : ",self.__balance)
        else:
            print("Invalid Pin")
        
c1=Atm()
c2=Atm()
c3=Atm()
c4=Atm()
print(c1.s_no)
print(c2.s_no)
print(c3.s_no)
print(c4.counter)
print(Atm.counter)
print(Atm.counter)



