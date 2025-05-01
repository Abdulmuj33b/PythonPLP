# PythonPLP
Gadget Class & Polymorphism Implementation Documentation
1. Gadget Class (Object-Oriented Programming)
Overview
The Gadget class represents a general electronic device with attributes such as brand, model, and price. The class utilizes constructors to initialize attributes and provides a method to display gadget details.

Implementation

    class Gadget:
        def __init__(self, brand, model, price):
            self.brand = brand
            self.model = model
            self.price = price

    def show_details(self):
        return f"{self.brand} {self.model} costs ${self.price}."
Inheritance: Smartphone Subclass
The Smartphone class inherits from Gadget, adding an extra attribute for the operating system (os). It overrides the show_details() method to include the OS.

    class Smartphone(Gadget):
        def __init__(self, brand, model, price, os):
            super().__init__(brand, model, price)
            self.os = os

    def show_details(self):
        return f"{self.brand} {self.model} runs on {self.os} and costs ${self.price}."
Object Creation Example

    gadget1 = Gadget("TechCorp", "X100", 299)
    smartphone1 = Smartphone("Innovate", "PhoneX", 999, "Android")
    
    print(gadget1.show_details())
    print(smartphone1.show_details())

2. Polymorphism Challenge (Vehicles & Movement)
Overview
The Vehicle base class defines a generic move() method. Subclasses (Car, Plane, and Boat) override the move() method to exhibit unique behaviors.

Implementation

    class Vehicle:
        def move(self):
            return "Moving in some way..."
    
    class Car(Vehicle):
        def move(self):
            return "Driving 🚗"
    
    class Plane(Vehicle):
        def move(self):
            return "Flying ✈️"
    
    class Boat(Vehicle):
        def move(self):
            return "Sailing 🚢"
Demonstrating Polymorphism
We instantiate multiple vehicle objects and call move() dynamically:


    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
    print(v.move())

✅ Encapsulation: Attributes (brand, model, price, os) are managed within class definitions. ✅ Inheritance: Smartphone inherits from Gadget, gaining all attributes and behaviors. ✅ Polymorphism: Vehicle subclasses override the move() method uniquely.
