# Python Notes for Reference

In order to convert a dataframe column without the index
Use below code :

~~~python
    dict = df_test.to_dict('dict') or  ('list')
~~~

Keep in mind that 'list' generates a list and 'dict' generates a dict object

Note that for this to work, the object has to be in Dataframe format and
not in list or array format.

Use

~~~python
[[]]
~~~

to extract data from column

* Note : We can create a Nested or hierarchical dictionary structure by including multiple columns together

_____________________________________________________________________________________=

## When creating a Multilevel index, sort the index, or it will give error

~~~python
    df.set_index(["col1","col2"],inplace=True)
    df.sort_index(inplace=True)
    df.loc["col1","col2"]
~~~

_____________________________________________________________________________________=

## The opposite of isin

~~~python
    1. df[-df["column"].isin(["value"])]
    2. df[~df["column"].isin(["value"])]
    3. df[df["column"].isin(["value"]) == False]
    4. df[np.logical_not(df["column"].isin(["value"]))]
~~~

_____________________________________________________________________________________=

## Iterating over the rows of a DataFrame

~~~python
    for index,rows in df.iterrows():
        print(rows)
~~~

## We can also print a specific column with

~~~python
    for index,rows in df.iterrows():
        print(rows["col1"])
~~~

_____________________________________________________________________________________=

## Filter one Dataframe based on another one

### The second dataframe may have lesser columns

~~~python
    import pandas as pd
    df = pd.dataFrame
    df.loc[dataframe_second.index]
~~~

This will filter one dataframe based on another. Another Dataframe may just contain condition from an output.

<https://www.geeksforgeeks.org/how-to-select-the-rows-of-a-dataframe-using-the-indices-of-another-dataframe/>

_____________________________________________________________________________________=

## To filter Data from a Dataframe on a specific pattern

~~~python
    df[df"Col1"].str.contains("string")]
~~~

## To negate that condition

~~~python
    df[~df"Col1"].str.contains("string")]
~~~

_____________________________________________________________________________________=

## The Below line would show whole numbers in Python's Pandas dataframes instead of Scientific Notation

~~~python
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
~~~

_____________________________________________________________________________________=

## To convert a column from one datatype to another, we use the below command

~~~python
    df[col].astype(int)
~~~

This will convert string datatype to int.

In order to convert multiple column types from string to int, we can do the following

~~~python
    for cols in df.columns:
        try:
            df[cols].astype(int)
        except:
            print("Exception Raised")
        else:
            print("Converting")
            df[col] = df[col].astypt(int)
~~~

_____________________________________________________________________________________=

This is Anything Between Parentheses

~~~python
    h_name = re.compile(r'\'.*?\'')  
~~~

_____________________________________________________________________________________=

## Read a CSV File in Python

~~~python
    loc = "file_location"
    opened_file = open(loc, encoding='utf8')
    from csv import reader
    read_file = reader(opened_file)
    db_creds = list(read_file)
    opened_file.close()
~~~

This will read a file and compile its contents into a list

_____________________________________________________________________________________=

## Stack numpy arrays

~~~python
    arr = np.vstack((arr1,arr2)) # This will stack the arrays vertically, one after the other
    arr = np.hstack((arr1,arr2)) # This will stack the arrays horizontally, 1st row of array 1, followed by first row of array 2 and so on.
    # The Arrays should be of the same size

    # Similarly, we have vplit and hsplit

    np.vsplit(array,2) # 2 will result in 2 arrays split vertically and so on.

~~~

_____________________________________________________________________________________=

## Passing Named argument from a dictionary to a function

~~~python
    # If we have a function with named arguments, then we can pass a dictionary as the arguments.
    def add(x,y):
        return x+y

    nums = {"x":10,"y":15}
    print(add(**nums))
~~~

_____________________________________________________________________________________=

## Iterating an array from a specific point

~~~python
    # If we want to iterate in Python from a specific value, like starting from second value etc. 
    import numpy as np
    arr = np.random.rand(10)*10

    for row in arr[1:]:   # This will start the countdown from the 2nd value in the array
        print(row)
~~~

_____________________________________________________________________________________=

## Mutable Parameters

Never make a paramter equal to a mutable value by default.

~~~python

    from typing import List

    class Student:
        def __init__(self,name:str, grades:List[int]=[]): ## This is bad
            self.name = name
            self.grades = grades

        def take_exam(self,result:int):
            self.grades.append(result)
    
    bob = Student("Bob")
    rolf = Student("Rolf")

    bob.take_exam(90)

    print(bob)
    print(rolf)


    # Output 

    [90]
    [90]

    # Explanation
    # Output for both is 90 even though we didn't define marks for Rolf. This is because List is immutable.  

    # To fix this, we need to pass the grade with the name. 

    bob = Student("Bob",[90,80]).

    # In general, do not use immutable parameters 

~~~

_____________________________________________________________________________________=
