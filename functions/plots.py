import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from functions.tests.categorical_only import create_contingency_table


def plot_heatmap(df: pd.DataFrame, column1: str, column2: str, label1: str, label2: str, title="", cmap="YlGnBu"):
    """
    Generates a heatmap based on a contingency table.

    Args:
    df (DataFrame): Data in the form of a DataFrame.
    column1 (str): Name of first categorical variable.
    column2 (str): Name of second categorical variable.
    label1 (str): Label for column1.
    label2 (str): Label for column2.
    title (str): Title of the plot (optional).
    cmap (str): Color palette (optional).

    Returns:
    None
    """
    table = create_contingency_table(df, column1, column2)
    sns.heatmap(table, annot=True, fmt="d", cmap=cmap)
    plt.xlabel(label2)
    plt.ylabel(label1)
    plt.title(title)
    plt.show()


def plot_scatter_with_regression(df: pd.DataFrame, column_quantitative: str, column_category: str, label_quantitative: str, label_category: str, title="Scatter Plot with Regression"):
    """
    Generates a scatter plot with a linear regression line.

    Args:
    df (DataFrame): Data in the form of a DataFrame.
    column_quantitative (str): Name of first quantitative variable.
    column_category (str): Name of categorical variable.
    label_quantitative (str): Label for quantitative data.
    label_category (str): Label for categorical data.
    title (str): Title of the plot (optional).

    Returns:
    None
    """
    x = df[column_quantitative]
    y = df[column_category]
    sns.set(style="whitegrid")
    sns.regplot(x=x, y=y, color='b')
    plt.title(title)
    plt.xlabel(label_quantitative)
    plt.ylabel(label_category)
    plt.grid(True)
    plt.show()


def plot_multi_boxplot(df: pd.DataFrame, category_param: str, continue_param: str, label_category: str, label_continue: str, title: str = "Boxplot dla grup"):
    """
    Generates a boxplot for multiple series of data based on a categorical parameter.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    category_param (str): The name of the column with categorical data.
    continue_param (str): The name of the column with continuous data.
    label_category (str): Label for categorical data.
    label_continue (str): Label for continuous data.
    title (str, optional): Title of the plot. Default is "Boxplot dla grup".

    Returns:
    None
    """
    sns.set(style="whitegrid")
    sns.boxplot(data=df, x=category_param, y=continue_param, orient="v")
    plt.title(title)
    plt.grid(True, axis='y')
    plt.xlabel(label_category)
    plt.ylabel(label_continue)
    plt.show()


def plot_two_boxplots(A, B, label_A='A', label_B='B', label='Value', title='Boxplot dla grup A i B'):
    """
    Generates a boxplot for two series of continuous data.

    Args:
    A (pd.Series): The first series of continuous data.
    B (pd.Series): The second series of continuous data.
    label_A (str, optional): Label for series A. Default is 'A'.
    label_B (str, optional): Label for series B. Default is 'B'.
    label (str, optional): Label for the y-axis of the plot. Default is 'Value'.
    title (str, optional): Title of the plot. Default is 'Boxplot dla grup A i B'.

    Returns:
    None
    """
    data = {label_A: A, label_B: B}
    df = pd.DataFrame(data)
    sns.set(style="whitegrid")
    sns.boxplot(data=df, orient="v")
    plt.title(title)
    plt.grid(True, axis='y')
    plt.ylabel(label)
    plt.show()


def plot_multi_density(df: pd.DataFrame, continue_param: str, category_param: str, label: str, label_legend: str, title="Wykres gęstości dla grup"):
    """
    Generates a density plot for multiple series of data based on a categorical parameter.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    continue_param (str): The name of the column with continuous data.
    category_param (str): The name of the column with categorical data.
    label (str): Label for the x-axis of the plot.
    label_legend (str): Label for the legend of the plot.
    title (str, optional): Title of the plot. Default is "Wykres gęstości dla grup".

    Returns:
    None
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    sns.set(style="whitegrid")
    for i, group in enumerate(groups):
        sns.kdeplot(group, label=df[category_param].unique()[i], warn_singular=False)

    plt.xlabel(label)
    plt.title(title, size=12)
    plt.legend(title=label_legend)
    plt.grid(True)
    plt.show()


def plot_two_density(A, B, label_A='A', label_B='B', label='Value', title='Wykres gęstości dla grup A i B'):
    """
    Generates a density plot for two series of continuous data.

    Args:
    A (pd.Series): The first series of continuous data.
    B (pd.Series): The second series of continuous data.
    label_A (str, optional): Label for series A. Default is 'A'.
    label_B (str, optional): Label for series B. Default is 'B'.
    label (str, optional): Label for the x-axis of the plot. Default is 'Value'.
    title (str, optional): Title of the plot. Default is 'Wykres gęstości dla grup A i B'.

    Returns:
    None
    """
    sns.set(style="whitegrid")
    sns.kdeplot(A, label=label_A, fill=True)
    sns.kdeplot(B, label=label_B, fill=True)
    plt.xlabel(label)
    plt.title(title)
    plt.legend()
    plt.show()

