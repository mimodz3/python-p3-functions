#!/usr/bin/env python3

def greet_programmer():  
    print("Hello, programmer!")
 
    pass
def greet(name):
    greeting = f"Hello, {name}!"  # Use an f-string to insert the 'name' variable into the greeting message
    print(greeting)  # Print the greeting message

    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
  
    pass

def add(num1, num2):
    return num1 + num2
    pass

def halve(number):
    if not isinstance(number, (int, float)):
         return None
    return number / 2
         
         
    pass
