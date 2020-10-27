#DEFINIZIONE DI FUNZIONI

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(first, second):
    print(f"arg1: {first}, arg2: {second}")

 # this just takes one argument
def print_one(first):
    print(f"arg1: {first}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
