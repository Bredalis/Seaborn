
import seaborn as sns
import matplotlib.pyplot as plt

from penguins_dataset import penguins


# Function to generate scatter plots
def scatter_plots(hue, size, row=None, size_var=None, 
                  sizes=None, style=None, col=None):
    sns.relplot(
        data=penguins,
        x="bill_length_mm",
        y="flipper_length_mm",
        hue=hue,
        s=size,
        row=row,
        size=size_var,
        sizes=sizes,
        style=style,
        col=col
    )
    plt.show()


# Generate different scatter plots
scatter_plots(None, None)  # Simple
scatter_plots("body_mass_g", 300)  # Hue and fixed size
scatter_plots("species", 300)

# Grid, custom size, and style
scatter_plots("species", 300, "sex", "body_mass_g", (100, 500), "sex", "island")
