class car:
    total=0
    def __init__(self,make,model,launch,price):
        self.make=make
        self.model=model
        self.launch=launch
        self.price=price
        self.started=False
        self.current_speed=0
        self.max_speed=200

    def startCar(self):
        self.started=True
    def accelerate(self,value):
        if self.started==True:
            self.current_speed+=value
        else:
            print("Car is not started yet")
c1=car("BMW","BM09",385039,589)
print(c1)
c1.startCar()
c1.accelerate(200)
print("Current speed:", c1.current_speed)

