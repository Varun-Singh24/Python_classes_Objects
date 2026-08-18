# 🚗 OOPs in Python: Classes & Inheritance

### This repository covers the fundamentals of **Object-Oriented Programming (OOP)** in Python, focusing on **Classes**, **Objects**, **Constructors**, and **Inheritance**.

### OOP helps structure code logically, enabling **reusability**, **scalability**, and clean software architecture.

---

## 🛠️ Tools & Environment

* **Language:** Python 🐍
* **Environment:** Jupyter Notebook / VS Code
* **Concepts Used:**
* Classes & Objects
* Constructor (`__init__`) & `self`
* Class Methods
* Inheritance & `super()`



---

## 🚘 1. Base Class & Object Creation

### 📌 Concept

A **Class** acts as a blueprint, while an **Object** is an instance created from that blueprint. The `__init__` constructor initializes the object's attributes, and `self` points to the current object instance.

### 🧾 Code

```python
# Defining the Base Class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model):
        self.brand = brand      # Instance Attribute
        self.model = model      # Instance Attribute

    # Instance Method
    def car_name(self):
        return f"{self.brand} {self.model}"


# Creating Objects (Instances) of Car
my_car = Car("Toyota", "Corolla")
print(my_car.brand)         # Output: Toyota
print(my_car.model)         # Output: Corolla
print(my_car.car_name())    # Output: Toyota Corolla

print("-" * 35)

my_new_car = Car("TATA", "Safari")
print(my_new_car.model)     # Output: Safari
print(my_new_car.car_name())# Output: TATA Safari

```

### 📘 Explanation

* **`__init__()`**: Automatically executes when a new object is created to assign initial values.
* **`self`**: A mandatory reference parameter that binds attributes and methods to the specific object instance.
* **`car_name()`**: A custom method that accesses instance attributes using `self` and returns formatted data.

---

## ⚡ 2. Inheritance & Super Class

### 📌 Concept

**Inheritance** allows a child class (`ElectricCar`) to inherit properties and methods from a parent class (`Car`), avoiding code duplication.

### 🧾 Code

```python
# Child Class inheriting from Parent Class (Car)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # Call the constructor of the Parent Class (Car)
        super().__init__(brand, model)
        self.battery_size = battery_size


# Instantiating the Child Class
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Accessing inherited attributes & methods
print(my_tesla.brand)        # Output: Tesla
print(my_tesla.model)        # Output: Model S
print(my_tesla.car_name())   # Output: Tesla Model S (Inherited Method)
print(my_tesla.battery_size) # Output: 85kWh (Child Attribute)

```

### 🎯 Use Case

✔ **Code Reusability:** Avoid re-writing common parameters (`brand`, `model`) in specialized classes.
✔ **Extensibility:** Easily add specialized features (like `battery_size`) specifically tailored for electric vehicles.

---

## 🧠 Concepts Practiced

* **Encapsulation:** Grouping attributes and behaviors into a single unit (Class).
* **Inheritance:** Deriving new classes from existing ones to build hierarchical relationships.
* **`super()` Function:** Delegating parent class attribute initialization cleanly.
