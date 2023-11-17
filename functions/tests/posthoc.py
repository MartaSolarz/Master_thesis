import pandas as pd
import statsmodels.api as sm
from scipy.stats import rankdata
import numpy as np
from tabulate import tabulate
from colorama import Fore, Style
from scikit_posthocs import posthoc_nemenyi
import pingouin as pg
from functions.tests.helper import make_decision

def anova_posthoc(df: pd.DataFrame, dependent_variable: str, independent_variable: str, subject='ID', alpha=0.05):
    """
    Perform post hoc analysis following ANOVA.

    Args:
    df (pd.DataFrame): DataFrame containing the data.
    dependent_variable (str): Name of the dependent variable column.
    independent_variable (str): Name of the independent variable column.
    subject (str): Name of the column containing subject IDs (default='ID').
    alpha (float): Significance level (default=0.05).

    Returns:
    None: Prints pairwise comparisons and corrected p-values.
    """

    posthoc = pg.pairwise_tests(dv=dependent_variable, within=independent_variable, subject=subject, data=df, padjust='holm')
    result = posthoc[['A', 'B', 'p-corr']]

    for index, row in result.iterrows():
        print('-----------------------')
        print(f"Groups: {row['A']} vs {row['B']}")
        print(f"P-value: {row['p-corr']}")
        make_decision(row['p-corr'], alpha)


def posthocTukey_test(df: pd.DataFrame, dependent_variable: str, independent_variable: str) -> None:
    """
    Conducts a posthoc Tukey test for parametric data sets.

    Args:
    df (DataFrame): The DataFrame containing the data.
    dependent_variable (str): The name of the dependent variable.
    independent_variable (str): The name of the independent variable.

    Returns:
    None
    """
    posthoc = sm.stats.multicomp.MultiComparison(df[dependent_variable], df[independent_variable])
    tukey_result = posthoc.tukeyhsd()
    print(tukey_result)


def posthocNemenyi_test(df: pd.DataFrame, dependent_variable: str, independent_variable: str, alpha=0.05) -> None:
    """
    Conducts a posthoc Nemenyi test for non-parametric data sets and displays results in a table format.

    Args:
    df (DataFrame): The DataFrame containing the data.
    dependent_variable (str): The name of the dependent variable.
    independent_variable (str): The name of the independent variable.
    alpha (float): The significance level.

    Returns:
    None
    """
    groups = [df[df[independent_variable] == i][dependent_variable] for i in df[independent_variable].unique()]
    ranks = [rankdata(group) for group in groups]
    nemenyi_result = posthoc_nemenyi(ranks)

    headers = [str(i) for i in df[independent_variable].unique()]
    table = []
    for i, row in enumerate(np.array(nemenyi_result)):
        row_values = []
        for p_value in row:
            if p_value < alpha:
                row_values.append(f"{Fore.RED}{p_value:.6f}{Style.RESET_ALL}")
            else:
                row_values.append(f"{p_value:.6f}")
        table.append([df[independent_variable].unique()[i]] + row_values)

    print(tabulate(table, headers=[""] + headers, tablefmt="grid"))


def posthocNemenyi2_test(df: pd.DataFrame, var: str, param='diff', alpha=0.05) -> None:
    """
    Conducts a posthoc Nemenyi test for non-parametric data sets and displays results in a table format.

    Args:
    df (DataFrame): The DataFrame containing the data.
    var (str): The name of the independent variable.
    param (str): The name of the dependent variable.
    alpha (float): The significance level.

    Returns:
    None
    """

    groups = [df[param][df[var] == category] for category in pd.unique(df[var])]
    nemenyi_result = posthoc_nemenyi(groups)

    headers = [str(i) for i in df[var].unique()]
    table = []
    for i, row in enumerate(np.array(nemenyi_result)):
        row_values = []
        for p_value in row:
            if p_value < alpha:
                row_values.append(f"{Fore.RED}{p_value:.6f}{Style.RESET_ALL}")
            else:
                row_values.append(f"{p_value:.6f}")
        table.append([df[var].unique()[i]] + row_values)

    print(tabulate(table, headers=[""] + headers, tablefmt="grid"))