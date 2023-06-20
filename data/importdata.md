# Basic data scrape and comparison
The code below will read a CSV from the student open data as a Pandas dataframe

nb: storage_options is an optional variable to include, the code will likely run without it but may be required for running on non Jisc laptops. It is a dictionary type containing some browser metadata to "spoof" a web browser.

```python
import pandas as pd
url = 'https://www.hesa.ac.uk/data-and-analysis/sb265/figure-1.csv'
storage_options = {'User-Agent': 'Mozilla/5.0'}
pd.read_csv(url, storage_options=storage_options, skiprows=22)
```

HESA's open data prepends a metadata section above the open data in CSVs. skiprows=22 removes this, the value of skiprows will need to change dependent on how many years of data the CSV contains.
Bulletins are typically a fixed 5 or 10 years where the data is available, so number of rows to skip will be consistent. This is not the case for open data.



As the purpose of this code is to compare two HESA datasets, it is advised to create a simple function to read this data, rather than repeat the code block.

```python
def get_hesa_csv(url, skip):
    storage_options = {'User-Agent': 'Mozilla/5.0'}
    return pd.read_csv(url, storage_options=storage_options, skiprows=skip)

df1 = get_hesa_csv('https://www.hesa.ac.uk/data-and-analysis/sb265/figure-1.csv', skip=23)
```
