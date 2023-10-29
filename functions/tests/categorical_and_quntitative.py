import pandas as pd
from scipy.stats import shapiro, f_oneway, levene, kruskal, ttest_ind, mannwhitneyu

from functions.tests.helper import make_decision


def conduct_categorical_vs_quantitative_for_many_groups_test(df: pd.DataFrame, continue_param: str, category_param: str, alpha=0.05) -> None:
    """
    Conducts a test between a categorical variable and a quantitative variable.

    Args:
    df (DataFrame): The DataFrame containing the data.
    continue_param (str): The name of the continuous parameter.
    category_param (str): The name of the categorical parameter.
    alpha (float): The significance level for the test. Default is 0.05.

    Returns:
    None
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    if any(len(group) < 3 for group in groups):
        print('Data have not at least length 3...')
        print('Kruskal-Wallis test conducted...')
        p_value = kruskal_wallis_test(groups)
    elif normality_test(groups, alpha) and homogeneity_var_test(groups, alpha) and is_sample_size_enough(groups):
        print('ANOVA test conducted...')
        p_value = anova_test(groups)
    else:
        print('Kruskal-Wallis test conducted...')
        p_value = kruskal_wallis_test(groups)

    make_decision(p_value, alpha)


def conduct_categorical_vs_quantitative_for_two_groups_test(df: pd.DataFrame, numerical_param: str, binary_param: str, alpha=0.05) -> None:
    """
    Conducts a test between a quantitative parameter and a binary parameter.

    Args:
    df (DataFrame): The DataFrame containing the data.
    numerical_param (str): The name of the numerical parameter.
    binary_param (str): The name of the binary parameter.
    alpha (float): The significance level for the test. Default is 0.05.

    Returns:
    None
    """
    data_group1 = df[df[binary_param] == 0][numerical_param]
    data_group2 = df[df[binary_param] == 1][numerical_param]
    groups = [data_group1, data_group2]
    if any(len(group) < 3 for group in groups):
        print('Data have not at least length 3...')
        print('Mann-Whitney test conducted...')
        p_value = mann_whitney_test(groups)
    elif normality_test(groups, alpha) and homogeneity_var_test(groups, alpha) and is_equivalence(groups):
        print('T-Student test conducted...')
        p_value = t_test(groups)
    else:
        print('Mann-Whitney test conducted...')
        p_value = mann_whitney_test(groups)

    make_decision(p_value, alpha)


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


def is_sample_size_enough(groups: list[pd.Series], min_size=20):
    """
    Checks if each group in the list has at least the minimum number of elements.

    Args:
    groups (list[pd.Series]): The list of groups to be checked.
    min_size (int): The minimum number of elements required for each group. Default is 20.

    Returns:
    bool: True if each group has at least the minimum number of elements, False otherwise.
    """
    return all(len(group) >= min_size for group in groups)


def anova_test(groups: list[pd.Series]) -> float:
    """
    Conducts an ANOVA test.

    Args:
    groups (list[pd.Series]): The list of groups to be tested for normality.

    Returns:
    float: p-value.
    """
    f_value, p_value = f_oneway(*groups)
    print('F-value:', f_value)
    print('p-value:', p_value)
    return p_value


def kruskal_wallis_test(groups: list[pd.Series]) -> float:
    """
    Conducts a Kruskal-Wallis test.

    Args:
    groups (list[pd.Series]): The list of groups to be tested for normality.

    Returns:
    float: p-value.
    """
    h, p_value = kruskal(*groups)
    print('H:', h)
    print('p-value:', p_value)
    return p_value


def is_equivalence(groups) -> bool:
    """
    Checks if two data sets are equivalence.

    Args:
    groups (list[pd.Series]): The list of groups.

    Returns:
    bool: True if one list is not more than twice as large as the other, False otherwise.
    """
    data1, data2 = groups
    return not (len(data1) > 2 * len(data2) or len(data2) > 2 * len(data1))


def t_test(groups: list[pd.Series]) -> float:
    """
    Conducts an independent t-test for two groups based on a binary column.

    Args:
    groups (list[pd.Series]): The list of groups.

    Returns:
    float: p-value.
    """
    data_group1, data_group2 = groups
    t_stat, p_value = ttest_ind(data_group1, data_group2)
    print('T-statistic:', t_stat)
    print('p-value:', p_value)
    return p_value


def mann_whitney_test(groups: list[pd.Series]) -> float:
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
    return p_value
