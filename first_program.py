# This is a sample Python script.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print("hello world")
#this is a comment
#python identation excercise
if 5>2:
    print("five is greater than two")
    if 5>2:
        print("five is greater")
        print("five is greater than two")



#Python variable
x=5
y="hello world"
print(x)
print(y)

#indentation
if 5>2:
    print("yes")
#assigning a variable
carname="volvo"
print (carname)

x=5
y=10
print(x+y)

#getting the char from index 2:4
txt="hello world"
x=txt[2:4]

#type of variables
x=5
y="jhon"
print(type(x))
print(type(y))

#Many values of multiple variables
x,y,z="orange","banana","cherry"
print(x)
print(y)
print(z)

#unpacking a List
x,y,z=["apples","banana","oragne"]
print(x)
print(y)
print(z)
"""global variables
declear variable outside and call in function"""
x="awesome"
def myfunc():
    print("my python is "+x)
myfunc()

"""creating variable inside function 
as global variable"""
x="awesome"
def myfunc():
    x="fantastic"
    print("python is "+x)
myfunc()
print("python is very "+x)
#global keyword
def myfunc():
    global x
    x="good"
myfunc()
print("python is "+x)
#print randon range
import random
print(random.randrange(1,10))
#multiline string
a="""this is 
a miltiline string"""
print(a)
a="hello world"
print(a[2])
#Looping through array
for x in "banana":
    print(x)
#string Length
a="hello world"
print(len(a))
#check string
a="the best in life is free"
print("free" in a)
if "free" in a:
    print("yes free is present")

#slicing
a="hello world"
print(a[-5:-2])
#upper and lowe case methods
a="hello world"
print(a.upper())
b="i am zahra"
print(b.lower())
#replacing a string
a="Hello world!"
print(a.replace("H","j"))
#split string
a="Hello, World"
print(a.split(","))
#string concat
a="hello"
b="world"
c=a+b
print(c)
#string formatting
age=36
txt="my name is jhon and i am {}"
print(txt.format(age))
#format argument
quantity=3
itemno=555
price=50
my_order="i want {} pieces of item{} for {} dollers"
print(my_order.format(quantity,itemno,price))
#boolean operator
print (9<10)

def func():
    return True
if func():
    print("yes")
else:
    print("no")
#List and sets (Arrays in python)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#comprehensiom
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
thislist=["orange","apple","banana"]
thislist.sort()
print(thislist)
#sorting a list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#joining the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#insert
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,
 "lemon")
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#pythoTuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#Loop in tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  #Python Dictionries
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print(thisdict)
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print(thisdict["brand"])
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print(type(thisdict))
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  x = thisdict["model"]
  car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }

  x = car.keys()

  print(x)  # before the change

  car["color"] = "white"

  print(x)  # after the change
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  if "model" in thisdict:
      print("Yes, 'model' is one of the keys in the thisdict dictionary")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  a = 200
  b = 33
  if b > a:
      print("b is greater than a")
  else:
      print("b is not greater than a")
#Loop
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
a = 2
b = 330
print("A") if a > b else print("B")
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement
if a==b and c==d:
    print("hello")
#for Loop in python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
fruits=["apple", "banana","cherry"]
for x in fruits:
    if x=="banana":
        break
    print (x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
for x in range(6):
  print(x)
for x in range(2, 30, 3):
  print(x)

#for loop
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":

        break

print(x)


#Interation in python
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#Functions
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#my iterative



cd


# This is a sample Python script.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print("hello world")
#this is a comment
#python identation excercise
if 5>2:
    print("five is greater than two")
    if 5>2:
        print("five is greater")
        print("five is greater than two")



#Python variable
x=5
y="hello world"
print(x)
print(y)

#indentation
if 5>2:
    print("yes")
#assigning a variable
carname="volvo"
print (carname)

x=5
y=10
print(x+y)

#getting the char from index 2:4
txt="hello world"
x=txt[2:4]

#type of variables
x=5
y="jhon"
print(type(x))
print(type(y))

#Many values of multiple variables
x,y,z="orange","banana","cherry"
print(x)
print(y)
print(z)

#unpacking a List
x,y,z=["apples","banana","oragne"]
print(x)
print(y)
print(z)
"""global variables
declear variable outside and call in function"""
x="awesome"
def myfunc():
    print("my python is "+x)
myfunc()

"""creating variable inside function 
as global variable"""
x="awesome"
def myfunc():
    x="fantastic"
    print("python is "+x)
myfunc()
print("python is very "+x)
#global keyword
def myfunc():
    global x
    x="good"
myfunc()
print("python is "+x)
#print randon range
import random
print(random.randrange(1,10))
#multiline string
a="""this is 
a miltiline string"""
print(a)
a="hello world"
print(a[2])
#Looping through array
for x in "banana":
    print(x)
#string Length
a="hello world"
print(len(a))
#check string
a="the best in life is free"
print("free" in a)
if "free" in a:
    print("yes free is present")

#slicing
a="hello world"
print(a[-5:-2])
#upper and lowe case methods
a="hello world"
print(a.upper())
b="i am zahra"
print(b.lower())
#replacing a string
a="Hello world!"
print(a.replace("H","j"))
#split string
a="Hello, World"
print(a.split(","))
#string concat
a="hello"
b="world"
c=a+b
print(c)
#string formatting
age=36
txt="my name is jhon and i am {}"
print(txt.format(age))
#format argument
quantity=3
itemno=555
price=50
my_order="i want {} pieces of item{} for {} dollers"
print(my_order.format(quantity,itemno,price))
#boolean operator
print (9<10)

def func():
    return True
if func():
    print("yes")
else:
    print("no")
#List and sets (Arrays in python)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#comprehensiom
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
thislist=["orange","apple","banana"]
thislist.sort()
print(thislist)
#sorting a list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#joining the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#insert
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,
 "lemon")
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#pythoTuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#Loop in tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  #Python Dictionries
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print(thisdict)
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print(thisdict["brand"])
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print(type(thisdict))
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  x = thisdict["model"]
  car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }

  x = car.keys()

  print(x)  # before the change

  car["color"] = "white"

  print(x)  # after the change
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  if "model" in thisdict:
      print("Yes, 'model' is one of the keys in the thisdict dictionary")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  a = 200
  b = 33
  if b > a:
      print("b is greater than a")
  else:
      print("b is not greater than a")

      print("b is not greater than a")


