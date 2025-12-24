import pandas as pd
df = pd.DataFrame({
    "Name": ["Alex", "Ben", "Cara"],
    "Age": [15, 14, 15],
    "Marks": [88, 92, 85]
})
filtered = df.query("Marks > 85 and Age == 15")
print(filtered)
