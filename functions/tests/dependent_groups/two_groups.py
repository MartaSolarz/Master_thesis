import pandas as pd
import pingouin as pg
from functions.tests.helper import make_decision, homogeneity_var_test, normality_test
from statsmodels.stats.contingency_tables import mcnemar
from scipy.stats import ttest_rel, wilcoxon


def mcnemar_test(df: pd.DataFrame, column1: str, column2: str, yate_flag=False, alpha=0.05):
    """
    Function to perform McNemar's test for a 2x2 contingency table.

    Parameters:
    df (DataFrame): DataFrame with data.
    column1 (str): Name of the first column.
    column2 (str): Name of the second column.
    alpha (float): Significance level.

    Returns:
    None.
    """
    table = pd.crosstab(df[column1], df[column2])
    print(table)
    if table.size == 1:
        print('Only one sample')
        return
    result = mcnemar(table, exact=yate_flag)
    p_val = result.pvalue
    print('McNemar statistic:', result.statistic)
    print('p-value:', p_val)
    make_decision(p_val, alpha)
    return f"{p_val:.2f}"


def ttest_or_wilcoxon(groups: list[pd.Series], alpha=0.05):
    """
    Function to perform either the t-test or the Wilcoxon test for dependent samples.

    Parameters:
    groups (list[Series]): The list of two groups to be tested.
    alpha (float): Significance level.

    Returns:
    None.
    """
    if len(groups) != 2:
        raise ValueError("Test requires two groups.")

    if normality_test(groups, alpha) and homogeneity_var_test(groups, alpha):
        print('Conducting t-test...')
        p = ttest_paired(groups, alpha)
        return p

    print('Conducting Wilcoxon test...')
    p = wilcoxon_test(groups, alpha)
    return p


def ttest_paired(groups: list[pd.Series], alpha=0.05):
    """
    Function to perform the paired sample t-test.

    Parameters:
    groups (list[Series]): The list of two groups to be tested.
    alpha (float): Significance level.

    Returns:
    None.
    """
    if len(groups) != 2:
        print('Invalid length.')
        return

    t_statistic, p_value = ttest_rel(groups[0], groups[1])
    print(f"t-statistic: {t_statistic}")
    print(f"p-value: {p_value}")
    make_decision(p_value, alpha)
    return f"{p_value:.2f}"


def wilcoxon_test(groups: list[pd.Series], alpha=0.05, method='auto'):
    """
    Function to perform the Wilcoxon signed-rank test for paired samples.

    Parameters:
    groups (list[pd.Series]): The list of two groups to be tested.
    alpha (float): Significance level.

    Returns:
    None.
    """
    if len(groups) != 2:
        print('Invalid length.')
        return
    try:
        result = wilcoxon(groups[0], groups[1], method=method)
    except ValueError:
        print('only one sample')
        return
    p_val = result.pvalue
    print('Wilcoxon statistic:', result.statistic)
    print('p-value:', p_val)
    make_decision(p_val, alpha)
    return f"{p_val:.2f}"
