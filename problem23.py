# Program to to detect if the alaphabet is vowel or consonant.

a = input("Enter an alphabet:")

vowel = ["a", "e", "i", "o", "u", "A", "E", "O", "U"]
flag=1

for i in vowel:
    if i==a:
        print(f"{a} is a vowel.")
        flag=0
        break

if flag:
    print(f"{a} is a consonant.")