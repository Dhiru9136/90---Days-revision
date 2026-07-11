# List
num = [5, 9, 6, 8, 5, 2, 4]

# insert() -> Kisi specific position (index) par element insert karta hai.
num.insert(1, 65)
print(num)

# append() -> List ke end me ek element add karta hai.
num.append(10)
print(num)

# remove() -> Di hui value ka pehla occurrence remove karta hai.
num.remove(10)
print(num)

# extend() -> Ek list ke end me dusri list ke saare elements add karta hai.
num.extend([8, 5, 9, 8])
print(num)

# insert() -> Kisi specific position (index) par element insert karta hai.
num.insert(1, 65)
print(num)

# copy() -> List ki shallow copy banata hai.
new = num.copy()
print(new)

# index() -> Di hui value ka pehla index return karta hai.
print(num.index(65))

# pop() -> Diye gaye index ka element remove karke return karta hai.
num.pop(-1)
print(num)

# count() -> Di hui value kitni baar aayi hai, uski counting return karta hai.
print(num.count(5))

# sort() -> List ko ascending order me sort karta hai.
num.sort()
# print(num)

# reverse() -> List ke elements ka order ulta kar deta hai.
num.reverse()
print(num,"reverse")

# copy() -> List ki shallow copy banata hai.
new = num.copy()
print(new)

# clear() -> List ke saare elements remove karke list ko empty kar deta hai.
num.clear()
print(num)