# to access array you need to import lib they are used when you need homogenous data

numbers = arr.array('i',[10,20,30])

print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers.index(10))

numbers.append(40)
print(numbers)

numbers.extend([1, 2, 3])
print(numbers)

numbers.insert(2, 200)
print(numbers)

numbers.remove(200)
print(numbers)
