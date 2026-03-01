
import seaborn as sns
import matplotlib.pyplot as plt

from load_tips_dataset import tips


def categorical_plots(kind, hue=None, x="day", y="total", col="smoker"):
    """
    Create categorical plot from tips dataset.
    
    Args:
        kind: Plot type (box, boxen and violin.)
        hue: Variable for color coding (optional)
        x: X-axis variable (default: day)
        y: Y-axis variable (default: total)
        col: Column variable for subplots (default: smoker)
    """
    sns.catplot(
        x=x,
        y=y,
        data=tips,
        kind=kind,
        col=col,
        hue=hue
    )
    plt.show()


if __name__ == "__main__":
    # Generate different plot types
    plot_types = ["box", "boxen", "violin"]
    
    for plot_type in plot_types:
        categorical_plots(plot_type)
    
    # Violin plot with smoker as hue
    categorical_plots("violin", hue="smoker")
