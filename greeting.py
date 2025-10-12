# Program to print greetings based on time

import time
time=time.strftime('%H')
if((time>='0') and (time<'12')):
    print("Good Morning Sir")
elif((time>='12') and (time<'18')):
    print("Good Afternoon Sir")
elif((time>='18') and (time<'24')):
    print("Good Evening Sir")







