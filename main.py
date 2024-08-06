def add_numbers(a,b):
    return a+b

def subtract_numbers(a,b):
  return a-b

def multiply_numbers(a,    b):
 return a *b

def divide_numbers(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b

if __name__ == "__main__":
    print(add_numbers(5,3))
    print(subtract_numbers(10,   4))
    print(multiply_numbers(2,6))
    print(divide_numbers(15,3))
