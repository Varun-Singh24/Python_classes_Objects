class Car :   # defined Class name 
    def __init__(self, brand, model ):    # This is a Constructor  __init__(self) : Q1 
        self.brand = brand                # these are attribute 
        self.model = model  


    # def function_name() :  
#  jo bhi methods banate hain usme hame self rakhna hi hota hai . Its compulsory (self as parameter) 
#  Jyada kar hum function se return karte hain . print bhi kar sakte hain 

    def carName(self) :
        return f"{self.brand} {self.model}"


# Inheritance ke liye hame 

class ElectricCar(Car) :        # it Inherits all the properties of the Car class 
    def __init__(self, brand, model, battery_size ):
        super().__init__(brand, model)  # Use super() keyword to access the superior class propertis...   (model and brand) used as it is  
        self.battery_size = battery_size                               # super upar se inherit kar leta hai.. 

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.carName())   # Inherited method 



my_Car = Car("Toyota" , "Corolla")   # this is the Object of the Car Class   
print(my_Car.brand)
print(my_Car.model)
print(my_Car.carName())

print("---------------------------------")

my_new_car = Car("TATA", "Safari") 
print(my_new_car.model)
print(my_new_car.carName())  
