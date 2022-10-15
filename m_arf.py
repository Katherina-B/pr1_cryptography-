import math
import numpy as np
import random


def step(b):
    temp1 = bin(b)
    temp2 = temp1[2:]
    n = 0
    for i in range(len(temp2)):
        if temp2[i]=='1':
            n=n+1
    x = np.arange(0, n, 1)
    j=0
    m = len(temp2)
    for i in range(m):
        if temp2[i]=='1':
            x[j]=m-i-1
            j=j+1
    return x


def mod1(a,m):
    if a> 0 :
        x = a%m
    if a<0:

        x = ( math.trunc(abs(a)/m)+1)*m+a
    return x

def mod2(a,b,m):
    b1 = step(b)
    n = len(b1)
    b_2= np.arange(0, n, 1)
    for i in range(n):
        b_2[i] = 2**b1[i]
    c = np.arange(0, b_2[0], 1)
    i=1
    c[0] =  mod1(a,m)
    for i in range(b_2[0]-1):
        if c[i]==1:
            c[i+1]=1
        else:
            A = a**(i+1)
            c[i+1] = mod1(A,m)
    x = 1
    for i in range(b_2[0]-1):
        if math.trunc(math.log2(i+1))!=math.log2(i+1):
            c[i]=1
    for i in range(len(b1)):
        x=x*c[b1[i]]
    return x

def mod3(a,b,m):
    flag = False
    i=1
    x=np.arange(0, 2, 1)
    while flag == False:
        if mod1(a*i,m)==mod1(b,m):
            x[0]=i
            flag = True
        else:
            i=i+1
    i=-1
    flag = False
    while flag == False:
        if mod1(a * i, m) == mod1(b, m):
            x[1] = i
            flag = True
        else:
            i = i - 1
    return x

def mod3_1(a,b,m):
    b = mod1(b,m)
    x = np.arange(0, 2, 1)
    flag = False
    temp=b
    while flag ==False:
        temp=temp+m
        if temp%a==0:
            x[0]=math.trunc(temp/a)
            flag = True
    flag = False
    temp = b
    while flag == False:
        temp = temp - m
        if temp % a == 0:
            x[1] = math.trunc(temp / a)
            flag = True
    return x

def resh(A,B):
    n = B
    x = np.arange(2, n, 1)
    m = 0
    for i in range(n-2):
        if x[i]==1:
            i=i+1
        else:
            for j in range(i+1, n-2):
                if x[j]%x[i]==0:
                    x[j]=1
                    m = m + 1
    y1 = np.arange(0, m, 1)
    y = np.arange(0, m, 1)
    j=0
    for i in range(n-2):
        if x[i]!=1:
            y[j] = x[i]
            j=j+1
    count_null=0
    for i in range(m):
        if y[i]<A:
            y1[i] = 0
            count_null=count_null+1
    num =random.randint(count_null, m)
    return y[num]


print("Завдання1")
m = int(input("m="))

#a1 = -257
print("Завдання2")
a = int(input("a="))
print(mod1(a,m))
#print(mod1(a1,m))

print("Завдання3")
a = int(input("a="))
b = int(input("b="))
m = int(input("m="))
#print(mod2(707, 321, 17))
print(mod2(a, b, m))
print("Завдання4")
a = int(input("a="))
b = int(input("b="))
m = int(input("m="))
print(mod3(a,b,m))
print(mod3_1(a,b,m))
print("Завдання5")
a = int(input("A="))
b = int(input("B="))
print(resh(a,b))