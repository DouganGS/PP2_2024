import re 

import re

with open('receipts.txt','r', encoding="utf-8") as file:
    txt = file.read()
costs = re.findall('Стоимость\n\w+[ \w]*,\w+', txt)
names = re.findall('[0-9]{1}\.\n\w+ [^(№)\d,.]*',txt)
name_of_products = list(x[3:] for x in names)

print('\n'.join(name_of_products),'\n')
print('\n'.join(costs))
