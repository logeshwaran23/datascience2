from google.colab import files
import pandas as pd

df = pd.read_excel('e-commerce.csv.xlsx', sheet_name='E Comm')
df.head()

df.shape
df.info()
df.describe(include='all')
