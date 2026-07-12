# Print:

# First element
# Last element
# Slice (20,30,40)
numbers = (10, 20, 30, 40,10, 50)
sli= numbers[0::5]
print(sli)


# Q2 Count how many times 10 appears.
numbers = (10, 20, 30, 40,10, 50)
count= 0
for i in numbers:
    if i == 10:
        count +=1

print(count)

# Q3 Find index of 40.

for i in range(len(numbers)):
    if numbers[i] == 40 :
        print(i)

# Q4 Traverse tuple using for loop.
for i in numbers:
    print(i)



#Set

# Q5
number = {10,20,30}
# Add 40.
number.add(40)
print(number)

# Q6 Remove 20.
number.remove(20)
print(number)

# Q7 Union

A = {1,2,3}
B = {3,4,5}

print(A.union(B))


# Q8 Intersection

A = {1,2,3}
B = {3,4,5}

print(A.intersection(B))

# Q9 Difference

A = {1,2,3}
B = {3,4,5}

print(A.difference(B))



# Q10 Remove duplicates
numbers = [10,20,20,30,30,40]

my_set = set(numbers)
print(my_set)