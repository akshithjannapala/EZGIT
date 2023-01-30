#!/usr/bin/env python
# coding: utf-8

# In[ ]:


choice=input()
arr=['ROCK','paper','scessor']
rock=1,paper=2
scessor=3


# In[1]:


import random
arr=['ROCK','paper','scessor']
scount=0
ucount=0
while True:
    choice=input("enter choice")
    a=random.choice(arr)
    if(a==choice):
        print("TIE GAME")
    elif(choice==arr[0] and a==arr[1]):
        print("user has won the game ")
        ucount=ucount+1
    elif(choice==arr[1] and a==arr[0]):
        print("system has won ")
        scount=scount+1
    elif(choice==arr[0] and a==arr[2]):
        print("USER has won ")
        ucount=ucount+1
    elif(choice==arr[1] and a==arr[0]):
        print("system has won ")
        scount=scount+1
    elif(choice==arr[2] and a==arr[1]):
        print("system has won ")
        scount=scount+1
    elif(choice==arr[1] and a==arr[2]):
        print("system has won ")
        scount=scount+1
    if(scount==5):
        print("system has won")
        break
    elif(ucount==5):
        print("user has won ")
        break
    


# In[ ]:





# In[ ]:




