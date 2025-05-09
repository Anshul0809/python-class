# import keyword
# keys=keyword.kwlist
# keys1=keyword.softkwlist
# print(keys)
# print(keys1)
# print(len(keys))
# print(len(keys1))

# import string
# a=string.ascii_letters
# b=string.ascii_lowercase
# c=string.ascii_uppercase
# d=string.punctuation
# print(a,b,c,d)
# print(len(a),len(b),len(c),len(d))

# import string
# abc_xyz01_02=string.ascii_letters
# print(abc_xyz01_02)

# import string
# X=string.ascii_letters
# print(X)

# x=10.5
# y=20
# print(x)
# print(y)
# print(type(x))
# print(type(y))


# x=10.5
# y=20+1j
# print(x)
# print(y)
# print(type(x))
# print(type(y))


# ''' x=input("enter your name:")
#  print (x)
#  print(id(x))
#  print(type(x))'''

# x='''python
# python'''
# print(x)
# x='python "class"'
# print(x)

# l=[10,20,'python','java']
# print(l)
# print(type(l))
# print(id(l))

# t=(10,20,'python',30,'java')
# print(t)
# print(type(t))
# print(id(t))

# d={'name':'anshul','age':18,'qualification':'B.tec'}
# print(d)
# print(type(d))
#print(id(d))

# s={10,20,30,10,10,'python','java'}
# print(s)
# print(type(s))
# print(id(s))

# d={'name':'anshul','age':18,'qualification':'B.tec'}
# fs=frozenset(d)
# print(fs)
# print(type(fs))
# print(id(fs))

# x,y,z,p,q,r=10,20,30,40,50,60
# print(x)
# print(y)
# print(z)
# print(p)
# print(q)
# print(r)

# x=y=z=r=t=10
# print(x,y,z,r,t)

# x,y,z=10,2+3j,[2,4,6,8]
# print(x)
# print(y)
# print(z)

# operators
# x=10.5+2j
# y=50.2+3j
# z1=x+y
# z2=x-y
# z3=x*y
# z4=x/y
# # z5=x//y
# # z6=x%y
# z7=x**y
# print(type(z1))
# print(type(z2))
# print(type(z3))
# print(type(z4))
# # print(type(z5))
# # print(type(z6))
# print(type(z7))
# x=10
# x=x+1
# # x+=1
# print(x)
# x=10
# y=20
# z=0
# # x+=y
# # z+=x
# z=x+y
# print(z)

#comparision operator (<,>,==,<=,>=,!=) (boolean)

'''x=10
y=20
print(x<y)
print(x>y)
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)
print(type(x>=y))'''

#logical operator (and,or,not) (boolean)
'''x=10
y=20
z=30
print(x>y and x>z)
print(z>x and z>y)'''

#membership operator(in,not in)(boolean)
''' x='python'
 print('p' in x)
 print('P' in x)
 print('p' not in x)
 print('P' not in x)
 print('Ptn' in x)
 print('th' in x) '''

#identity operator(is, is not)(compair on the basis of address) (boolean)

'''x=10
y=10
z=20
print(id(x))
print(id(y))
print(id(z))
print(x is y)
print(x is z)'''

#BITWISE operator(&,|,~,<<,>>)
# x=3
# y=7
# print(x & y)
# print(x | y)
# print( ~ y)
# print( ~ x)

# left shift
'''x=10
print(x<<2)
x=10
print(x>>2)'''

#empty data type declaration (generaly typecasting ke liye use hoti hai)
'''x=int()
print(x) 
print(type(x))
x=float()
print(x)
print(type(x))
x=complex()
print(x)
print(type(x))
y=list()
print(y)
z=str()
print(z)
a=tuple()
print(a)
b=dict()
print(b)
c=set()
print(c)
f=frozenset()
print(f)
'''
# second type to declaration
'''x=0
print(x)
print(type(x))
x=0.0
print(x)
print(type(x))
x=''
print(x)
print(type(x))
x=[]
print(x)
print(type(x))
x=()
print(x)
print(type(x))
x={}
print(x)
print(type(x))'''

#typecasting

'''x=input('enter any no..=')
print(x)
# print(type(x)) //by default string'''


'''x=int(input('enter a number'))
print(x)
print(type(x)) '''

#eval inbuilt function (pythhon inbuilt function =print,type,id,input,eval,max,min,sum,len)
# x=eval(input('enter anything:'))
# print(x)
# print(type(x))

''' s="python"
# print(sum(s))
print(max(s))
print(min(s))
print(len(s))

l=[10,20,30,40 ,'python']
print(max(l))
print(min(l))
print(len(l))
print(sum(l))'''

#python inbuilt class(int,str,list,tuple,set,dict,frozenset,float,complex)

'''print('hello')
print('hii')
x=10
y=20
print(x,y) 
####print(sep=' ' ,end='\n')
print("hello",end=',')
print('hii')
print(x,y ,sep=" , ")'''

# bytes ka size janne ke liye
'''
import sys
x=int()
y=str()
z=list()
p=tuple()
q=dict()
r=set()
s=frozenset()
print( "size of integer :",sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getsizeof(z))
print(sys.getsizeof(p))
print(sys.getsizeof(q))
print(sys.getsizeof(r))
print(sys.getsizeof(s))'''

# python object 
# 1.mutable
# 2.immutable
#immutable
'''x=10
y=10
print(id(x),id(y))
x="python"
y="python"
print(id(x),id(y))


x=(10,20,30)
y=(10,20,30)
print(id(x),id(y))
#mutable

x=[10,20,30]
y=[10,20,30]
print(id(x),id(y))'''

# Indexing (orderd collection requeired only ),(findout element position)
# syntex =collection.index('element')
# collection = list,tuple, string
# index(element,start,stop)(stop=excluded)
'''s="python"
print(s.index('o'))
print(s.index('y',2)) #substring not found
print(s.index('h',1,3)) #substring not found
'''
'''l=[10,20,30 ,'python','java']
print(l.index(30))
print(l.index(30,2))
print(l.index(30,3))
print(l.index('java',3,4))'''

# find out first as well as last element
# syntex = collection[indexposition]
'''s="python"
print(s[0]) #first element
print(s[-1]) #last element
print(s[3]) #third(fourth) element
print(s[-3]) #third element from last'''

###Slice

#syntex:-collection[start:stop:step/direction]
#minimum value =s[:]
#rules:1. check step direction if direction not mention that means bydefault its +ve(1)
#2.check start ans stoppoint direction if not given it folloes step direction
#3.if above both directions are same that means we grt o/p but if above both directions are different/opposite that means we always get empty o/p

'''s="i love python"
print(s[: :])
s="i love python"
print(s[: : 2]) '''

'''s="i love python"
print(s[::-1]) #string reverse
print(s[2:10])
print(s[7:-10])
print(s[7:-2]) 
print(s[7:7]) 
print(s[7:-6]) '''

#nesting slice
'''
s="I love python"
print(s[::-1][1:7][::-1][2:3])
'''

'''s='PythonProgramming'
print (s[6:][::-1][:6])'''

###Range
#create collection of similar pattern sequential element
#syntex ; range (start,stop,stepdirection)
#RANGE(stop)
#range(start ,stop)

#example=

'''n=int(input("enter any number"))
x=range(1,n+1)
print(x)
print(list(x))'''

'''x=range(-1,-10)
print(list(x))'''

'''x=range(-1,-11,-1)
print(list(x))

x=range(2,11,2)
print(tuple(x))

x=range(1,10,2)
print(tuple(x))

x=range(-4,5,2)
print(tuple(x))

x=range(-4,0,1)
print(tuple(x))

x=range(-5,-4)
print(tuple(x))

x=range(-5,-6,-1)
print(tuple(x))

x=range(4,-5,-2)
print(tuple(x))

x=range(10,0,-1)
print(tuple(x))'''


'''
#print
print(end="/n")
#print(end=",")
print('hii',end=",")
print(sep='')
print(x,y,sep=",")

'''

'''#######data type
1.numeric
a.integer
b.float
c.complex
2.ordered collection
a.sting
b.list
c.tuple
3.unordered collection
a.set
b.frozenset
4.mapped
a.dictionary
5.boolean
##fundamentaldata type'''

'''x=10
print(x)
print(type(x))

x=10.5
print(x)
print(type(x))

x=("anshul")
print(x)
print(type(x))

x=10+2j
print(x)
print(type(x))'''

#python inbuilt function for numeric
'''1.max()
2.min()
3.len()
4.type()
5.id()
6.print()
'''
'''x=10 #(it is not iterable)
print(len(x)) '''

#int
'''x=10
print(x)
print(type(x))
print(id(x))  #it is applicable'''

#oderded collection(string,list,tuple)
#string
'''.collection of charecter
.repersent by '' ,"", ''''''
.oderded collection
.indexing support
.slicing support
.immutable'''

'''x="anshul" #it is iterable
#pythoninbuilt function
print(max(x))
print(min(x))
print(len(x))
print(id(x))
print(type(x))
print(x)'''

#string inbuilt methods
'''1.lower()
2.upper()
3.swapcase()
4.titel()
5.capitalize()
6.center()
7.join()
8.split()'''

'''s="This is python class"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.title())
print(s.capitalize())
print(s.center(100,'!'))'''
#join()
#syntex='seperator'.join(iterator)
'''
s1="anshul"
s2="gajbhiye"
# print(''.join(s1,s2)) //error
print(' '.join(s1))
print(' '.join((s1,s2)))
print(' '.join([s1,s2]))
'''
#split()
#syntex= variable.split(__,__)#(where,howmanytimes)
s="this is python"
print(s.split()) #bydefault split by space (space ko hatake ,)
print(s.split('s')) #split by s(s ko hatake ,)
print(s.split('s',0)) #split by s,0
print(s.split('s',1)) #split by s,1

