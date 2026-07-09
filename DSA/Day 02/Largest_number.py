# Bina max() use kiye maximum number find karo.

marks =[10,5,80,25,60]
def maximum():
    big= 0
    for i in marks:
        if i > big:
            big = i

    return big

print(maximum())