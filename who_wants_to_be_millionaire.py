print("\t\tWho wants to be a Millionaire")
print("Game Rules:")
print("For each correct answer you will get 5000 Tk")
print("For one incorrect answer the game is over\nand you will go home with the money you won")
Q=["Is Python case sensitive when dealing with identifiers?","All keywords in Python are in _____?","Which of the following is used to define a block of code in Python language?","Which of the following character is used to give single-line comments in Python?","What does pip stand for python?"]
Ans=["A","B","A","D","C"]
A=["Yes","Capitalized","Indention","/*","pip install python"]
B=["No","Lowercase","Key","<!","pip install packages"]
C=["Both","Uppercase","Brackets","//","Preferred installer program"]
D=["None","None","All","#","None"]
n=range(0,5,1)
tk=0
for i in n:
    print("\n",Q[i],"\n")
    print("A",f"{A[i] :<30}",f"{'B' :>10}",B[i]) #space alignment with f-string
    print("C",f"{C[i] :<30}",f"{'D' :>10}",D[i])
    a=input("\nChoose an option: (uppercase only)")
    if(a==Ans[i]):
        tk=tk+5000
        print("Congratulaitons! The answer is correct.\nYou have won ",+tk,"tk")
    else:
        print("Sorry! The answer is incorrect.\nYou will have to go home with ",+tk,"tk")
        print("\n\t\tGame Over")
        break
        
