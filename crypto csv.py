import csv

with open('C:\\Users\\user\\Downloads\\or.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    num = []
    for row in reader:
        num.append(row)
dict_keys = num[0]
dict_values = num[1:len(num)]
list_of_dict = [dict(zip(dict_keys, i)) for i in dict_values]
items = []
items2 = []
rounded = []
for item in list_of_dict:
    items.append(item['Total (inc GST)'])
for item in items:
    if item.endswith('AUD'):
        items = float(item[:-3])
        items2.append(items)
for item in items2:
    x = round(item, 2)
    rounded.append(x)
total = sum(rounded)
print(round(total, 2))
