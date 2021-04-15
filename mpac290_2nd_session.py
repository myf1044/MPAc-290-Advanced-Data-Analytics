# -*- coding: utf-8 -*-
"""MPAc290 2nd session.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XiSdcK4Az92vsc0e0Q4sQ9puqKzdDRKM
"""



"""In this session we will be talking about conditions, loops and some libraries that will be useful for the rest of the course.

## Condition Statements

Comparison operations compare some value or operand and, based on a condition, they produce a Boolean. When comparing two values you can use these operators:

<ul>
    <li>equal: <b>==</b></li>
    <li>not equal: <b>!=</b></li>
    <li>greater than: <b>></b></li>
    <li>less than: <b>&lt;</b></li>
    <li>greater than or equal to: <b>>=</b></li>
    <li>less than or equal to: <b>&lt;=</b></li>
</ul>
"""

# Condition Equal

a = 5
a == 6

# Greater than Sign

i = 6
i > 5

# Greater than Sign

i = 2
i > 5

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/CondsGreater.gif" width="650" />"""

# Inequality Sign

i = 2
i != 6

# Use Equality sign to compare the strings

"ACDC" == "Michael Jackson"

# Use Inequality sign to compare the strings

"ACDC" != "Michael Jackson"

"""in the following cell Python compare ASCII code for those two letters"""

'B' > 'A'

# Compare characters

'BA' > 'AB'

"""Branching: 

<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/CondsIf.gif" width="650" />
"""

# If statement example
age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# If statement example
age = 19
age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")

# Else statement example

age = 18
age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/CondsElse.gif" width="650" />"""

# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

"""<img src ="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/CondsElif.gif" width="650" />

As before, we can add an <code>else</code> block to the <code>if</code> block. The code in the <code>else</code> block will only be executed if the result is <b>False</b>.


<b>Syntax:</b> 

if (condition):
    # do something
else:
    # do something else

Logical Operations

Sometimes you want to check more than one condition at once. For example, you might want to check if one condition and another condition is **True**. Logical operators allow you to combine or modify conditions.
<ul>
    <li><code>and</code></li>
    <li><code>or</code></li>
    <li><code>not</code></li>
</ul>

These operators are summarized for two variables using the following truth tables:

A: 2 > 4 --> Bool(A) = False

B: 17 > 10 --> Bool(B) = True

<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/CondsTable.png" width="650" />
"""

# Condition statement example

album_year = 1980

if (album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

# Condition statement example

album_year = 1990

if (album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

# Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")

"""### Loops

Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by <b>loops</b>. We will look at two types of loops, <code>for</code> loops and <code>while</code> loops.
"""

range(3)

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsRange.png" width="300" />"""

list(range(3))

list(range(1,12))

list(range(1,12,2))

"""The <code>for</code> loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.    
Let's try to use a <code>for</code> loop to print all the years presented in the list <code>dates</code>:
"""

list(range(3))

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    #print(i)
    print(dates[i])
    #print(80*'=')

list(range(1,3))

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsForRange.gif" width="800" />

In Python we can directly access the elements in the list as follows:
"""

# Exmaple of for loop, loop through list
dates = [1982,1980,1973]
for year in dates:  
    print(year)

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsForList.gif" width="800">"""

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])

squares

"""What is while loop?"""

# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while (year != 1973):
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i ,"repetitions to get out of loop.")

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsWhile.gif" width="650" />"""

A = "Class"
A.lower()

"""Library"""

# Commented out IPython magic to ensure Python compatibility.
# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
# %matplotlib inline

# Plotting functions

def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

# Create a python list

a = ["0", 1, "two", "3", 4]

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumOneList.png" width="660" />"""

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a

type(a)

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumOneNp.png" width="500" />"""

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

a.dtype

# Create a numpy array

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

type(b)

b.dtype

# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c

c[0] = 100

# Assign the 5th element to 0

c[4] = 0
c

# Slicing the numpy array

d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c

# Create the index list

select = [0, 2, 3]

c

# Use List to select elements

d = c[select]
d

# Assign the specified elements to new value

c[select] = 100000
c

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array

a.size

# Get the number of dimensions of numpy array

a.ndim

# Get the shape/size of numpy array

a.shape

# Get the mean of numpy array

mean = a.mean()
mean

# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation

# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b

# Get the biggest value in the numpy array

max_b = b.max()
max_b

min_b = b.min()
min_b

u = np.array([1, 0])
u

v = np.array([0, 1])
v

# Numpy Array Addition

z = u + v
z

# The value of pie

np.pi

"""Linespace"""

# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)

# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a

# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
A

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumTwoEg.png" width="500" />

<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumTwoFT.png" width="400" />
"""

A.ndim

# Show the numpy array shape

A.shape

# Show the numpy array size

A.size

b = [1,2,3,4]
b[0]

# Access the element on the second row and third column

A[1, 2]

# Access the element on the second row and third column

A[1][2]

# Access the element on the first row and first column

A[0][0]

# Access the element on the first row and first and second columns

A[0][0:2]

# Access the element on the first and second rows and third column

A[1:3, 2]

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumTwoTST.png" width="400" />

<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumTwoAdd.png" width="500" />
"""

# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y

# Add X and Y

Z = X + Y
Z

"""<img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumTwoDb.png" width="500" />"""

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y

# Multiply Y with 2

Z = 2 * Y
Z

# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])
C

# Get the transposed of C

C.T

"""# Pandas"""

import pandas as pd

import numpy as np

test_list = [100,200,300]
pd.Series(data=test_list)

"""Let's bring a dataset and see how we can use Pandas to learn more about it.
Here, we are going to use the Iris dataset from UCI Archive. https://archive.ics.uci.edu/ml/datasets/Iris
"""

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

df = pd.read_csv(url)

df.head()

iris = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
iris.head()

"""Analytics:
* descriptive analytics
* predictive analytics
* prescriptive analytics
"""

iris.info()

iris.describe()

iris.nunique()

iris['sepal_length']

list_a = list(iris['sepal_length'])

iris[['sepal_length', 'petal_length']]

"""**Conditional Selection**

We can also ***filter*** through the data. 
"""

iris[iris['petal_length'] > 1.6]

iris[iris['species'] == 'Iris-setosa']

"""**Aggregation Functions**

Now that we know how to navigate through data, it is time to do some aggregation upon it. To start off, we can use the describe function to find out the distribution, max, minimum and useful statistics of our dataset.
"""

iris.describe()

iris.max()

iris['petal_width'].max()

iris.std()

iris['petal_width'].median()

iris.corr()

"""Explartory Data Analysis - EDA"""

import pandas as pd
url = 'https://raw.githubusercontent.com/ArashVafa/DESC624/master/bank_marketing_training'
bank_train = pd.read_csv(url)
bank_train.head(10)

bank_train['days_since_previous'].value_counts()

bank_train.shape

iris.shape

bank_train['index'] = pd.Series(range(0,26874))

bank_train.head(n = 5)

type(bank_train)

type(iris)

bank_train['days_since_previous'].plot(kind = 'hist')

bank_train.describe()

bank_train['days_since_previous'] = bank_train['days_since_previous'].replace({999: np.NaN})

bank_train['days_since_previous'].plot(kind = 'hist')

bank_train.head()

bank_train