# Q1. Count Vowels (Function)
vowel= "aeiou"
name = "programming"
def vol():
    count=0
    for i in vowel:
        for j in name:
            if i==j:
                count +=1
    return count
print(vol())


# Q2. Count Consonants
Consonants="B C D F G H J K L M N P Q R S T V W X Y Z"
name = "programming"
def con():
    count =0
    for i in Consonants.lower():
        for j in name:
            if i==j:
                count +=1
    return count
print(con())


# Q3. Reverse String (Without [::-1])
name= "Dhiraj"
def reverse():
    rev = ""
    for i in name:
        rev = i + rev
    return rev
print(reverse())

# Q4. Palindrome
print("Palindrome")
name = 'madam'
def palin():
    rev = ""
    for i in name:
        rev = i+rev

    if name == rev:
        return "Palindrome"
    else :
        return "not a Palindrome"
    
print(palin())
# Q5. Count Uppercase & Lowercase
name= "Dhiraj Pal"
def count():
    upper =0
    lower = 0
    for i in name:
        if i.isupper():
            upper+=1
        else:
            lower+=1
    return upper, lower

print(count())

# Q6. Remove Spaces
name = "Dhiraj Pal"
def remove():
    return name.replace(" ","")
print(remove())
# Q7. Replace Word
name= "Dhiraj"
def replace():
    return name.replace('Dhiraj','Pal')
print(replace())
# Q8. Count Word Frequency (Basic)
sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)