# Specific requirements
This repo intends to build on basic Python and Pandas knowledge and cater that to working at Jisc.

## UKPRN format
By default most sources will format the UKPRN column as a floating point number when imported into a data frame.
The following code converts the UKPRN column of a dataframe into a string, in doing so, that leaves a decimal e.g. "10007773.0".
The split separates the integer and decimal part of the converted UKPRN string, then takes the first part of that [0] ([1] would return the decimal due to Python 0 indexing)
``` python 
df["UKPRN"] = df["UKPRN"].astype(str).str.split(".", expand = True)[0]
```
## File paths
Python supports 'relative file paths'
```
Short explanation of relative file paths

Example in use
```
It is recommended to set up file structures to support that. However realistically it's not always possible and file paths are necessary.
Teams/SharePoint/OneDrive embeds the current user's name in filepaths.
To dynamically insert the username in a path, use the inbuilt getpass library, specifically getuser. 
``` python
import os
from getpass import getuser

os.chdir(r"C:/Users/" + getuser() + "/Jisc/22056 Quality Task Group - General/DF QA Data Engineering/Code")
```
**_Note that os.getlogin() is also available, however it is recommended that getpass is used to avoid the reliance on a controlling terminal if deployed in Linux._**

# Common requirements
## Dataframe columns
``` python
df.columns
```
## Dtypes

## Info

## Table dimensions

## Group by

## Pivot
```
...or pivot_table... that is the question.
```
## String manipulation

## List comprehension in practice

## Table comparison
```
Brandon's self-built package?

Maybe a basic example to demo without the package
```

## Import Excel
``` python
pd.read_excel(, xlrd [plus others])
```
## Standardisation of quote/apostrophe
It is strongly recommended to use quote marks " as standard over apostrophes ' 
For example - embedding SQL code in Python scripts:
``` python
sql = "SELECT TOP 100 * FROM [Student].[V056_StudentEngagement] WHERE Z_PERMADDGRP4 = '04'"
```
Or, a more preferred version of the above using multi-line text and f-strings:
``` python
sql = f"""
SELECT TOP 100
  *
FROM [Student].[V056_StudentEngagement]
WHERE
  {field} = '{field_value}'
"""
```

## IDE advice and recommendations

## Using command line
