print('===========01==========')
# 1 Add two numbers using a function.
def add(a,b):
    
    return a+b
sum=add(5,8)
print(sum)



print('===========02==========')
# 2 Find the largest of three numbers.
number= [5,4,8,2,6,9]
def largest():
    return max(number)
lar = largest()
print(lar)




print('===========03==========')
# 3 Check whether a number is prime.

def prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime"

print(prime(5))   # Prime
print(prime(10))  # Not Prime
print(prime(13))  # Prime
print('===========04==========')
# 4 Find factorial using a function.

def factorial(num):
    new=1
    for i in range(1,num+1):
        new = new * i
    return new
print(factorial(5))
print('===========05==========')
# 5 Fibonacci using a function.
def fibonacci(num):
    first, second = 0, 1
    result = []
    for i in range(num):
        result.append(first)
        first, second = second, first + second
    return result

num = 5
print(fibonacci(num))


print('===========06==========')
# 6 Reverse a string using a function.
name= "Dhiraj"
def reverse():
    new= ""
    for i in name:
        
        new = i+new
    return new
print(reverse())
print('===========07==========')
# 7 Palindrome check using a function.
print('===========08==========')
# 8 Count vowels using a function.
print('===========09==========')
# 9 Find maximum element in a list.
print('===========10==========')
# 10 Calculate the average of a list.
print('===========11==========')
# 11 Add Two Numbers
num= [10,22,8,10]
def add_list():
    new=0
    for i in num:
        new = new + i
    return new
print(add_list())



print('===========12===========')
# Square

def square(a):
    return a*a

print(square(10))
print('===========13===========')
# Cube

def Cube(a):
    return a*a*a

print(Cube(3))
print('===========13===========')

# 14 Maximum Element in List


marks= [10,5,2,98,4,45,3]
def maximum():
    a=max(marks)
    return a

print(maximum())
