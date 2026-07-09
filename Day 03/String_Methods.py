name = "  Dhiraj  "
age= "32dhiraj"
age1= "32 dhiraj"
sur = "Pal"
print(len(name))

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.strip())#print(name.strip()) ka matlab hai ki string ke starting aur ending ke extra spaces ko hata diya jayega.
print(" ".join([name,sur]))#join() ka use strings ko jodne (concatenate) ke liye hota hai. Iska syntax thoda ulta hota hai:
print(name.count("j"))#string me kisi character ya substring kitni baar aaya hai uski counting karta hai.
print(name.find("h"))
print(name.index("h"))#string me kisi character ya substring ka pehla position (index) batata hai.
print(sur.startswith('P'))#check karta hai ki string kisi diye gaye character ya word se shuru hoti hai ya nahi.
print(sur.endswith('l'))#Check karta hai ki ending kisi diye gaye character ya word se end hoti hai ya nhi.
print(sur.isalpha()) #check karta hai ki string ke saare characters sirf letters (A-Z, a-z) hain ya nahi.
print(age.isdigit())#isdigit() check karta hai ki string ke saare characters digits (0–9) hain ya nahi.
print(age.isalnum()) #isalnum() check karta hai ki string me sirf alphabets (A-Z, a-z) aur digits (0-9) hain ya nahi.
print(age1.isalnum()) #isalnum() 1. Space hone ki wajah se False aaya. 2. check karta hai ki string me sirf alphabets (A-Z, a-z) aur digits (0-9) hain ya nahi.

