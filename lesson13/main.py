import csv


import pandas as pd

#products = ['apples', 'grapes', 'oranges', 'bananas']

#sales= [150,200,180,90]

#sales_series = pd.Series(sales, index=products)

# total_sales = sales_series.sum()
#best_selling_product= sales_series.idxmax()
#print(f"Best Selling product: {best_selling_product}")
#
# data= {'Name': ['Arion', 'John', 'Micheal'],
#        'Age': [21,59,32],
#        'City': ['Prishtine', 'New York', 'London']
#        }
# df = pd.DataFrame(data)
# print(df)

# data = [
#     ['Name', 'Age', 'City'],
#     ['Arion', 21, 'Prishtine'],
#     ['Micheal', 25, 'New York'],
#     ['John', 48, 'London']
# ]
#
# with open('example.csv','w' ,newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#
#     print("Data written to example.cvs")
#
# with open('example.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# data = [
#     {'Name': 'Dorart', 'Age': 17, 'City': 'Vushtrri'},
#     {'Name': 'Fat', 'Age': 17, 'City': 'Prishtine'},
#     {'Name': 'Klea', 'Age': 17, 'City': 'Prishtine'}
# ]
# header = ['Name', 'Age', 'City']
#
# with open('people.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(data)
#
# print('data written to people.csv')
#
#
# with open('people.csv','r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(dict(row))


