#1

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

def grams_to_ounces(grams):
    return 28.3495231 * grams

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
    
    grams = 100
    print(f"{grams} grams is {grams_to_ounces(grams)} ounces")

#2

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

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

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
    
    grams = 100
    print(f"{grams} grams is {grams_to_ounces(grams)} ounces")
    
    fahrenheit = 98.6
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")

#3

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

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return "No solution"

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
    
    grams = 100
    print(f"{grams} grams is {grams_to_ounces(grams)} ounces")
    
    fahrenheit = 98.6
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    
    numheads, numlegs = 35, 94
    chickens, rabbits = solve(numheads, numlegs)
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")

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

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

numbers = [10, 15, 3, 7, 19, 23, 29, 30]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return "No solution"

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
    
    grams = 100
    print(f"{grams} grams is {grams_to_ounces(grams)} ounces")
    
    fahrenheit = 98.6
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    
    numheads, numlegs = 35, 94
    chickens, rabbits = solve(numheads, numlegs)
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")

#5

import itertools

def print_permutations():
    user_input = input("Enter a string: ")
    permutations = itertools.permutations(user_input)
    
    # Convert permutations to a list and print each permutation
    for perm in permutations:
        print(''.join(perm))

# Call the function
print_permutations()

#6

def reverse_words():
    user_input = input("Enter a sentence: ")
    words = user_input.split()  # Split the sentence into a list of words
    reversed_sentence = ' '.join(words[::-1])  # Reverse the list of words and join them
    return reversed_sentence

# Call the function
result = reverse_words()
print(result)

#7

def has_33(nums):
    # Loop through the list, checking for two consecutive 3's
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Test cases
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False

#8

def spy_game(nums):
    # Check if 0, 0, 7 appears in order in the list
    sequence = [0, 0, 7]
    index = 0
    
    for num in nums:
        if num == sequence[index]:
            index += 1
        if index == len(sequence):
            return True
    
    return False

# Test cases
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False

#9

import math

def sphere_volume(radius):
    # Volume of a sphere: (4/3) * π * r^3
    return (4/3) * math.pi * radius**3

# Test case
radius = 5
print(f"The volume of the sphere with radius {radius} is {sphere_volume(radius)}")

#10

def unique_elements(nums):
    unique_list = []
    
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list

# Test case
input_list = [1, 2, 2, 3, 4, 4, 5]
print(f"Unique elements: {unique_elements(input_list)}")

#11

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Test cases
print(is_palindrome("madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True

#12

def histogram(nums):
    for num in nums:
        print('*' * num)

# Test case
histogram([4, 9, 7])

#13

import random

def guess_the_number():
    # Greet the user and ask for their name
    name = input("Hello! What is your name?\n")
    
    # Choose a random number between 1 and 20
    number_to_guess = random.randint(1, 20)
    
    # Inform the user about the game
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    guesses_taken = 0
    
    while True:
        # Prompt the user to take a guess
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

# Call the function to start the game
guess_the_number()

#14