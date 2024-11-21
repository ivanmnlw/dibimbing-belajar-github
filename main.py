import pandas as pd

def read_csv():
    df = pd.read_csv('username.csv', sep = ';')
    return df

print(read_csv())