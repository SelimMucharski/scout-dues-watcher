import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the csv file
account_csv = pd.read_csv('secret/account_statement.csv', sep=";", skiprows=25, index_col=False)

# print(account_csv)

# saving xlsx file
account_xlsx = pd.ExcelWriter('secret/account_statement.xlsx')
account_csv.to_excel(account_xlsx, index=False)

describes = account_csv["#Opis operacji"]

words = []

for describe in describes:
    words_holder = describe.split()
    print(words_holder)
    if "KWARTAŁ" in words_holder:
        words = words + words_holder

plt.hist(words)
plt.show() 

account_xlsx.close()