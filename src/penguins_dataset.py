
# Libraries
import seaborn as sns

# Load the dataset
penguins = sns.load_dataset("penguins")

# Assign column names
penguins.columns = [
    "species",
    "island",
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex",
]

# Display the dataset
print(f"Penguins dataset:\n{penguins}")
