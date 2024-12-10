# Advanced Python Object-Oriented Programming Notebook

## 1. Metaclasses and Class Creation

```python
# Custom Metaclass for Logging Class Creation
class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        # Add a creation timestamp to the class
        attrs['_created_at'] = __import__('datetime').datetime.now()
        
        # Log class creation
        print(f"Creating class: {name}")
        
        # Optionally modify or validate class attributes
        if not any(method.startswith('validate_') for method in attrs):
            print(f"Warning: No validation method found for {name}")
        
        # Create the class
        return super().__new__(cls, name, bases, attrs)

# Using the metaclass
class DataValidator(metaclass=LoggingMeta):
    @classmethod
    def validate_data(cls, data):
        """Base validation method"""
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        return data

class UserProfile(DataValidator):
    def __init__(self, **kwargs):
        validated_data = self.validate_data(kwargs)
        for key, value in validated_data.items():
            setattr(self, key, value)
    
    def __repr__(self):
        attrs = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

# Demonstrate metaclass and class creation
user = UserProfile(name="Alice", age=30, email="alice@example.com")
print(user)
print(f"Class created at: {UserProfile._created_at}")
```

## 2. Advanced Descriptor Protocol

```python
# Custom Descriptor for Type and Range Validation
class ValidatedAttribute:
    def __init__(self, expected_type=object, min_value=None, max_value=None):
        self.expected_type = expected_type
        self.min_value = min_value
        self.max_value = max_value
        self.data = {}
    
    def __get__(self, instance, owner):
        return self.data.get(instance, None)
    
    def __set__(self, instance, value):
        # Type checking
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type.__name__}, got {type(value).__name__}")
        
        # Range checking for numeric types
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        
        self.data[instance] = value

class Product:
    price = ValidatedAttribute(expected_type=(int, float), min_value=0, max_value=10000)
    quantity = ValidatedAttribute(expected_type=int, min_value=0)
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity

# Demonstrate descriptor usage
laptop = Product("MacBook", 1200, 5)
print(f"Product: {laptop.name}, Total Value: ${laptop.total_value()}")

# This will raise an exception
try:
    invalid_product = Product("Invalid", -100, -1)
except (TypeError, ValueError) as e:
    print(f"Validation Error: {e}")
```

## 3. Context Managers and Protocol Implementation

```python
class ResourceManager:
    """Advanced Context Manager for Resource Handling"""
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.resource = None
    
    def __enter__(self):
        print(f"Acquiring {self.resource_name}")
        # Simulate resource acquisition
        self.resource = f"Resource_{self.resource_name}"
        return self.resource
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Releasing {self.resource_name}")
        self.resource = None
        
        # Error handling
        if exc_type is not None:
            print(f"An error occurred: {exc_type.__name__} - {exc_value}")
        
        # Suppress specific exceptions if needed
        return exc_type is ValueError

# Using the context manager
def process_data(data):
    with ResourceManager("DataProcessor") as resource:
        if not data:
            raise ValueError("Empty data")
        print(f"Processing with {resource}")
        return [x * 2 for x in data]

# Demonstrate context manager
try:
    result = process_data([1, 2, 3, 4])
    print("Processed Result:", result)
    
    # This will trigger error handling
    process_data([])
except Exception as e:
    print(f"Caught exception: {e}")
```

## 4. Advanced Inheritance and Composition

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        """Abstract method to be implemented by subclasses"""
        pass
    
    @classmethod
    @abstractmethod
    def validate_input(cls, data):
        """Abstract class method for input validation"""
        pass

# Composition over Inheritance
class DataAnalytics:
    def __init__(self, processor):
        self.processor = processor
    
    def analyze(self, data):
        processed_data = self.processor.process(data)
        return {
            'mean': sum(processed_data) / len(processed_data),
            'max': max(processed_data),
            'min': min(processed_data)
        }

# Concrete Implementation
class NumberProcessor(DataProcessor):
    @classmethod
    def validate_input(cls, data):
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("All elements must be numbers")
        return data
    
    def process(self, data):
        self.validate_input(data)
        return [x * 2 for x in data]

# Demonstrate Advanced Inheritance and Composition
numbers = [1, 2, 3, 4, 5]
processor = NumberProcessor()
analytics = DataAnalytics(processor)
print("Data Analytics:", analytics.analyze(numbers))
```

## 5. Operator Overloading and Protocol Implementation

```python
class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __len__(self):
        return len(self.components)
    
    def __getitem__(self, index):
        return self.components[index]
    
    def __add__(self, other):
        """Vector addition"""
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")
        return Vector(*[a + b for a, b in zip(self, other)])
    
    def __mul__(self, scalar):
        """Scalar multiplication"""
        return Vector(*[component * scalar for component in self])
    
    def __repr__(self):
        return f"Vector{self.components}"
    
    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5

# Demonstrate Vector operations
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print("V1:", v1)
print("V2:", v2)
print("V1 + V2:", v1 + v2)
print("V1 * 2:", v1 * 2)
print("Magnitude of V1:", v1.magnitude())
```

## Advanced OOP Challenges

1. Implement a custom matrix class with operator overloading
2. Create a plugin system using metaclasses
3. Design a complex inheritance hierarchy for a real-world system
4. Build a decorator that adds logging to class methods
5. Develop a serialization mechanism for custom objects

## Learning Objectives
- [x] Understand metaclass creation and usage
- [x] Master descriptor protocol
- [x] Implement advanced context managers
- [x] Learn composition and abstract base classes
- [x] Practice operator overloading
- [x] Explore advanced inheritance techniques

## Additional Resources
- Python's `abc` module documentation
- Advanced Python Programming books
- PEP 3119 (Abstract Base Classes)
- Design Patterns in Python
"""
Advanced Object-Oriented Programming in Python

This notebook explores complex OOP concepts, demonstrating 
advanced techniques for creating flexible, robust, and 
extensible Python classes.
"""
```
"""

1. Metaclasses
   - Custom metaclass creation
   - Class creation logging and validation

2. Descriptor Protocol
   - Creating custom descriptors
   - Implementing type and range validation

3. Context Managers
   - Advanced resource management
   - Error handling in context managers

4. Advanced Inheritance and Composition
   - Abstract base classes
   - Composition techniques
   - Dependency injection

5. Operator Overloading
   - Implementing custom vector operations
   - Protocol methods like `__add__`, `__mul__`

Key Features:
- Detailed explanatory comments
- Practical, runnable code examples
- Challenges for further learning
- Learning objectives checklist

Each section demonstrates a different advanced OOP concept with executable code that illustrates the principles in action.

Recommended Approach:
- Run each code section
- Experiment with the implementations
- Try the suggested challenges
- Modify and extend the classes

"""