import pandas as pd
import os

os.chdir('D:/python/project/first/practice')
data=pd.read_excel('房价与工资.xlsx')

print(data)


import pyecharts

bar=Bar