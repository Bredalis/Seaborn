
import seaborn as sns
import matplotlib.pyplot as plt

from penguins_dataset import penguins


# Plot style configuration
sns.set_theme(style="darkgrid", context="talk")

# Create relational plot
relational = sns.relplot(
    data=penguins,
    height=7,
    aspect=1.2,
    markers=["s", ".", "P", "d"]
)

# Configure titles and labels
relational.set(title="Penguin Analysis")
relational.set_xlabels("Penguin Numbers")
relational.set_ylabels("Variables")

plt.show()
