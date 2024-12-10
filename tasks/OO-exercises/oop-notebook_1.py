# Python Object-Oriented Programming (OOP) Notebook

## 1. Introduction to Classes and Objects

### 1.1 Defining a Basic Class

```python
class Car:
    # Class attribute
    wheels = 4
    
    # Constructor method
    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    # Instance method
    def start_engine(self):
        """Start the car's engine"""
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model}'s engine started!")
        else:
            print("Engine is already running.")
    
    # Instance method with return
    def get_description(self):
        """Return a description of the car"""
        return f"{self.year} {self.make} {self.model}"

# Creating objects (instances)
my_car = Car("Toyota", "Corolla", 2022)
print(my_car.get_description())
my_car.start_engine()
```

### 1.2 Inheritance

```python
class ElectricCar(Car):
    """A subclass of Car specific to electric vehicles"""
    def __init__(self, make, model, year, battery_capacity):
        # Call the parent class constructor
        super().__init__(make, model, year)
        
        # Additional attribute specific to electric cars
        self.battery_capacity = battery_capacity
    
    # Method override
    def start_engine(self):
        """Override start_engine for electric cars"""
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model}'s electric motor activated!")
        else:
            print("Vehicle is already running.")
    
    # New method specific to electric cars
    def check_battery(self):
        """Check battery capacity"""
        return f"Battery Capacity: {self.battery_capacity} kWh"

# Create an electric car instance
tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
print(tesla.get_description())
tesla.start_engine()
print(tesla.check_battery())
```

## 2. Advanced OOP Concepts

### 2.1 Class Methods and Static Methods

```python
class MathOperations:
    # Class attribute to keep track of operations
    operation_count = 0
    
    @classmethod
    def increment_operations(cls):
        """Class method to track number of operations"""
        cls.operation_count += 1
    
    @staticmethod
    def add(x, y):
        """Static method for addition"""
        MathOperations.increment_operations()
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """Static method for multiplication"""
        MathOperations.increment_operations()
        return x * y

# Using class and static methods
print(MathOperations.add(5, 3))
print(MathOperations.multiply(4, 6))
print(f"Total operations: {MathOperations.operation_count}")
```

### 2.2 Encapsulation and Property Decorators

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        # Private attributes (convention using underscore)
        self._owner = owner
        self._balance = balance
    
    # Getter for balance
    @property
    def balance(self):
        return self._balance
    
    # Getter for owner
    @property
    def owner(self):
        return self._owner
    
    # Setter with validation
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

# Using the BankAccount class
account = BankAccount("Alice", 1000)
print(f"Owner: {account.owner}")
account.deposit(500)
print(f"Balance: ${account.balance}")
```

### 2.3 Multiple Inheritance

```python
class Flying:
    def fly(self):
        return "I can fly!"

class Swimming:
    def swim(self):
        return "I can swim!"

class Drone(Flying, Swimming):
    def __init__(self, model):
        self.model = model
    
    def describe(self):
        return f"Drone Model: {self.model}"

# Create a multi-capability drone
my_drone = Drone("Phantom")
print(my_drone.describe())
print(my_drone.fly())
print(my_drone.swim())
```

## 3. Practical Exercise: Employee Management System

```python
class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self._salary = 0
    
    def assign_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be positive")
    
    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}"

class Manager(Employee):
    def __init__(self, name, employee_id, department, team_size):
        super().__init__(name, employee_id, department)
        self.team_size = team_size
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Team Size: {self.team_size}"

# Create and manage employees
employees = [
    Employee("John Doe", "E001", "Marketing"),
    Employee("Jane Smith", "E002", "Sales"),
    Manager("Mike Johnson", "M001", "IT", 10)
]

for emp in employees:
    try:
        emp.assign_salary(50000 if isinstance(emp, Manager) else 40000)
        print(emp.get_details())
    except ValueError as e:
        print(f"Error: {e}")
```

"""

## Learning Objectives Checklist
- [x] Create and use basic classes
- [x] Understand constructors and instance methods
- [x] Implement inheritance
- [x] Use class and static methods
- [x] Implement encapsulation
- [x] Explore property decorators
- [x] Understand multiple inheritance
- [x] Create a practical OOP project

## Additional Challenges for Practice
1. Extend the `BankAccount` class with more advanced features
2. Create a complex inheritance hierarchy
3. Implement error handling in your classes
4. Design a small project using OOP principles
"""

"""
```

## Notes for Learners
- Run each code section individually
- Experiment with the code
- Try modifying and extending the classes
- Create your own classes based on these examples
"""