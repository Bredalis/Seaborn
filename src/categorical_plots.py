
import seaborn as sns
import matplotlib.pyplot as plt

from load_tips_dataset import tips


def categorical_plots(kind="strip"):
    """
    Create categorical plot from tips dataset.
    
    Args:
        kind: Type of plot (strip, swarm, box, violin, etc.)
    """
    sns.catplot(
        x="day",
        y="total",
        data=tips,
        hue="party_size",
        s=7,
        col="smoker",
        kind=kind
    )
    plt.show()


if __name__ == "__main__":
    categorical_plots("strip")
    categorical_plots("swarm")
