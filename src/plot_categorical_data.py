
import seaborn as sns
import matplotlib.pyplot as plt

from load_tips_dataset import tips


# Function to plot categorical data
def plot_categorical(y, kind, col, hue):
    sns.catplot(
        x="dia",
        y=y,
        data=tips,
        kind=kind,
        col=col,
        hue=hue
    )
    plt.show()


# Examples of using the function
plot_categorical("total", "point", "smoker", None)
plot_categorical("total", "bar", None, "party_size")
plot_categorical(None, "count", None, "party_size")
