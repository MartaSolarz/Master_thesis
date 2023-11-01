import pandas as pd
import pingouin as pg
from functions.tests.helper import make_decision
from statsmodels.stats.contingency_tables import mcnemar
from scipy.stats import ttest_rel, shapiro, levene


def mcnemar_test(df: pd.DataFrame, column1: str, column2: str, alpha=0.05) -> None:
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
    result = mcnemar(table)
    p_val = result.pvalue
    print('McNemar statistic:', result.statistic)
    print('p-value:', p_val)
    make_decision(p_val, alpha)


def ttest_or_wilcoxon(groups: list[pd.Series], alpha=0.05) -> None:
    """
    Function to perform either the t-test or the Wilcoxon test for dependent samples.

    Parameters:
    groups (list[Series]): The list of two groups to be tested.
    alpha (float): Significance level.

    Returns:
    None.
    """
    if len(groups) != 2:
        print('Invalid length.')
        return

    if normality_test(groups, alpha) and homogeneity_var_test(groups, alpha):
        print('Conducting t-test...')
        ttest_paired(groups, alpha)
        return

    print('Conducting Wilcoxon test...')
    wilcoxon_test(groups, alpha)


def ttest_paired(groups: list[pd.Series], alpha=0.05) -> None:
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


def wilcoxon_test(groups: list[pd.Series], alpha=0.05) -> None:
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

    result = pg.wilcoxon(groups[0], groups[1])
    p_val = result['p-val'][0]
    print('Wilcoxon statistic:', result['W-val'][0])
    print('p-value:', p_val)
    make_decision(p_val, alpha)


def normality_test(groups: list[pd.Series], alpha=0.05) -> bool:
    """
    Conducts a test to check if the distribution is Gaussian.

    Args:
    groups (list[pd.Series]): The list of groups to be tested for normality.
    alpha (float): The significance level for the test.

    Returns:
    bool: True if all groups have a Gaussian distribution, False otherwise.
    """
    print('Conducting normality test...')
    all_normal = True
    for data in groups:
        stats, p_value = shapiro(data)
        if p_value < alpha:
            all_normal = False
    return all_normal

def homogeneity_var_test(groups: list[pd.Series], alpha=0.05) -> bool:
    """
    Conducts a homogeneity variance test.

    Args:
    groups (list[pd.Series]): The list of groups to be tested for normality.
    alpha (float): The significance level for the test.

    Returns:
    bool: True if variances are homogeneity, False otherwise.
    """
    print('Conducting homogeneity variance test...')
    _, p_value = levene(*groups)
    if p_value < alpha:
        return False
    return True