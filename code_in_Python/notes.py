# ============================================================

# In order to convert a dataframe column without the index
# Use below code :
dict = df_test.to_dict('dict') or  ('list')

# Keep in mind that 'list' generates a list and 'dict' generates a dict object

# Note that for this to work, the object has to be in Dataframe format and 
# not in list or array format.
# Use [[]] to extract data from column

#* Note : We can create a Nested or hierarchical dictionary structure by 
# including multiple columns together. 


# ============================================================

# When creating a Multilevel index, sort the index, or it will give error. 
df.set_index(["col1","col2"],inplace=True)
df.sort_index(inplace=True)
df.loc["col1","col2"]

#=============================================================

# The opposite of isin

1. df[-df["column"].isin(["value"])]
2. df[~df["column"].isin(["value"])]
3. df[df["column"].isin(["value"]) == False]
4. df[np.logical_not(df["column"].isin(["value"]))]

#=============================================================

#Iterating over the rows of a DataFrame 

for index,rows in df.iterrows():
    print(rows)

# We can also print a specific column with 

for index,rows in df.iterrows():
    print(rows["col1"])


#==============================================================
# Filter one Dataframe based on another one. 
# The second dataframe may have lesser columns 

dataframe.loc[dataframe_second.index]

# This will filter one dataframe based on another. 
# Another Dataframe may just contain condition from an output.

# https://www.geeksforgeeks.org/how-to-select-the-rows-of-a-dataframe-using-the-indices-of-another-dataframe/

#==============================================================
## To filter Data from a Dataframe on a specific pattern

df[df"Col1"].str.contains("string")]

## To negate that condition 
df[~df"Col1"].str.contains("string")] 


#===============================================================

## The Below line would show whole numbers in Python's Pandas dataframes instead of Scientific Notation
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#===============================================================

# Below BLock of Code Helps Finad anything between a set of Parentheses 
match = re.compile(r'\'.*?\'') 

# This will find anything between '' <-- Single Quotes. 
match.findall(string)

# Then we can get the value between the Parentheses using the .split() method and extracting the suitable candidiate 

#===============================================================

# Getting the Hostname of a System
os.uname()

# This Returns a Class Object. To convert it to a string, we need to wrap it in str()
