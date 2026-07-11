# Q1. Find Minimum (without min())
num = [5, 9, 6, 8, 5, 2, 4]
def minimum():
    mini= num[0]
    for i in num:
        if i < mini :
            mini= i
    return mini
print(minimum(), "Minimum")

# Time: O(n) (poori list ek baar traverse karte hain)
# Space: O(1) (sirf ek variable mini use hota hai)

# Q2. Find Maximum (without max())

num = [5, 9, 6, 8, 5, 2, 4]
def Maximum():
    mini= num[0]
    for i in num:
        if i > mini :
            mini= i
    return mini
print(Maximum(), "Maximum")

# Q3. Sum of Array
num = [5, 9, 6, 8, 5, 2, 4]
def sum_of_array():
    sum= 0
    for i in num:
        sum = i +sum
    return sum

print(sum_of_array(), "Sum of Array")


# Q4. Average of Array (without sum() and len())
num = [5, 9, 6, 8, 2, 4]
def sum_of_array():
    sum= 0
    count= 0
    for i in num:
        sum += i
        count += 1
    average = sum/count
    return sum ,average

print(sum_of_array(), "Sum of Array")

# Q5. Count Even and Odd Numbers

numbers = [1, 2, 3, 4, 5, 6, 7]
def Even_Odd():
    even = []
    odd = []
    for i in numbers:
        if i %2 ==0 :
            even.append(i)
        else:
            odd.append(i)
    return f"Even Number = {even}, Odd Number = {odd}" 
            
          
print(Even_Odd())

# Q6. Reverse List (without reverse())
numbers = [10, 20, 30, 40]
rev = numbers[::-1]
print(rev)
# Q7. Linear Search (Return Index)

numbers = [5, 8, 10, 15]
target = 10

def linear_search():
    for i in numbers:
        if i == 10:
            return( numbers.index(i))
        

print(linear_search())


# Q8. Second Largest Number (without sort())

numbers = [10, 25, 80, 45, 60]

lar= numbers[0]
sec_larg= numbers[0]
for i in numbers:
    if i > lar:
        sec_larg= lar
        lar = i
    elif i > sec_larg and i != lar:
        sec_larg = i



print(lar)
print(sec_larg)