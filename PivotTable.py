import pandas as pd
df = pd.DataFrame({
    "Class": ["10A", "10A", "10B", "10B"],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [88, 92, 85, 90]
})
pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Class",
    columns="Subject",
    aggfunc=["mean", "max", "min"]  # multiple aggregation functions
)
print(pivot)
