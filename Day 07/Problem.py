# Q1 Create student.txt.
# open("student.txt",'x')

# Q2 Read complete file.

n= open("student.txt",'r') 
print(n.read())
n.close()

# Q3 Read line by line.

m= open("student.txt",'r')
# print(m.readline())s
m.close()


# Q4 Append:

ap = open("student.txt",'a')
ap.write("\nPython")
print(ap)
ap.close()


# Q5 Count total lines.
# Count total lines and words

with open("student.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
words = data.split()

print("Total Lines:", len(lines))
print("Total Words:", len(words))