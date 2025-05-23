import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from windrose import WindroseAxes


def plot_numeric_histograms(df: pd.DataFrame, bins: int = 30, cols_per_row: int = 4, figsize: tuple = (20, 15)):
    """
    Plots histograms for all numeric columns in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing numeric columns.
        bins (int): Number of bins for the histogram.
        cols_per_row (int): Number of subplots per row.
        figsize (tuple): Size of the full figure.
    """
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    num_cols = len(numeric_cols)

    if num_cols == 0:
        print("No numeric columns found to plot.")
        return

    rows = (num_cols + cols_per_row - 1) // cols_per_row  # Ceiling division

    plt.figure(figsize=figsize)
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(rows, cols_per_row, i)
        sns.histplot(df[col], kde=True, bins=bins)
        plt.title(col)
    plt.tight_layout()
    plt.show()




def plot_time_series(
    df: pd.DataFrame,
    cols: list,
    timestamp_col: str = 'Timestamp',
    y_label: str = 'Average Value',
    freq_title_map: dict = {
        'D': 'Daily',
        'M': 'Monthly'
    },
    freqs: list = ['D', 'M'],
    figsize: tuple = (14, 6)
):
    """
    Plots time series trends with flexible resampling frequencies and titles.

    Args:
        df (pd.DataFrame): DataFrame containing time series data.
        cols (list): List of column names to visualize.
        timestamp_col (str): Name of the timestamp column.
        y_label (str): Y-axis label.
        freq_title_map (dict): Dict mapping frequency codes (e.g., 'D') to plot titles (e.g., 'Daily').
        freqs (list): List of resampling frequencies to plot, e.g., ['D', 'M'].
        figsize (tuple): Size of each plot.
    """
    if timestamp_col not in df.columns:
        raise ValueError(f"'{timestamp_col}' column is required in the dataframe.")
    
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    df.set_index(timestamp_col, inplace=True)

    for freq in freqs:
        if freq not in freq_title_map:
            raise ValueError(f"Missing title for frequency '{freq}' in freq_title_map.")
        
        resampled = df[cols].resample(freq).mean()

        plt.figure(figsize=figsize)
        resampled.plot(ax=plt.gca())
        plt.title(f"{freq_title_map[freq]} Trend of {' | '.join(cols)}")
        plt.ylabel(y_label)
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def plot_correlation_heatmap(df, columns, region_name=''):
    """Plot a correlation heatmap for the specified numeric columns."""
    plt.figure(figsize=(8, 6))
    corr = df[columns].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f'{region_name} - Correlation Heatmap')
    plt.tight_layout()
    plt.show()


def plot_scatter_plots(df, x_columns, y_column='GHI', hue_column='GHI', region_name=''):
    """Plot scatter plots for multiple x-columns vs y-column."""
    for x in x_columns:
        plt.figure(figsize=(8, 6))
        # sns.scatterplot(x=x, y=y_column, hue=hue_column, palette='viridis', data=df)
        if hue_column:
            sns.scatterplot(x=x, y=y_column, hue=hue_column, palette='viridis', data=df)
        else:
            sns.scatterplot(x=x, y=y_column, data=df)
        plt.title(f'{region_name} - {x} vs {y_column}')
        plt.tight_layout()
        plt.show()



def plot_histograms_side_by_side(df, columns, colors=None, titles=None, xlabels=None, bins=30, figsize_per_plot=(5,4)):
    """
    Plot histograms for given columns in pairs, side-by-side (2 per row),
    styled similar to your example (simple matplotlib histograms).

    Args:
        df (pd.DataFrame): The data frame.
        columns (list): List of column names (str) to plot.
        colors (list or None): List of colors for each histogram; defaults to alternating 'orange' and 'blue'.
        titles (list or None): List of titles for each histogram; defaults to "Histogram of <col>".
        xlabels (list or None): List of x-axis labels for each histogram; defaults to column names.
        bins (int): Number of bins for the histograms.
        figsize_per_plot (tuple): Size of each subplot (width, height).

    """
    n = len(columns)
    rows = (n + 1) // 2  # 2 plots per row
    figsize = (figsize_per_plot[0] * 2, figsize_per_plot[1] * rows)

    # Default colors if not provided
    if colors is None:
        colors = ['orange', 'blue'] * (n // 2 + 1)

    # Default titles if not provided
    if titles is None:
        titles = [f"Histogram of {col}" for col in columns]

    # Default xlabels if not provided
    if xlabels is None:
        xlabels = columns

    plt.figure(figsize=figsize)

    for i, col in enumerate(columns, 1):
        plt.subplot(rows, 2, i)
        plt.hist(df[col], bins=bins, color=colors[i-1], alpha=0.7)
        plt.title(titles[i-1])
        plt.xlabel(xlabels[i-1])
        plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

def plot_wind_analysis(df: pd.DataFrame, region_name: str = ''):
    """
    Plots wind rose and histograms for a given DataFrame with wind and GHI data.
    
    Parameters:
        df (pd.DataFrame): Must contain columns 'WS', 'WD', and 'GHI'.
        region_name (str): Optional title prefix for plots.
    """
    # Check required columns
    required_cols = ['WS', 'WD', 'GHI']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain columns: {required_cols}")
    
    # 1. Wind Rose Plot
    fig = plt.figure(figsize=(8, 8))
    ax = WindroseAxes.from_ax(fig=fig)
    ax.bar(df['WD'], df['WS'], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend(title="Wind Speed (m/s)")
    plt.title(f"{region_name} - Wind Rose: Wind Speed & Direction")
    plt.show()

    # 2. Histograms using your existing function
    plot_histograms_side_by_side(
        df,
        columns=['GHI', 'WS'],
        colors=['orange', 'blue'],
        titles=["Histogram of GHI", "Histogram of Wind Speed"],
        xlabels=["GHI (W/m²)", "Wind Speed (m/s)"],
        bins=30
    )


def plot_bubble_chart(df, x_col, y_col, size_col, region_name=''):
    """
    Plots a bubble chart where:
    - x_col is on the x-axis
    - y_col is on the y-axis
    - size_col determines both bubble size and color
    """
    bubble_size = df[size_col]

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(
        df[x_col],
        df[y_col],
        s=bubble_size * 10,   # Adjust scaling factor as needed
        alpha=0.6,
        c=bubble_size,
        cmap='viridis',
        edgecolors='w',
        linewidth=0.5
    )
    plt.colorbar(scatter, label=size_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    title = f'{region_name} - {y_col} vs {x_col} (size & color by {size_col})' if region_name else f'{y_col} vs {x_col}'
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
