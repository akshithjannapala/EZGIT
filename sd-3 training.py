#!/usr/bin/env python
# coding: utf-8

# In[36]:


#happy number program
def happy(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum
num=int(input("enter the number"))
result=num
while(result!=1 and result!=4):
    result=happy(result)
    
if result==1:
    print("happy number bro")
else:
    print("iam not happy bro")


# In[35]:


#harsh number
def happy(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=num//10
    return sum
num=int(input("enter the number"))
result=num
flag=happy(result)
if num%flag==0:
    print("iam a harsh number")
else:
    print("iam not a harsh number")


# In[38]:


#farhenhit to celcius
fa=float(input("enter the value"))
ce=(0.58)*(fa-32)
print(ce)


# In[41]:


#check weather the number is potitive or not 
num=int(input(" enter the nunmber"))
if num>0:
    print("positive number")
else:
    print(" negative number")


# In[ ]:


#palindrome
frount to back same
ex:level
#symmetrical
if we divide a strin  into half the the two halfs will be same 
ex:noon
#anagram
same alphabets with different arrangements
ex:listen-silent
#TOM_RIDDLES
splitting a single word and forming differnt meaningfull words
ex:HARRY PORTER-TRY HERO PORT


# In[45]:


#WRITE A PROGRAM TO FIND A TEXT WEATHER IIT IS PRESENT IN A GIVEN TEXT OR NOT
sen=str(input("enter the text"))
flag="is"
if flag in sen:
        print(" yes it is there")
else:
        print(" no it is not present")


# In[47]:


sen="mississippi"
print(sen.split("s"))


# In[49]:


#multi line strings
abc="""
netherlands
australia
greece"""
print(abc)


# In[57]:


#method by using sum
def ls(string):
return sum(l for i in string)
string='india'
print(ls(string))


# In[62]:


def ls(str):
    c=0
    for i in str:
        c+=1
    return c
str="hi"
print(ls(str))


# In[64]:


def ls(str):
    if not str:
        return 0
    else r_str='py'
    return ((r_str).join(str).c(r_str)+l)
str="india"
print(ls(str))


# In[ ]:


upper()
lower()
partition()---return a tuple
find()-----it returns the index values of first substring
replace()----replacing the substring
split()---
startswith()---
endswith()---
index()--returns the index value


# In[71]:


name='akshith'
country='india'
print(f'{name}  is born in {country}')


# # sets

# In[ ]:


a={1,2,3,4,5,6,7,8}
b={3,4,6}


# In[ ]:


longest common subset or sebsequence


# In[ ]:


2^n-1----calculate the number of ways to find the possible outputs in tower of annoy


# In[72]:


set={1,2,3,4}
set1={2.0,(1,2,3),"abc"}
print(set)
print(set1)


# In[ ]:


we cant have duplicate elements in set


# In[74]:


#modifying  set 
#1)adding a new element
#2)UPDATING
m_set={1,2}
m_set.add(3)
m_set
m_set.update([4,5,6])
m_set


# In[75]:


m_set.update([6,7],{1,5,7})
m_set


# In[ ]:





# In[113]:


m_set=set("acdef")
print(m_set)
print(m_set.pop())


# In[140]:


total = 10
candies_wanted = int(input("enter number of candies u want"))
Candies_available=total-candies_wanted
if Candies_available<=5:
    print('No. of Candies Sold:',candies_wanted)
    print('No. of Candies available:',total-candies_wanted)
    print("candies after filing is ",candies_wanted+Candies_available)
else:
    print("candies not available")
   


# In[1]:


size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)
for i in range(0,size):
    if arr[i]=='1':
        count=count+1
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)


# In[3]:


i=0
while(i<=10):
    print(i,)
    i=i+1


# In[2]:


i=0
while(i<=10):
    print(i,end=" ")
    i=i+1


# In[4]:


i=0
while(i<=10):
    print(i,end="\t")
    i=i+1


# In[12]:


#write  a program  to add the elements between the range to (m,n)
m=int(input("enter m value"))
n=int(input("enter the n value"))
c=0
i=0
while(m<=n):
    c=c+m
    m=m+1
print(c)


# In[20]:


#write a program to fing the sum of digits in a number
num=int(input("enter the number"))
rem=0
sum=0
while(num>0):
        rem=num%10
        sum=sum+(rem)
        num=num//10
print(sum)


# In[ ]:


#write a program to fing the number is nivens number
num=int(input("enter the number"))
rem=0
sum=0
temp=num
while(num>0):
        rem=temp%10
        sum=sum+(rem)
        temp=temp//10
print(sum)
rem1=num%sum
if rem1==0:
    print("nivens number")
else:
    print("not a nivens number")


# In[ ]:


#reversing of a number using type conversion
num=int(input("enter the number"))
n_str=str(num)
temp=print(n_str[::-1],end=" ")


# In[ ]:


#revese of a number
num=int(input("enter the number"))
rem=0
temp=num
while(temp>0):
        rem=temp%10
        print(rem,end="\t")
        temp=temp//10


# In[12]:


#printing 10 numbers, adding them and finding the average of the numbers
i=0
sum=0
num=int(input("enter the number"))
for i in range(0,num+1):
    sum=sum+i
    i=i+1
    print(i)
print("sum is ",sum)
temp=sum/10
print("average is ",temp)


# In[22]:


#table or multiple of a numbers upto 10
num=int(input("enter the number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


# In[27]:


for i in range(1900,2101):
    if  i%4==0:
        print(i,end=" ")
    


# In[22]:


li=[]
n=int(input("enter size"))
if(n==0):
    print("invalid input")
else:
    for i in range(0,n):
        ele=int(input("enter elements"))
        li.append(ele)
print(swap(li, 0, n))


# In[29]:



for i in range(1900,2101,4):
    print(i)


# In[37]:



sum=0
num=int(input("enter the number"))
for i in range(1,num+1):
    sum=sum+1.0/i
    print(sum)


# In[39]:



sum=0
num=int(input("enter the number"))
for i in range(1,num+1):
    sum=sum+(1.0/i*1.0/i)
    print(sum)


# In[41]:


#center tag in string--puts the string i the middle 
str="hi"
print(str.center(10,'$'))


# In[93]:


str="he"
substr="hehellhehell"
print(substr.count(str,0,len(substr)))


# In[98]:


#syntax for zfill width
str='14'
print(str.zfill(4))


# In[101]:


str='akshith'
str.title()


# In[103]:


str='akshith'
str.swapcase()


# In[104]:


str.upper()


# In[106]:


str.lower()


# In[107]:


print(list(enumerate(str)))


# In[5]:


#table or multiple of a numbers upto 10

li=[0,0]
m=0
s=0
for i in range(1,11):
   m=m+7
   li.append(m)
   s=s+6
   li.append(s)
print(li)
pos=int(input("enter the position"))
print(li[pos])

    


# In[6]:


li=[1,1]
for i in range(1,18):
   m=2**i
   li.append(m)
   s=3**i
   li.append(s)
print(li)
pos=int(input("enter the position"))
print(li[pos])


# In[115]:


str="INDIA"
for i in str:
    print(i,end="\t")


# In[ ]:


str=int(input("enter the number to encode"))
num=int(input("enter the key value"))
while(num<str[i]):
    letter=int[num]
    print(int(ord(letter)+num),end=" ")
    num=num+1
    


# In[ ]:


#caser cipher
str="india"
index=0
while index<len(str):
    letter=str[index]
    print(chr(ord(letter)+2),end=" ")
    index=+1


# In[ ]:


#caser cipher
str="india"
index=0
while index<len(str):
    letter=str[index]
    print(chr(ord(letter)+2),end=" ")
    index=+1


# In[ ]:


0 0 7  6  14 12 21 18 ................


# In[ ]:


#table or multiple of a numbers upto 10
for i in range(1,11):
    if(i%2==0):
        print(6*i)
    else: 
        print(7*i)
    


# In[20]:


str1="abcdef"
str2="ate"
for i in str1:
    print(i+str2,end=" ")


# # patterns
# #1)basic patterns
# #2)mirror image patterns
# #3)symmetric patterns
# #4)choice of patterns
# #5)anti-patterns/hallow patterns

# In[66]:


num=int(input("enter the number"))
a="akshith"
for i in range(num):
    print(a*i)


# In[ ]:





# In[32]:


num=int(input("enter the number"))
a="*"
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")


# In[42]:


num=int(input("enter the number"))
a="*"
for i in range(num):
    for j in range(num-i):
        print(,end=" ")
    print("\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[33]:


num=int(input("enter the number"))
a="*"
for i in range(num,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print("\n")


# In[35]:


num=int(input("enter the number"))
a="*"
for i in range(1,num+1):
    for j in range(1,num+i):
        if(j>i):
            print(' ',end=" ")
            
        else:
            print()
        print(j+1,end=" ")
    print("\n")


# In[46]:


num=int(input("enter the number"))
a="*"
for i in range(num):
    for j in range(num-i):
        print(j+1,end=" ")
    print("\n")


# In[43]:


num=int(input("enter the number"))
a="*"
for i in range(num):
    for j in range(num+1):
        print(j+1,end=" ")
    print("\n")


# In[94]:


num=int(input("enter the number"))
for i in range(num):
    for j in range(i+1):
        if(j>i):
            print(' ',end=" ")
        else:
            print(j,end=" ")
    print("\n")       
            


# In[64]:


num=int(input("enter the number"))
for i in range(-1,0,num):
    for j in range(i,0):
        if(j>i):
            print(' ',end=" ")
        else:
            print(j,end=" ")
    print("\n")       
            


# In[86]:


str1=(input("enter the text"))
for i in range(len(str)):
    for j in range(i+1):
        print(str[j],end=" ")
    print("\n")


# In[92]:


a=65
r=14
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a=a+1
    print(" ")


# In[93]:


a=65
r=14
m=(2*a)-2
for i in range(0,r):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a=a+1
    print(" ")


# In[ ]:


#write a program to print pattern of 10 lines evaluating vertical  to a right angled ttriangle


# In[118]:


num=int(input("enter the number"))
i=1
for i in range(num):
    for j in range(1,i+1):
        if(j>i):
            print(' ',end=" ")
        else:
            print(j*i,end=" ")
    print("\n")       
            


# In[122]:


#functions in python
def username(name):
    return name
def add(a,b):
    return a+b,b-a
name1=input("enter the name")
result=username(name1)
print(result)
result1=add(10,20)
print(result1)


# In[125]:


#functions in python
def username(name):
    print(name)
def add(a,b):
    print(a+b)
    print(b-a)
name1=input(" enter the name")
username(name1)
result1=add(10,20)


# In[4]:


#display a string n number of times
def rep(str):
    for i in range(1,20):
        print(str)
user=input("enter the string")
rep(user)


# In[ ]:





# In[14]:


a=int(input("enter the number"))
b=int(input("enter the number"))
while():
    for i in range(a+b/2):
            if(i%j==0):
                print(j)


# In[8]:


#golbal variable accessing 
var1="hi"
def abc():
    global var2
    var2="good morning"
    print("in the function var1 is -",var1)
abc()
print("outside the function is var2-",var2)
print("var1 is -",var1)


# In[11]:


#program to demo access of var in inner and outer function
def out_fn():
    var=11
    def inner_fun():
        var=22
        print(" outer variable",var)
    inner_fun()
    print(" outer variable",var)
out_fn()


# In[16]:


#write a function and return its cubation format
def cude(num):
    return (num*num*num)
num=int(input("enter the number"))
cude(num)


# In[17]:


#program to demo key args
def display(str,int_x,float_y):
    print("the string is ",str)
    print("the integer is ",int_x)
    print("the float is ",float_y)
display(float_y=5678.9998,str="hi",int_x=1234)


# In[18]:


#program to demo key args
def display(name,age,salary):
    print("the string is ",name)
    print("the integer is ",age)
    print("the float is ",salary)
a='vijay'
b=32
c=123456789
display(name=a,age=b,salary=c)


# In[19]:


#lambda functions
addition=lambda x,y:x+y
print("sum=",addition(10,20))


# In[21]:


addition=lambda x,y,z:x+y+z
print("sum is ",addition(10,20,30))


# In[ ]:


#key functions of lambda function
lambda function has no names
it can take n nuumber of attributes
it can onlly return one value
*lambda function cannot access global variables
it cannot access var other than their parameters list
cannot contain multi parameters 
it doesnt have explicit statements


# In[22]:


def small(a,b):
    if(a<b):
        return a
    else:
        return b
add = lambda x,y:x+y
diff = lambda x,y:x-y
print("smaller of two numbers:",small(add(-9,7),diff(-2,6)))


# In[23]:


#program to pass lambda
def increment(y):
    return (lambda x:x+1)(y)
a=100
print("a=",a)
print("a after incrementing")
b=increment(a)
print(b)


# In[24]:


#program to pass a lambda fun as an fun arg
def fun(f,n):
    print(f(n))
twice=lambda x:x*2
triple=lambda x:x*3
fun(twice,4)
fun(triple,3)


# In[25]:


add=lambda x,y:x+y
m_add=lambda x,y,z:x*add(y,z)
print(m_add(3,4,5))


# In[3]:


#swapping of two numbers using functions
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
swap(2,3)


# In[8]:


#write a program to return the full name of a persom 
#where fst variable passed is firest name 
#2nd variable passes is last name
f_name=str(input("enter first name"))
l_name=str(input("enter last name"))
def disp(f_name,l_name):
    return f_name+" "+ l_name
disp(f_name,l_name)


# In[12]:


num=int(input(" enter number"))
def even(a):
        if(a%2==0):
            print(" number is even")
        else:
            print(" number is not even")
even(num)


# In[21]:


#write a program to calculate si.suppose the coustomer is a senior citizen
#he is being offered 12% roi for all other customers,the rot is 10% 
p=200
t=3
age=int(input("enter the age"))
if(age>60):
    print((p*t*12)/100)
else:
     print((p*t*10)/100)
    


# In[33]:


def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
a = int(input("enter a number"))
print(fact(a))


# In[ ]:


import numpy as np
num=int(input("engter the number"))
a=[]
arr=[]
arr1=[]
rem=0
for i in range(0,num):
    l=int(input())
    a.append(l)

while(num>0):
    a=a%10
    if(a%2==0):
        arr.append(rem)
    else:
        arr1.append(rem)
    a=a//10
con=np.array(arr)
con1=np.array(arr1)

print(con)
print(con1)


# 3
# 4## import numpy as np
# my_list =[4, 2]
# my_array = np. array(my_list)
# my_array

# In[65]:


li=[4,3,2,1]
print(li.sort())


# In[ ]:


def sort():
    while(li>0):
        


# In[51]:


def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods


# In[53]:


def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print(a,b,c)
hanoi(len(a),a,b,c)


# In[70]:



arr=int(input())
for i in range(arr):
    print(arr)


# In[74]:


a=[]
b=[]
c=[]
num=int(input("engter the number"))
for i in range(0,num):
    l=int(input())
    a.append(l)
print(a)
if i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)
        
        


# In[ ]:


string=input()
sum=0
for i in range(0,len(string)):
    sum+=ord(string[i])
print(sum)


# In[1]:


import numpy as np
num=int(input("engter the number"))
arr=[]
arr1=[]
rem=0
while(num>0):
    rem=num%10
    if(rem%2==0):
        arr.append(rem)
    else:
        arr1.append(rem)
    num=num//10
con=np.array(arr)
con1=np.array(arr1)
d=con+con1


# In[ ]:


li=[]
arr=[]
arr1=[]
rem=0
n=int(input("enter size"))
for i in range(0,n):
    ele=int(input("enter elements"))
    li.append(ele)
for i in range(0,n):
    if(li[i]%2==0):
        arr.append(li[i])
    else:
        arr1.append(li[i])
print(arr)
print(arr1)


# import numpy as np
# li=[]
# arr=[]
# arr1=[]
# new=[]
# new1=[]
# n=int(input("enter size"))
# for i in range(0,n):
#     ele=int(input("enter elements"))
#     li.append(ele)
# for i in range(0,n):
#     if(li[i]%2==0):
#         arr.append(li[i])
#     else:
#         arr1.append(li[i])
# new=arr+arr1
# print(new)

# In[ ]:





# In[20]:


import numpy as np
li=[]
arr=[]
arr1=[]
new=[]
new1=[]
n=int(input("enter size"))
for i in range(0,n):
    ele=int(input("enter elements"))
    li.append(ele)
for i in range(0,n):
    if(li[i]%2==0):
        arr.append(li[i])
    else:a
        arr1.append(li[i])
new=arr+arr1
print(new)


# In[22]:


import numpy as np
li=[]
arr=[]
arr1=[]
new=[]
new1=[]
n=int((input("enter size"))
ele=input("enter elements").split()
li.append(ele)
for i in range(0,n):
    if(li[i]%2==0):
        arr.append(li[i])
    else:
        arr1.append(li[i])
new=arr+arr1
print(new)


# In[7]:


2num=int(input("enter size"))
for i in range(0,num):
    ele=int(input("enter the elements"))
for i in range(0,6):
    rem=ele%10
    sum=sum*rem
    ele=ele//10
print(sum)


# In[8]:


#happy number program
def happy(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum*rem
        num=num//10
    return sum
num=int(input("enter the number"))
result=num
result=happy(result)
print(result)


# In[3]:



#multiplication  in an array
li=[]
n=int(input("enter size"))
if(n<=0):
    print("invalid input")
    result=0
else:
    for i in range(0,n):
        ele=int(input("enter elements"))
        li.append(ele)
        result = 1
        for i in li:
            result = result * i
if(result!=0):
    print(result)


# In[2]:


#swappin in a annay
def swap(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
li=[]
n=int(input("enter size"))
if(n==0):
    print("invalid input")
else:
    for i in range(0,n):
        ele=int(input("enter elements"))
        li.append(ele)
print(swap(li, 0, n))


# In[23]:


#program to access var using a class object
class abc:
    var=22
obj=abc()
print(obj.var)


# In[24]:


class abc:
    var=22
    def display(self):
        print(" this is class method")
obj=abc()
print(obj.var)
obj.display()


# In[25]:


class abc():
    var=22
    var1=222
obj=abc()
print(obj.var)
print(obj.var1)


# In[28]:


#program to illustrate the constructor
#__init__()...method
class abc:
    def __init__(self,val):
        print("in class method")
        self.val=val
        print("this is :",val)
obj=abc(10)


# In[30]:


class abc:
    def __init__(self,a,b):
        self.a,b=a,b
        print("value of a ,b is ",a+b)
obj=abc(5,6)


# In[36]:


#program to differentiate btw class and object variable
class abc():
    class_var=0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print(" object variable is",var)
        print("class variable is ",abc.class_var)
obj=abc(10)
obj=abc(10)
obj=abc(10)


# In[59]:


class abc:
    even=[]
    odd=[]
    def __init__(self,n):
        self.n=n
        if(n%2==0):
            abc.even.append(n)
        else:
            abc.odd.append(n)
        
n1=abc(2)
n2=abc(3)
n3=abc(5)
n4=abc(8)
print(abc.even)
print(abc.odd)
even_odd=abc.even+abc.odd
print(even_odd)



    


# In[60]:


class abc:
    even=[]
    odd=[]
    def __init__(self,n):
        self.n=n
        if(n%2==0):
            abc.even.append(n)
        else:
            abc.odd.append(n)
        
n1=int(input("enter number")
abc(n1)
n2=int(input("enter number")
abc(n2)
n3=int(input("enter number")
abc(n3)
n4=int(input("enter number")
abc(n4)
even_odd=abc.even+abc.odd
print(even_odd)



    


# In[66]:


#delete method-------c++ java analogus to destructors
#general syntax _del_
class abc():
    class_var=0
    def _init_(self,var):
        abc.class_var+=1
        self.var=var
        print("the object value is",var)
        print("the class value is",abc.class_var)
    def _del_(self):
        abc.class_var-=1
        print("object with value %d is going out of scope "%self.var)
obj1=abc(11)
obj2=abc(22)
obj3=abc(33)
del obj1
del obj2
del obj3


# In[ ]:


#1)__repr__ ----- syntax report of the object
#__cmp__ ---- compares two class objects
#__len__ --len(object)
#__call__ --it acts like a func to call its instances
#__it__,__le__,__eq__,__ne__,__gt__ ,__cmp__
#__iter__ iteration over a object
#__getitem__ used for indexing
#gs:def __getitem__(self,var/key)
#set item assign an item to the indexed value


# In[70]:


#program to demonstrate get and set item in list

class num:
    def _init_(self,mylist):
        self.mylist=mylist
    def _getitem_(self,index):
        return self.mylist[index]
    def _setitem_(self,index,val):
        self.mylist[index]=val
numlist=num([1,2,3,4,5,6,7,8,9])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)


# In[1]:


class abc():
    def _init_(self,name, var):
        self.name=name
        self.var=var
    def _repr_(self):
        return repr(self.var)
    def _len_(self):
        return len(self.name)
    def _cmp_(self):
        return self.var-obj.var
    
obj = abc("ghijkl",1)
print("the value stored in obj is: ",repr(obj))
print("the length of the name storted in obj: ",len(obj))
obj1 = abc("ghijkl",1)

val = obj._cmp_(obj1)
if val==0:
    print("both values are equal")
elif val==-1:
    print("1st value is less than 2nd")
else:
    print("2nd value is lessthan 1st")


# In[8]:


#is for illustrating use of a private method
class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("this is from class method,var=" ,self.__var)
obj=abc(10)
obj._abc__display()


# In[10]:


def fibbo(num):
    if (num<2):
        return 1
    else:
        return (fibbo(num-1)+fibbo(num-2))
for i in range(num):
    print(fibbo(i))
    


# In[11]:


#program to show how a class method calls a function
#which defined in the global name space
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is=",self.var)
    def modify(self):
        self.var=scale_10(self.var)
obj=abc(10)
obj.display()
obj.modify()
obj.display()


# In[ ]:


#built-in attributes
#for get set and delete
1..hasattr(obj,name)-checks obj possesses the attributes values or not 
2..getattr(obj,name[,default])
3..setattr(obj,name,value)-which is used to set an attribute of the object
4..delattr(obj,name)---deleting item


# In[12]:


#program to demo builtin
class abc():
    def __init__(self,var):
        self.var=var
        def display(self):
            print("varis ",sself.var)
obj=abc(10)
obj.display()
print("check weather obj has attributes var")
getattr(obj,'var')
setattr(obj,'var',50)
print("after setting valu ,vas is",obj.var )
setattr(obj,'count',10)
print("new variable count is cfreated and its value =",obj.count)
delattr(obj,'var')
print("after deleting tyhe attr,var is :",obj.var)


# In[ ]:


built in class attributes
1. .__dict__
2. .__doc__
3. .__name__
4


# In[13]:


class abc():
    def _init_(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1 is :",self.var1)
        print("var2 is :",self.var2)
obj=abc(10,20.65)
obj.display()
print("object._dict-",obj.__dict_)
print("object._doc-",obj.__doc_)
print("object._namme-",abc.__name_)
print("object._module-",obj.__module_)
print("object._bases-",abc.__bases_)


# In[21]:


# n chunks 
li=[]
li1=[]
n=int(input("enter size"))
if(n%2==1):
    print("invalid input")
else:
    for i in range(0,n):
        ele=int(input("enter elements"))
        li.append(ele)
k=int(input("enter the size to divide"))
for i in range(0,k):
        if i!=k:
            li1.append(li)
            print(li1)
            


# In[27]:


n=int(input())
b=[]
c=[]
l=[int(i) for i in input().split()][:n]
for i in range(1,n+1):
    if(i%2==0):
        b.append(i)
    else:
        c.append(i)
d=b+c
print(d)


# In[1]:


import gc
print("garbage collection threshold",gc.get_threshold())


# In[2]:


#abstract class
#abstract determination example
class fruits:
    def  taste(self):
        raise NotImplemetedError()
        #abs lacks required derived class
    def rich(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruits):
    def taste(self):
        return "sweet"
    def rich(self):
        return "Vitamine A"
    def color(self):
        return "orange"
Alphanso = mango()
print(Alphanso.taste(),Alphanso.rich(),Alphanso.color())


# In[8]:


#program to interviene polymorphism on a complex number
class complex():
    def __init__(self):
        self.real=0
        self.img=0
    def setValue(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,c):
        temp=complex()
        temp.real=self.real+c.real
        temp.img=self.img+c.img
        return temp
    def display(self):
        print("(",self.real,"+",self.img,"i)")
c1=complex()
c1.setValue(1,2)
c2=complex()
c2.setValue(3,4)
c3=c1+c2
print("result is ....")
c3.display()


# In[ ]:


#OPERATORS---------FUNCTION NAME
+   __add__
+=  __iadd__
-  __sub__
-=  __isub__
*   __mul__
*=   __imul__
__truediv__()
(=, __idiv__)
**  __pow__
**=  __ipow__
get_ipython().run_line_magic('__mod__', '')
get_ipython().run_line_magic('=', ' __imod___')
>>  __rshift__
>>= __irshift__
&   __and__
&=  __iand__
|   __or__
|=  __ior__
^   __xor__
^= __ixor__
~  __invert__
~= __iinvert__
> __gt__
< __lt__
>= __ge__
<= __le__


# In[12]:


#program that has abstract class to drive 2 classes
#rectangle and triangle from polgon class and
#write the methods to get their details and dimensions
#and hence calculate the area respectlively
class polygon:
    def get_data(self):
        raise notImplementedError()
    def area(self):
        raise notimplemenetedError()
class rectangle(polygon):
    def get_data(self):
        self.length=float(input("Enter rectangle length="))
        self.breadth=float(input("Enter rectangle breadth="))
    def area(self):
        return self.length*self.breadth
class triangle(polygon):
    def get_data(self):
        self.base=float(input("Enter triangle base="))
        self.height=float(input("Enter triangle height="))
    def area(self):
        return 0.5*self.base*self.height
R=rectangle()
R.get_data()
print("area of a rectangle",R.area())
T=triangle()
T.get_data()
print("area of a triangle",T.area())


# In[15]:


#encapsulation public members
class pub:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def Num(self):
        print("roll number is ",self.num)
obj=pub("harry",2009)
obj.Num()


# In[20]:


#program to overload the __call__method
class multi:
    def __init__(self,num):
        self.num=num
    def __call__(self,O):
        return self.num*O
x=multi(10)
print(x(5))


# In[31]:


#PROGRAM TO OVER-RIDE GET-ITEM AND SET=-ITEM METHODS
class mylist:
    def __init__(self,list):
        self.list=list
        
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,num):
        self.list[index]=num
    def __len__(self):
        return len(self.list)
    def display(self):
        print(self.list)
L=mylist([1,2,3,4,5,6,7,8,9])
print("list is...............")
L.display()
index=int(input("enter the index"))
print(L[index])
index=int(input(" enter the index"))
num=int(input(" enter the position u want to modify"))
L[index]=num
L.display()
print("the length of list is ",len(L))


# In[ ]:


#special or miscellaneous functions in overloading
 class number:
        def __init__(self,num):
            self.num=num
        def display(self):
            return self.num


# In[32]:


class number:
    def _init_(self,num):
        self.num=num
    def display(self):
        return self.num
    def _abs_(self):
        return abs(self.num)
    def _float_(self):
        return float(self.num)
    def _hex_(self):
        return hex(self.num)
    def _oct_(self):
        return oct(self.num)
    def _setitem_(self,num):
        self.num=num
n=number(14)
print("n is=",n.display())
print("abs(n) is=",abs(n))
n=abs(n)
print("coverting to float",float(n))
print("coverting to hexa",hex(n))
print("coverting to octal",oct(n))


# In[35]:


#to visualize inheritance flow
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",self.name)
        print("age is",self.age)
class teacher(person):
        def __init__(self,name,age,exp,rarea):
            person.__init__(self,name,age)
            self.exp=exp
            self.rarea=rarea
        def displaydata(self):
            person.display(self)
            print(("experience is ",self.exp))
            print("rarea is ",self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):      
        person.display(self)
        print("course=",self.course)
        print("marks=",self.marks)
print(".....................teacherclass..............")
t=teacher("mark",43,20,"jss")
t.displaydata()
print("............student class/........")
s=student("akshith",23,"bee",89)
s.displaydata()

        
            


# In[47]:


#to visualize inheritance flow
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",self.name)
        print("age is",self.age)
class teacher(person):
        def __init__(self,name,age,exp,rarea):
            person.__init__(self,name,age)
            self.exp=exp
            self.rarea=rarea
        def displaydata(self):
            person.display(self)
            print(("experience is ",self.exp))
            print("rarea is ",self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):      
        person.display(self)
        print("course=",self.course)
        print("marks=",self.marks)
print(".....................teacherclass..............")
t=teacher("mark",43,20,"jss")
t.displaydata()
print("............student class/........")
s=student("akshith",23,"bee",89)
s.displaydata()
print(" t is a teacher:",isinstance(t,teacher))
print(" t is a person:",isinstance(t,person))
print(" t is a object:",isinstance(t,object))


# In[38]:


#program to invoke __init__ in multiple inheritance
class base1(object):
    def __init__(self):
        print("base class 1")
class base2(object):
        def __init__(self):
            print("base class 2")
class derived(base1,base2):
    pass
d=derived()
            


# In[45]:


# program to call constructor of a base class from super class
#program to invoke __init__ in multiple inheritance
class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
        def __init__(self):
            print("base class 2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived class")
d=derived()
            


# In[48]:


class person:
    def name(self):
        print("name is....")
class teacher(person):
    def qual(self):
        print("qualification is phd")
class hod(teacher):
    def expr(self):
        print("experience is 22 yrs")
HOD=hod()
HOD.name()
HOD.qual()
HOD.expr()


# In[ ]:


#multi path inheritance
class student:
    def name(self):
        print("name......")
class academic(students):
    def acad_score(self):
        print("academic score 90% above")
class eee(student):
    def eligibility(self):
        print("-------------------- eligible")
        self.acad_score()
        self.eee_score()
r=result()
r.eligibility()


# In[3]:


n=int(input())
if n<=0:
    print("Invalid Input")
else:

 l=input()
 x=l.split(" ")
 f=[]
 flo=[]
 fle=[]
 fl=[]
 for i in range(0,n):
    f.append(int(x[i]))
 f.sort()
 for i in range(0,n):
    if(f[i]%2==0):
        fle.append(f[i])
    else:
        flo.append(f[i])
 fl=fle+flo
 for i in range(n):
    print(fl[i],end=" ")


# In[ ]:


a=int(input())
 b=int(input())  count=0

4- if((ax0) or (b<0)): 45678 6 else: 77 for i in range(a,b+1): 8+ 9

print("Invalid Input")

for j in range(1,i+1):

if(i%j==0):

count count+1

if(count==2):

print(i,end=" ")

count=0


# In[1]:


import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)


# In[2]:


import heapq

H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H,8)
print(H)


# In[3]:


import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)


# In[ ]:


h=[12,3,4,6,5,9,10]
l1=[]
l2=[]
 for i in range len(h):
        if h[i]%2==0:
            l1.append[h[i]]


# In[1]:


#a=[12,3,4,6,5,9,10]
n=int(input("enter the size"))
a=[int(i) for i in input().split()][:n]
l=[]
l1=[]
y=[]
for i in range(len(a)):
    if a[i]%2==0:
        l.append(a[i])
    else:
        l1.append(a[i])
l1.extend(l)
#print(" ".join(map(str,l1)))
print(l1)


# ###### 

# In[2]:


#write a program to combine list to dictionary to form a hash table 
#input:
keys=['name','age','branch']
values=['akshith','20','cse']
outsource=zip(keys,values)
abc=xyz(outsource)
print(abc)


# In[ ]:


#write a program to combine list to dictionary to form a hash table 
#input:
keys=['name','age','branch']
values=['akshith','20','cse']
details=zip(keys,values)
abc=xyz(outsource)
print(abc)


# In[ ]:


#write a  program to store a sparse matrix into a dictionary
#ex:
     [[0,0,0,1,0],
     [2,0,0,0,3],
     [0,0,0,4,0]]


# In[3]:


d={}
write a  program to store a sparse matrix into a dictionary


# In[6]:


# Dictionary to store sparse matrix 
d= {} 
matrix=  [[0,0,0,1,0],
     [2,0,0,0,3],
     [0,0,0,4,0]]
# Finding non zero elements 
for i in range(4): 
    for j in range(4): 
        if matrix[i][j]!= 0: 
            d[(i, j)] = matrix[i][j] 
  
# Print sparse matrix 
print (sparseMatrix)


# In[7]:


matrix =  [[0,0,0,1,0],
     [2,0,0,0,3],
     [0,0,0,4,0]]
  
# Dictionary to store sparse matrix 
sparseMatrix = {} 
  
# Finding non zero elements 
for i in range(4): 
    for j in range(4): 
        if matrix[i][j]!= 0: 
            sparseMatrix[(i, j)] = matrix[i][j] 
  
# Print sparse matrix 
print (sparseMatrix)


# In[12]:


# creating sparse matrix
a = [[0, 0, 0, 1, 0],
       [2, 0, 0, 0, 3],
       [0, 0, 0, 4, 0]]
dic = {}
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] != 0:
            dic[i, j] = a[i][j]
print(dic)


# In[18]:


s=str(input("enter a string"))
a=s[i]
for i in range(len(s)):
    if s.find(s[i])==0:
        print(s[i])
    else:
        print(" no repetition")
     
    


# In[20]:


str=str(input("enter a string"))
for i in str:
    count=0
    for j in str:
        if i==j:
            count+=1
        if count>1:
            break
    if count==1:
        print(" the non-repeated char is ",i)


# In[21]:


#creating a single linked list
class Node:
    def __init__(self,num):
        self.num=num
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def push(self,newnum):
        newnode=Node(newnum)
        newnode.next=self.head
        self.head=newnode
    def insertnext(self,prenode,newnode):
        if prenode is None:
            print(" the previous node")
            return
        newnode=Node(newnum)
        newnode.next=prenode.next
        prenode.next=newnode
    def append(self,newnum):
        newnode=Node(newnum)
        if self.head is Nonne:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
    def printnum(self):
        t=self.head
        while(t):
            print(t.data)
            t=temp.next
if __name__=='__main__'
l1=llist()
l1.append(1)
l1.append(3)
l1.append(5)
l1.append(8)
print(printnum)


# In[4]:


n=int(input("enter the size"))
a=[int(i) for i in input().split()][:n]
a.sort()
print(a)
k=int(input())
print(a[k-1])


# In[8]:


l1=[]
n=int(input("enter the size"))
a=[int(i) for i in input().split()][:n]
for i in range(n-1):
    l1.append(a[i])
l1.extend(a)
print(l1)


# In[15]:


l1=[]
n=int(input("enter the size"))
a=[int(i) for i in input().split()][:n]
b=a.pop()
print(b)
l1.append(b)
l1.extend(a)
print(l1)


# In[ ]:


#heap is a complete binary tree in which every level is filled except the last node
#where as the nodes in the last are filled from left to right
# working of heap sort algorithm 
#-->first step includes the creation of a heap by adjusting the elements in a array
#after the creation of heap now remove the root element of the heap repeatedly by shifting 
#array and then store theheap structure with the remaining elements


# In[1]:


a,b,c=input().split()
#b=int(input(" enter the number"))
#c=int(input(" enter the number"))
if a>b and a>c:
  print("a is the greatest",a)
elif b>a and b>c:
  print("b is the greatest",b)
elif c>a and c>b:
  print("c is greatest",c)


# In[8]:


num=int(input("enter the number"))
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")


# In[11]:


num=int(input("enter the number"))
for i in range(num):
    for j in range(num-i):
        print(j+1,end=" ")
    print("\n")


# In[10]:


num=int(input("enter the number"))
sum=1

if num==0:
    print("factorial is zero")
else:
    for i in range(1,num+1):
        sum=sum*i;
    print("factorial is ",sum)


# In[12]:


num=int(input("enter the number"))
a = 0
b = 1
print(a)
print(b)
for i in range(2, num):
    c = a + b
    print(c)
    a = b
    b = c


# In[21]:


n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
if(c==2):
    print("it is a prime")
else:
    print("it is not prime")


# In[3]:


li=[(10,20,30,40,50),(),(1,2,3,4,5,6)]
li=[i for i in li if len(i)>0]
li


# In[2]:


num=int(input("enter the number"))
li=[]
sum=0
for i in range(num):
    a=int(input("enter elements"))
    li.append(a)
    sum=sum+a
print(sum)
avg=sum/num
print(avg)


# In[8]:


x =['red','green','white','black','pink','yellow']
x.remove('red')
x.remove('pink')
x.remove('yellow')
print(x)


# In[ ]:





# In[13]:


sum=1
tu=(1,2,3)
for i in range(len(tu)):
    sum=sum*tu[i]
print (sum)


# In[13]:


ster=(input("enter the string "))
a=len(ster)
if(a%4==0):
    print(ster[::-1])
else:
    print("not a multiple of 4")


# In[18]:


#a=[12,3,4,6,5,9,10]
n=int(input("enter the size"))
a=[int(i) for i in input().split()][:n]
l=[]
l1=[]
l2=[]
y=[]
for i in range(len(a)):
    if a[i]==0:
        l2.append(a[i]) 
    elif a[i]%2==0:
        l.append(a[i])
    else:
        l1.append(a[i])

print(l)
print(l1)
print(l2)


# ## 

# In[4]:


n=int(input())
arr=[]
for i in range(n):
    username=input("username")
    password=input("password")
    arr.append({username:password})
print(arr)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




