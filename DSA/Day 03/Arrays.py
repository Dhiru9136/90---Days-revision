# Q2 Find Minimum (without min())
num = [4,5,2,9,6,23]
count =num[0]
for i in num:
    if count > i:
        count = i
print(count)

# Q3 Find Maximum (without max())
maxi = num[0]
for i in num:
    if maxi < i:
        maxi = i
print(maxi)

# Q4 Sum of Array
sum =0
for i in num:
    sum = i+ sum
print(sum)



