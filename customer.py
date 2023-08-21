class customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(customer):
    if customer=="M":
        customer.name="Muskan"
        print("Hello",customer.name,"Sir")
    else:
        print("Hello",customer.name,"Madam")
cust=customer("Ankit","M")
greet(cust)

#This shows that objects are mutable like lists and dictionary.