numbers = {10, 20}

# add() -> Set mein ek naya element add karta hai.
numbers.add(30)
print(numbers)

# update() -> Ek ya ek se zyada elements (list, tuple, set, etc.) add karta hai.
numbers.update([30, 40])
print(numbers)

# remove() -> Specific element remove karta hai.
# Agar element nahi mila to KeyError aata hai.
numbers.remove(40)
print(numbers)

# discard() -> Specific element remove karta hai.
# Agar element nahi mila to koi error nahi aata.
numbers.discard(10)
print(numbers)

# pop() -> Set se ek random element remove karke return karta hai.
val = numbers.pop()
print(val)
print(numbers)

num = {10, 50, 60, 5}

# union() -> Do sets ke sabhi unique elements ko combine karke naya set return karta hai.
print(numbers.union(num))

# copy() -> Set ki shallow copy banata hai.
new_set = num.copy()
print(new_set)

b = {10, 20, 3, 60, 50}

# intersection() -> Dono sets ke common elements return karta hai.
print(num.intersection(b))

# difference() -> Sirf pehle set ke unique elements return karta hai.
print(num.difference(b))

# issubset() -> Check karta hai ki pehla set doosre set ka subset hai ya nahi.
print(num.issubset(b))

# clear() -> Set ke saare elements remove karke set ko empty kar deta hai.
numbers.clear()
print(numbers)