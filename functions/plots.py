import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from functions.tests.categorical_only import create_contingency_table


def plot_heatmap(df, column1, column2, label1, label2, title="", cmap="YlGnBu"):
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


def plot_scatter_with_regression(df: pd.DataFrame, columnX: str, columnY: str, title="Scatter Plot with Regression"):
    """
    Generates a scatter plot with a linear regression line.

    Args:
    df (DataFrame): Data in the form of a DataFrame.
    columnX (str): Name of first categorical variable.
    columnY (str): Name of second categorical variable.
    title (str): Title of the plot (optional).

    Returns:
    None
    """
    x = df[columnX]
    y = df[columnY]
    sns.set(style="whitegrid")
    sns.regplot(x=x, y=y, color='b', marker='+', scatter_kws={'s': 100})
    plt.title(title)
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


# def create_histogram(df, title, column, column_label):
#     """
#     Generates a histogram for a specific column in the DataFrame, along with an estimated empirical normal distribution curve.
#
#     Args:
#     df (DataFrame): The DataFrame containing the data.
#     title (str): Title of the histogram.
#     column (str): Name of the column to create a histogram for.
#     column_label (str): Label for the column on the x-axis.
#
#     Returns:
#     None
#     """
#
#     mu, sigma = df[column].mean(), df[column].std()
#     x = np.linspace(0, max(df[column]), 100)
#     y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
#     plt.xlim([0, max(df[column])])
#     plt.xlabel(column_label)
#
#     plt.hist(df[column], 20, density=True, alpha=0.7, rwidth=0.95)
#     plt.plot(x, y, '--r', label='Approximated empirical normal distribution curve from the sample')
#     plt.title(f"{title} Histogram\n($\mu$={mu:.2f}, $\sigma$={sigma:.2f})")
#     plt.legend()
#     plt.grid(True, axis='y')
#     plt.show()


###################################
def create_histogram_for_many(dfs, names, col, col_label):
    for i, df in enumerate(dfs):
        create_histogram(df, names[i+1], col, col_label)


# def create_histogram(df, name, col, col_label):
#     mu, sigma = df[col].mean(), df[col].std()
#     x = np.linspace(0, max(df[col]), 100)
#     y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
#     plt.xlim([0, max(df[col])])
#     plt.xlabel(col_label)
#
#     plt.hist(df[col], 20, density=True, alpha=0.7, rwidth=0.95)
#     plt.plot(x, y, '--r',
#              label='przybliżona krzywa empirycznego\nrozkładu normalnego z próby')
#     plt.title(f"{name} Histogram\n($\mu$={mu:.2f}, $\sigma$={sigma:.2f})")
#     plt.legend()
#     plt.grid(True, axis='y')
#     plt.show()

def create_categorical_time_plot(df, col, col_label, categorical_column_name, categorical_column_label,  name):
    """
    Create categorical time plot.
    """
    time_column_name = col
    categories = df[categorical_column_name].unique()

    plt.figure(figsize=(10, 6))
    for i, category in enumerate(categories):
        category_data = df[df[categorical_column_name] == category]
        plt.scatter(category_data[time_column_name], [i + 1] * len(category_data), label=category)

    plt.xlim([0, df[time_column_name].max()+10000])
    plt.yticks(range(1, len(categories) + 1), categories)
    plt.xlabel(col_label)
    plt.ylabel(categorical_column_label)
    plt.title(f'{name} Rozkład czasu vs. {categorical_column_label}')
    plt.legend()
    plt.grid(True)
    plt.show()


def create_scatterWithregression_and_residuals_plots(df, continue_param, category_param, labelContinue, labelCategory):
    """
    Create scatter plot with linear regression and residuals plot.
    """
    X = sm.add_constant(df[continue_param])
    model = sm.OLS(df[category_param], X)
    results = model.fit()
    plt.scatter(df[continue_param], df[category_param])
    plt.plot(df[continue_param], results.fittedvalues, 'r')
    plt.xlabel(labelContinue)
    plt.ylabel(labelCategory)
    plt.title(f"{labelContinue} vs. {labelCategory}")
    plt.grid(True)
    plt.show()

    residuals = df[category_param] - results.fittedvalues
    plt.scatter(df[continue_param], residuals)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel(labelContinue)
    plt.ylabel('Reszty')
    plt.title('Wykres reszt')
    plt.grid(True)
    plt.show()


def create_scatter_logit_plot_for_many(dfs, names, col1, col2, label1, label2):
    for i, df in enumerate(dfs):
        print('-------------------------------')
        print(names[i+1])
        create_scatter_logit_plot(df, col1, col2, label1, label2)


def create_scatter_logit_plot(df, col1, col2, label1, label2):
    """
    Create scatter plot.
    """
    if not ((0 <= df[col2]) & (df[col2] <= 1)).all():
        df[col2] = (df[col2] - np.min(df[col2])) / (np.max(df[col2]) - np.min(df[col2]))

    plt.scatter(df[col1], df[col2], label='Data Points')
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.title(f'{label1} vs. {label2}')

    logit_model = sm.Logit(df[col2], sm.add_constant(df[col1]))
    result = logit_model.fit(disp=0)
    x_values = np.linspace(np.min(df[col1]), np.max(df[col1]), 100)
    y_values = result.predict(sm.add_constant(x_values))
    plt.plot(x_values, y_values, color='r', label='Logistic Regression Curve')

    plt.legend()
    plt.grid(True)
    plt.show()


def create_roc_curve_and_residuals_plot(df, col1, col2, label1):
    """
    Create ROC curve plot and residuals plot.
    """

    if not ((0 <= df[col2]) & (df[col2] <= 1)).all():
        df[col2] = (df[col2] - np.min(df[col2])) / (np.max(df[col2]) - np.min(df[col2]))

    logit_model = sm.Logit(df[col2], sm.add_constant(df[col1]))
    result = logit_model.fit(disp=0)
    y_pred = result.predict(sm.add_constant(df[col1]))
    fpr, tpr, _ = roc_curve(df[col2], y_pred)

    # Plot ROC curve
    plt.plot([0, 1], [0, 1], color='r', linestyle='--')
    plt.plot(fpr, tpr, marker='.')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Plot')
    plt.grid(True)
    plt.show()

    # Calculate residuals and plot
    y_pred_binary = (y_pred > 0.5).astype(int)
    residuals = df[col2] - y_pred_binary
    plt.scatter(df[col1], residuals)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel(label1)
    plt.ylabel('Residuals')
    plt.title('Residuals Plot')
    plt.grid(True)
    plt.show()


def create_conditional_effects_plot(df, col1, col2, label1, label2):
    """
    Create conditional effects plot.
    """
    sns.lmplot(x=col1, y=col2, data=df, logistic=True, y_jitter=.03)
    plt.title('Wykres warunkowych efektów')
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.grid(True)
    plt.show()
