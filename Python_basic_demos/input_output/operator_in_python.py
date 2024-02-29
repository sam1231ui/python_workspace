# Arithmetic op
print(f"{1 + 2} -> {1 - 2} -> {1 * 2} -> {1 / 2} -> {1 // 2} -> {1 % 2} -> {2 ** 2}")

# Logical
print(f"{1 and 2} -> {1 or 2} -> {1 not in []}")

# Compare
print(f"{1 == 2} -> {1 != 2} -> {1 > 2} -> {1 < 2} -> {1 >= 2} -> {1 <= 2}")

# Bitwise (this works only on int values)
# AND return 1 if both have 1 operand
print(1 & 2)
print(1 & 5)

# OR return 1 if any have 1 operand
print(3 | 4)
print(1 | 5)

n = 24
ans = "Weird" if (n & 1) else ("Not Weird" if n in range(2, 6) else ("Weird" if n in range(6, 20) else "Not Weired"))

print(400%2 or 200%2)

s = "sam"
"s" if 1 < 2 else s = s[0]
print(s + "s")