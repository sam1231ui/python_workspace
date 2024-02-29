import constant_demo

print(constant_demo.PI)
print(constant_demo.GRAVITY)

# this will not prevent  the below code but its convention to make const like this
constant_demo.PI = 10
print(constant_demo.PI)

print(type('s'))

demo = None
print(demo)