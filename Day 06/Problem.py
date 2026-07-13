# Q1 Create a dictionary. Print: Name ,Age ,City
man = {"name":"Dhiraj",
       "age": 23,
       "city":"Mumbai"}

print(man)


# Q2 Add:

man.update({"Course":"Python"})
print(man)

# Q3 Update:
man.update({"Course":"JS"})
print(man)

# Q4 Delete:

print(man.pop("age"))
print(man)

# Q5 Print all keys.


print(man.keys())

# Q6 Print all values.
print(man.values())

# Q7 Traverse dictionary using items().


for key,values  in man.items():
    print(key ,":", values)


# Q8 Character Frequency
words= "programming"
freq = {}

for i in words:
    if i in freq:
        freq[i] +=1
    else:
        freq[i]= 1

for key , values in freq.items():
    print(key,":",values)




# Q9 Word Frequency
sentence = "python django python flask python"

frequency = {}
for word in sentence.split():
    if word in frequency:
        frequency[word] += 1
    else :
        frequency[word] =1

for key , values in frequency.items():
    print(key,":",values)


# Q10 Find Highest Marks

marks = {
    "A":90,
    "B":85,
    "C":98,
    "D":88
}

# R?ule: Don't use max().
count= 0
for key ,values in marks.items(0):
    if values > count:
        count= values
print(count)