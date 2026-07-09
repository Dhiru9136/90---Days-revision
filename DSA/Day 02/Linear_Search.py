num=[5,8,10,15]
target= 152
def search():
    for i in num:
        if i == target:
            return 1
        
    return -1
        
        
print(search())