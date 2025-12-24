import pandas as pd
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alex", "Ben", "Cara"]
})
df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [88, 92, 85]
})
merged = pd.merge(df1, df2, on="ID")
print(merged)
