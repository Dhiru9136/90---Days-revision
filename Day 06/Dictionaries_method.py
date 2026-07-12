# Dictionary -> Data ko Key : Value pair ke form mein store karta hai.

# Key -> Data ko access karne ke liye use hoti hai.

# Value -> Key ke saath associated data hota hai.

# Dictionary mutable hai, isliye add, update aur delete kar sakte hain.

# Duplicate keys allow nahi hoti.

# Duplicate values allow hoti hain.

# Python 3.7+ mein Dictionary insertion order maintain karti hai.

# Nested Dictionary -> Ek dictionary ke andar doosri dictionary store hoti hai.

student = {
    "name": "Dhiraj",
    "age": 22,
    "city": "Mumbai"
}

print(student)

# keys() -> Dictionary ki sabhi keys return karta hai.
print(student.keys())

# values() -> Dictionary ki sabhi values return karta hai.
print(student.values())

# items() -> Dictionary ke sabhi key-value pairs return karta hai.
print(student.items())

# get() -> Di gayi key ki value return karta hai.
# Agar key nahi mile to None return karta hai.
print(student.get("age"))
print(student.get("subject"))

# update() -> Naya key-value pair add karta hai ya existing key ki value update karta hai.
student.update({"subject": "Python"})
print(student)

# pop() -> Di gayi key ko remove karke uski value return karta hai.
value = student.pop("age")
print(value)
print(student)

# popitem() -> Last inserted key-value pair remove karke return karta hai.
print(student.popitem())
print(student)

# copy() -> Dictionary ki shallow copy banata hai.
value = student.copy()
print(value)

# setdefault() -> Agar key exist nahi karti to default value ke saath add karta hai.
# Agar key pehle se hai to uski existing value return karta hai.
value.setdefault("age", 23)
print(value)

# clear() -> Dictionary ke saare key-value pairs remove kar deta hai.
student.clear()
print(student)