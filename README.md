# lastguru
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
