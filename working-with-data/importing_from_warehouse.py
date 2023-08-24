# Getpass is useful but optional - it returns the current username - this is then 
# inserted in the SQL connection
# sqlalchemy is necessary to connect to the warehouse
# Both can be installed with 'pip install _____' in the console
import getpass
import pandas as pd
from urllib import parse
from sqlalchemy import create_engine


# SQL string
# it's suggested that SQL strings are wrapped with speech marks rather than apostrophes
# apostrophes are commonly used in SQL so would break the string unless handled
sqlstring = """
SELECT * FROM [x].[x]
"""

# Connection string
# A lot of this can be identified via the connection pop-up in SSMS.
# Getpass is used here to auto-populate the user ID (UID) field
connecting_string = "__" # Removed for access security

# Pre-processing the connection string
# Used by SQLAlchemy to set up the DBAPI for connection to the warehouse
# Quote plus, the only reason for urllib here replaces spaces in the above with "+"
# this creates a string in a format that is understood by the SQL connection

# The 'connection_string' below has been suppressed for security - this can be acquired upon request
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % 
                       parse.quote_plus(connection_string))

# Perform the transaction of connecting to the warehouse using the above
# Ex-HESA specific - you need to have the VPN connected for this step
connection = engine.connect()

# Pandas interprets the SQL text and sends that command via the connection
# a dataframe is returned
df = pd.read_sql(sqlstring, connection)


# As SQL code can be lengthy, it is advised to keep that in a separate file
# This file can be read in as a string variable and run as with the embedded code
sqlfile = !!! Need to link a file here
sqlstring = open(sqlfile, mode='r', encoding='utf-8-sig').read()
df = pd.read_sql(sqlstring, connection)
