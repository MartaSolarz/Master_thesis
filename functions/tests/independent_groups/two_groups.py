from scipy.stats import chi2_contingency, fisher_exact, mannwhitneyu, ttest_ind
import pandas as pd
from functions.tests.helper import make_decision, create_contingency_table, is_sample_size_enough, normality_test, homogeneity_var_test, is_equivalence


def chi2_or_fisher_test(df: pd.DataFrame, variable1: str, variable2: str, alpha=0.05):
    """
    Conducts a statistical test between two categorical variables.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    variable1 (str): The name of the first variable.
    variable2 (str): The name of the second variable.
    alpha (float): The significance level for the test. Default is 0.05.

    Returns:
    None
    """
    tab = create_contingency_table(df, variable1, variable2)
    print(tab)
    if is_sample_size_enough(tab):
        print('Chi2 test conducted...')
        p_value = chi2_test(tab)
    else:
        print('Fisher test conducted...')
        p_value = fisher_test(tab)

    make_decision(p_value, alpha)


def chi2_test(data: pd.DataFrame, yate_corr=False) -> float:
    """
    Function to conduct chi-squared test.

    Args:
    data (DataFrame): The contingency table.
    yate_corr (bool): Yate's correction flag.

    Returns:
    float: p-value.
    """
    chi2_stat, p_value, _, _ = chi2_contingency(data, correction=yate_corr)
    print('Chi-squared test statistic value:', chi2_stat)
    print('P-value:', p_value)
    return p_value


def fisher_test(data: pd.DataFrame) -> float:
    """
    Function to conduct Fisher test.

    Args:
    data (DataFrame): The contingency table.

    Returns:
    float: p-value.
    """
    result = fisher_exact(data)
    print('Fisher test statistic value:', result.statistic)
    print('P-value:', result.pvalue)
    return result.pvalue


def ttest_or_mannwhitney_test(df: pd.DataFrame, numerical_param: str, binary_param: str, alpha=0.05, var_1=0, var_2=1) -> None:
    """
    Conducts a test between a quantitative parameter and a binary parameter.

    Args:
    df (DataFrame): The DataFrame containing the data.
    numerical_param (str): The name of the numerical parameter.
    binary_param (str): The name of the binary parameter.
    alpha (float): The significance level for the test. Default is 0.05.
    var_1, var_2 (int, str): split category variables.

    Returns:
    None
    """
    data_group1 = df[df[binary_param] == var_1][numerical_param]
    data_group2 = df[df[binary_param] == var_2][numerical_param]
    groups = [data_group1, data_group2]
    if any(len(group) < 3 for group in groups):
        print('Data have not at least length 3...')
        print('Mann-Whitney test conducted...')
        p_value = mann_whitney_test(groups, print_flag=False)
    elif normality_test(groups, alpha) and homogeneity_var_test(groups, alpha) and is_equivalence(groups):
        print('T-Student test conducted...')
        p_value = t_test(groups)
    else:
        print('Mann-Whitney test conducted...')
        p_value = mann_whitney_test(groups, print_flag=False)

    make_decision(p_value, alpha)

def t_test(groups: list[pd.Series]) -> float:
    """
    Conducts an independent t-test for two groups based on a binary column.

    Args:
    groups (list[pd.Series]): The list of groups.

    Returns:
    float: p-value.
    """
    if len(groups) != 2:
        raise ValueError("Test requires two groups.")

    data_group1, data_group2 = groups
    t_stat, p_value = ttest_ind(data_group1, data_group2)
    print('T-statistic:', t_stat)
    print('p-value:', p_value)
    return p_value


def mann_whitney_test(groups: list[pd.Series], print_flag=True, alpha=0.05):
    """
    Conducts Mann-Whitney-Wilcoxon test for two groups.

    Args:
    groups (list[pd.Series]): The list of groups.

    Returns:
    float: p-value.
    """
    data_group1, data_group2 = groups
    statistic, p_value = mannwhitneyu(data_group1, data_group2)
    print('U-statistic:', statistic)
    print('p-value:', p_value)
    if print_flag:
        make_decision(p_value, alpha)
        return
    return p_value
