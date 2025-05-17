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
##fundamentaldata type 
1.integer
2.string
3.list
4.tuple
5.dict.. 
'''

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
'''s="this is python"
print(s.split()) #bydefault split by space (space ko hatake ,)
print(s.split('s')) #split by s(s ko hatake ,)
print(s.split('s',0)) #split by s,0
print(s.split('s',1)) #split by s,1
'''
s="python123"
'''
print(s.isascii())
print(s.isdigit())
print(s.isspace())
print(s.isnumeric())
print(s.isdecimal())
'''#return boolean

##list
# defi.collection of homogeneous as well as heterogeneous element
# represented through [] with , sapereted element

'''
l1=["python","java","php"]
l2=[1,2,3,4,5]
print(max(l1))
print(max(l2)) 
print(min(l1))
print(min(l2))
# print(sum(l1)) //error 
print(sum(l2))
print(len(l1))
print(len(l2))
print(type(l1))
print(type(l2))
print(id(l1))
print(id(l2))
print(l1)
print(l2)
'''
#list method (copy(),clear(),append(),extend(),insert(),pop(),remove(),index(),count(),reverse(),sort())
'''
l=[10,20,30,40,10,10,"python"]

l.append("java")
print(l)
l.append([2,4,5,6,8,10])
print(l)
l.extend(["php","java"])
print(l)
l.extend("python")
print(l)
l.extend("21")
print(l)
l.extend("p")
print(l)
l.insert(0,"java")
print(l)
l.insert(0,[1,2,3,4,5])
print(l)

l.pop()
print(l)
l.remove(30)
print(l)

l=[10,20,30,"python"]
print(l.index(20))

'''
'''
#count():-(frequncy calculate karna )
l=[10,20,30,10,50,60,10]
print(l.count(10))
print(l.count(20))
print(l.count(100)) 

l=[10,30,5,20]
l.sort()
print(l)

l=[2,4,6,1,3,5]
l.reverse()
print(l)

#arrange decending order

# l.sort (assending order)
# l.reverse(desending order)

l=[10,20,50,30,2,4]
# l.sort()
# l.reverse()
l.sort(reverse=True) #desending order
print(l)

#copy
l=[10,20,30,50]
l1=l.copy()
print(l)
print(l1)
print(id(l),id(l1)) 

#clear
l=[10,20,30,"python"]
l.clear()
x=l
print(l)
print(id(x))
# l.clear()
# print(l)
# print(id())
del l #del use to delet object in memory
print(l)

'''
### Tuple = collection of odered homogeneuse as well as hetrogeneuse element
# repersented through () with comma sapareted object
# indexing supported
# sclicing supported
# immutable in nature 
# example
'''
t=(2,4,3,6,1,5)
print(t)
print(id(t))
'''
# python inbuilt function for tuple' 
# len()
# max()  (only homogeneus)
# min()  (only homogeneus)
# sum()  (only homogeneus numeric)
# type()
# id()

'''
t=(2,4,6,"python")
print(len(t))
# print(max(t)) #only homogeneus //error
# print(min(t)) #only homogeneus 
# print(sum(t)) #only homogeneus numeric //error
print(type(t))
print(id(t))

t=("python","java")
print(max(t)) #only homogeneus //python
print(min(t)) #only homogeneus //java

t=(10,10.5,20)
print(sum(t)) #only homogeneus numeric //40.5
'''
'''
#inbuilt methods of tuple (index,count)
t=(10,20,30,"python",40)
print(t.index("python")) 
# print(t.index("python",4)) #// error
print(t.count(10))
'''
#dictionary
#def.collection of key value pair
#key should be unique
# Value may be duplicate
#represented through {} with comma saoereted key value pair
# indexing not support
# sclicing not supported
# mutable in nature
# 
#python inbuilt function for dictionary
#len()
#max()
#min()
#sum()
#type()
#id()
'''
d={'name':'Anshul','age':20,'quali':'b.tech'}
print(len(d))
print(max(d))
print(min(d))

d={'name':'Anshul',1:20,'quali':'b.tech'}
# print(max(d)) #error (not supported between instances of 'int' and 'str')
# print(min(d)) #error (not supported between instances of 'int' and 'str')
print(len(d))

d={2:'Anshul',1:20,3:'b.tech'}
print(max(d)) 
print(min(d))
print(sum(d)) 
print(len(d))
print(type(d))
print(id(d))

d={2:'Anshul',2:20,'3':'b.tech'}
print(d)
'''
#dictionary methods
# 2.update()
# 3.clear()
# 4.copy()
# 5.get('key')
# 6.items()
# 7.keys()
# 8.pop('key')
# 9.popitem() #remove last item
# 10.setdefault()
# 11.values()
# 12.fromkeys()

'''
d={'name':'Anshul','age':20,'quali':'b.tech'}
print(d.keys())
print(d.values())
print(d.items())
print(d.get('name'))
print(d.get('age'))
# d.pop('age')
# print(d)
# d.popitem()
# print(d)

#use of fromkeys()
l=[1,2,3,'z','a','s','f']
d=dict.fromkeys(l,10)
print(d)

d={'name':'Anshul','age':20,'quali':'b.tech'}
# d.setdefault('name1','rahul')
# d.setdefault('name','rahul')
# print(d.setdefault('name','rahul'))
# print(d)
# x=d.copy()
# print(x)
# d.clear()
# print(d)

d1={'name':'ans','age':25}
d.update(d1)
print(d)
'''

###set()
# unordered collection of unique element 
# representing through {} with comma sapereted object
# indexing not supported
# sclicing not supported
# mutable in nature
#ex:=
'''
st={2,4,6,8,2,"python","java","php"} 
print(st)
print(id(st))
print(type(st))

#python methods for set
# 1.len()
# 2.max() //error
# 3.min() //error
# 4.sum()  //error
 
print(len(st))
print(max(st)) #error
print(min(st)) #error
print(sum(st)) #error

'''
#inbuilt methods

# s. 
# 1.add() //add element in set
# 2.remove() //remove element from set
# 3.pop() //remove random element from set
# 4.clear() //clear all element from set
# 5.discard() //remove element from set if present
# 6.union() //return union of two set
# 7.intersection() //return intersection of two set
# 8.difference() //return difference of two set
# 9.copy() //return copy of set
# 10.update() //update set with elements from another set
# 11.issubset() //check if set is subset of another set
# 12.issuperset() //check if set is superset of another set
# 13.issubset() //check if set is subset of another set
# 14.issuperset() //check if set is superset of another set
# 15.isdisjoint() //check if set is disjoint with another set
# 16.frozenset() //return frozenset object
# 17.remove() //remove element from set if present
# 18.discard() //remove element from set if present
#19.symmetric_difference()
#20.symmetric_difference_update()
'''
s={2,4,6,8,'python','java'}
##single set applicable methods

# s.add('php') #add element in set on element
# print(s)
# s.update(1,3) #add multiple element in set
# print(s)  #error (int' object is not iterable)
# s.update('python')
# print(s)
# s.update((1,3,5,10))
# print(s)
# s.update((1,3,'anshul'),"python")
# print(s)
# s.pop()  #ramdom oneelement delete
# print(s) 
# s.remove('java') #delete perticular element from set
# print(s)
# # s.remove('Java')
# # print(s) error
# s.discard('Java')
# print(s) #error se bachne ke liye use kare discard element nhi hai to same exicute ho jayega
# s.clear()
# print(s) #clear all element from set
# S1=s.copy()
# print(S1) #copy of set
# print(id(s),id(S1))

##double set applicable methods
#union
s1={1,2,3,4,5}
s2={4,5,6,7,8}
# print(s1.union(s2)) #return union of two set
#intersection
# print(s1.intersection(s2)) #return intersection of two set common element
#difference
# print(s1.difference(s2)) #return difference of two set (s1-s2=and only s1 element returns)
#symmetric_difference
# print(s1.symmetric_difference(s2)) #return symmetric difference of two set (intersection ka just opposite)

#intersection_update
#difference_update
#symmetric_difference_update

# s1.intersection_update(s2) #intersection update
# print(s1) #s1 me intersection of s2 element add ho jayega
# print(s2) #no change

# s1.difference_update(s2) #difference update
# print(s1) #s1 me difference of s2 element delete ho jayega
# print(s2) #no change

# s1.symmetric_difference_update(s2)
# print(s1) #s1 me symmetric difference of s2 element add ho jayega
# print(s2) #no change

#isdisjoint()
print(s1.isdisjoint(s2))

#issuperset
print(s1.issuperset(s2)) 
print(s2.issuperset(s1))

#issubset
print(s1.issubset(s2)) 

'''
#frozenset (union,intersection,difference,symmetric difference are applicable)
fs1={10,20,10,30,20,40}
fs2={2,4,6,8}
fs1=frozenset(fs1)
fs2=frozenset(fs2)
print(fs1)
# print(fs1.union(fs2)) #union merged two set
# print(fs1.intersection(fs2)) #intersection common element return
# print(fs1.difference(fs2)) #difference s1-s2 return
# print(fs1.symmetric_difference(fs2)) #symmetric difference s1-s2 and s2-s
# print(fs1.isdisjoint(fs2))
# print(fs1.issubset(fs2))
# print(fs1.issuperset(fs2))

#empty declaration of datatypes will be
#int()
#float()
#complex()
#str()
#list()
#tuple()
#dict()
#set()
#frozenset()


