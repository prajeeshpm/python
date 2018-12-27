def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1},  arg2: {arg2}")
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
#this one take one argumennt
def print_one(arg1):
    print(f"arg1: {arg1}")
# this one take no arguments
def print_none():
    print("I got nothing")
print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("First")
print_none()