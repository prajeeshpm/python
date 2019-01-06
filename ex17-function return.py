def add(a,b):
    print(f"adding {a} + {b}")
    return a + b 
def substract(a,b):
    print(f"substracting {a} - {b}")
    return a - b 
def multiply(a,b):
    print(f"multiply {a} * {b}")
    return a * b
def divide(a,b):
    print(f"Devide {a} / {b}")
    c = a / b
    return c
print("Lets do some math with functons")
age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
print(f"Age:  {age} , Height: {height}, Weight : {weight}, Iq : {iq}")
print("Here is a puzle")
what = add (age, substract(height,multiply(weight,divide(iq,2))))
print(f"That becomes: {what} can you do it bu hand?")

