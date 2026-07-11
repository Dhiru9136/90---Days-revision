# Without Third Variable

a=10
b=20
a,b=b,a
print(f'a={a},b={b} ')

# With Third Variable
a= 10
b=20
temp =a
a=b
b=temp
print(f'a={a},b={b}')

