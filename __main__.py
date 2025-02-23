import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def is_due(transfer: dict):
    description: str = transfer["#Opis operacji"]
    key_words = ["składk", "skladk", "kwarta", "kw.", "przelew express elixir"]
    key_word_pass = False

    for key_word in key_words:
        if key_word in description.lower():
            key_word_pass = True
    
    if not key_word_pass:
        return False

    if not contains_member(transfer, members):
        return False

    # print(transfer["#Kwota"])
    return True

def contains_member(transfer: dict, members: pd.DataFrame):
    for index, member in members.iterrows():
        if member["Surname"][:7].lower() in transfer["#Opis operacji"].lower():
            return True
    
    # if is_due(transfer):
        # print(transfer["#Opis operacji"][:50])
    return False

        
# Reading the csv file
account_csv = pd.read_csv('secret/account_statement.csv', sep=";", skiprows=25, index_col=False)
members = pd.read_csv('secret/membership_list.csv', sep=",", index_col=False)

dues = []
likely_dues = []

for index, transfer in account_csv.iterrows():
    if contains_member(transfer, members) and is_due(transfer):
        dues.append(transfer)
    elif transfer["#Kwota"] in list(["55,00 PLN","110,00 PLN","165,00 PLN", "220,00 PLN", "65,00 PLN", "130,00 PLN", "195,00 PLN", "260,00 PLN"]):
        likely_dues.append(transfer)

print(dues)

words = []
for due in dues:
    words_holder = due["#Opis operacji"].split()
    words = words + words_holder

plt.hist(words)
plt.show() 

pass