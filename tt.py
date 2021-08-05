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

def setUpModule():
    global df
    with dt.working_directory(__file__):
        df = pd.read_csv('test.csv')

class TestValues(dt.DataTestCase):
    @dt.mandatory
    def test_columns(self):
        self.assertValid(
            df.columns,
            {'CID', 'Chargeback_Case_ID', 'Case_Number', 'Desired_State', 'DNF_Reason', 'REP_ID'},
        )

def test_CID(self):
        self.assertValid(df['CID'], int)

def test_Chargeback_Case_ID(self):
        self.assertValid(df['Chargeback_Case_ID'], int)
def test_Csae_Number(self):
        self.assertValid(df['Case_Numer'], int)
def test_Desired_State(self):
        self.assertValidRegex(df['Desired_State'], r'^[A-Z]')
def test_DNR_Reason(self):
        self.assertValidRegex(df['DNF_Reason'], r'^[A-Z]')
def test_REP_ID(self):
        self.assertValid(df['REP_ID'], int)


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
        
        
        
        
        
        https://www.dezyre.com/recipes/perform-data-validation-python-by-processing-only-matched-columns
