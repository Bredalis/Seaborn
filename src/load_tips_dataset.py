
# Libraries
import seaborn as sns


# Load the dataset
tips = sns.load_dataset("tips")

# Rename columns for clarity
tips.columns = [
    "total",
    "tip",
    "gender",
    "smoker",
    "day",
    "time",
    "party_size",
]

# Display the dataset
print(f"Tips dataset:\n{tips}")
