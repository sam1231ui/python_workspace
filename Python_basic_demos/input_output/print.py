import random

print("hello-world")

# variables
# no = input("Enter no ")
# print("This is your no ", no)
no2 = 20
# print(type(no))
# print(type(no2))

print(f"type - {type(3j)} value - {3j}")

print(random.randrange(1, 10))

# String of python it does nt have chr as type
str = "samruddha"
print(str)
print(f"{type(str[0])} value {str[0]}")

# we can check directly if text is present in string or not
txt = "The best things in life are free!"
status = "happy" if "free" in txt else "not happy"
print(status)

print(2**10)

print(100//2.3)

print(2 & 3)

n = "return" if not(3 & 1) else "not return" if (False) else "nt"
print(n)

