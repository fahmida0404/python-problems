import random
import string
print("\t\tSecret Code Language")
a=input("Enter 1 for encoding and 2 for decoding:")
if(a=='1'):
    msg=input("Enter your message to encode:")
    w=msg.split(" ")
    new=[]
    for i in w:
        if(len(i)<3):
            c=list(i)
            c.reverse()
            x="".join(c)
            
        else:
            r=''.join(random.choices(string.ascii_letters,k=3))
            c=list(i)
            c.extend(c[0])
            c.pop(0)
            c.insert(0,r)
            x="".join(c)
        new.append(x)
    print(" ".join(new))
else:
    msg=input("Enter code to decode:")
    w=msg.split(" ")
    new=[]
    for i in w:
        if(len(i)<3):
            c=list(i)
            c.reverse()
            x="".join(c)
        else:
            r=len(i)-4
            c=list(i)
            del c[:3]
            c.insert(0,c[r])
            c.pop(r+1)
            x="".join(c)
        new.append(x)
    print(" ".join(new))