import csv
from csv import DictReader

with open('input.csv', 'r') as csv_file: 
    csv_reader = DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
       #print(row [line_count]) 
        print(row)
    for row in csv_reader:
       #print(row [line_count]) 
        print(row)
        
=====================================================================================
import csv
from csv import DictReader
import pandas as pd
import numpy as np
import datatest as dt



def read_file():
    df = pd.read_csv(filename)
    if(df.empty):
        print ('CSV file is empty')
    else:
        print ('CSV file is not empty')
        return df
filename = 'test.csv'

missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
df = pd.read_csv("test.csv", na_values = missing_value_formats)

def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan

# apply make_int function to the entire series using map
df['CID'] = df['CID'].map(make_int)
print(df['CID'].head())
df['Chargeback Case ID'] = df['Chargeback Case ID'].map(make_int)
print(df['Chargeback Case ID'].head())
df['Case Number'] = df['Case Number'].map(make_int)
print(df['Case Number'].head())
df['REP ID'] = df['REP ID'].map(make_int)
print(df['REP ID'].head())

missing_value_formats = ["0-9"]
df = pd.read_csv("test.csv", na_values = missing_value_formats)
def make_str(i):
    try:
        return str(i)
    except:
        return pd.np.nan
df['Desired State'] = df['Desired State'].map(make_str)
print(df['Desired State'].head())
df['DNF Reason'] = df['DNF Reason'].map(make_str)
print(df['DNF Reason'].head())


with open('test.csv', 'r') as csv_file:
    csv_reader = DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
    for row in csv_reader:
        print(row)

df = pd.read_csv(filename)
data = pd.read_csv('test.csv')
df = df[sorted(data)]
validation = df

for col in df.columns:
    miss = df[col].isnull().sum()
    if miss>0:
        print("{} has {} missing value(s)".format(col,miss))
    else:
        print("{} has NO missing value!".format(col))
filename = 'test.csv'






============================================

missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
df = pd.read_csv("test.csv", na_values = missing_value_formats)

def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan

# apply make_int function to the entire series using map
df['CID'] = df['CID'].map(make_int)
print(df['CID'].head())
        
        
        https://go.slack.com/get-started/enQtMjM2NTM5MjE4NTY5Ny1mOTdlOTk1MjI3N2ExNWFhYTc1MGI4MWY1YmRiNzJmZWI3OTBjZmRlNDU3MGM3ZDgxOGY5ODUzZjJmN2JjZjBm?e=anVzdGljZS5rQG1pZGlnYXRvci5jb20%3D&i=default&m=slack&x=x-a2365392208017
        
        
        https://www.dezyre.com/recipes/perform-data-validation-python-by-processing-only-matched-columns
