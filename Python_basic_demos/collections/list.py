# lists are mutable
Var = ["sam", "swo", "om"]
print(Var)


#  comprehension of list
print([x for x in Var if 's' in x])

def create_list(start, end):
    return [item for item in range(start, end + 1)]


s, e = 10, 20
l1 = create_list(s, e)
l2 = create_list(1, 10)

print(create_list(s, e))

l1[2] = "sam"
print(f"{l1} -> {len(l1)}")

l3 = l1 + l2
print(l1)
l3[2] = "this is changed"
print(l3)

l3 [1:4] = ["changed", "this one too"]

print(l3)



