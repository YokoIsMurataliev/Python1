#1

class StringProcessor:
    def __init__(self):
        self.input_string = ""
    
    def getString(self):
        self.input_string = input("Enter a string: ")
    
    def printString(self):
        print(self.input_string.upper())

# Example usage:
if __name__ == "__main__":
    sp = StringProcessor()
    sp.getString()
    sp.printString()

#2

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

# Example usage:
if __name__ == "__main__":
    square = Square(5)
    print("Area of square:", square.area())

#3

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Example usage:
if __name__ == "__main__":
    square = Square(5)
    print("Area of square:", square.area())
    
    rectangle = Rectangle(4, 6)
    print("Area of rectangle:", rectangle.area())

#4

import math

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example usage:
if __name__ == "__main__":
    square = Square(5)
    print("Area of square:", square.area())
    
    rectangle = Rectangle(4, 6)
    print("Area of rectangle:", rectangle.area())
    
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    point1.show()
    print("Distance between points:", point1.dist(point2))

#5

import math

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

# Example usage:
if __name__ == "__main__":
    square = Square(5)
    print("Area of square:", square.area())
    
    rectangle = Rectangle(4, 6)
    print("Area of rectangle:", rectangle.area())
    
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    point1.show()
    print("Distance between points:", point1.dist(point2))
    
    account = Account("John Doe", 100)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(150)

#6

import math

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 19, 23, 29, 30]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)

# Example usage:
if __name__ == "__main__":
    square = Square(5)
    print("Area of square:", square.area())
    
    rectangle = Rectangle(4, 6)
    print("Area of rectangle:", rectangle.area())
    
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    point1.show()
    print("Distance between points:", point1.dist(point2))
    
    account = Account("John Doe", 100)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(150)
