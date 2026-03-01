
import seaborn as sns
import matplotlib.pyplot as plt

from penguins_dataset import penguins


# Line plot
sns.lineplot(
    x="bill_length_mm",
    y="flipper_length_mm",
    data=penguins,
    hue="species"
)
plt.show()
