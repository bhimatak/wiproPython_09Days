import os
import csv

# os.mkdir("data")
#os.rmdir("data")
content = [
    ['Name','Age','City'],
    ['Bhima',45,'Bangalore']
]

with open("data\\sap1.csv","w",newline="") as file:
    w = csv.writer(file)

    w.writerows(content)

# os.remove("data\\sap1.csv")