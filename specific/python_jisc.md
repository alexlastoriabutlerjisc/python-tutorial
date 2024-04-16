# Specific requirements
## UKPRN format
``` python 
df['UKPRN'] = df['UKPRN'].astype(str).str.split('.', expand = True)[0]
```
## File paths
Python supports 'relative file paths'

```
Short explanation of relative file paths

Example in use
```

# Common requirements
## Dataframe columns
```
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
```
pd.read_excel(, xlrd [plus others])
```

```
IDE advice and recommendations

Using command line
```
