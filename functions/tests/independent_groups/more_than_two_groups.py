from scipy.stats import f_oneway, kruskal
import pandas as pd
from functions.tests.helper import make_decision, create_contingency_table, is_sample_size_enough, normality_test, homogeneity_var_test, check_size
from functions.tests.independent_groups.two_groups import chi2_test


def chi2_or_chi2_yate_test(df: pd.DataFrame, variable1: str, variable2: str, alpha=0.05):
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
        print('Chi2 test with Yate\'s correction conducted...')
        p_value = chi2_test(tab, yate_corr=True)

    make_decision(p_value, alpha)


def anova_or_kruskalwallis_test(df: pd.DataFrame, continue_param: str, category_param: str, alpha=0.05) -> None:
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
        p_value = kruskal_wallis_test(groups, print_flag=False)
    elif normality_test(groups, alpha) and homogeneity_var_test(groups, alpha) and check_size(groups):
        print('ANOVA test conducted...')
        p_value = anova_test(groups)
    else:
        print('Kruskal-Wallis test conducted...')
        p_value = kruskal_wallis_test(groups, print_flag=False)

    make_decision(p_value, alpha)


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


def kruskal_wallis_test(groups: list[pd.Series], print_flag=True, alpha=0.05):
    """
    Conducts a Kruskal-Wallis test.

    Args:
    groups (list[pd.Series]): The list of groups to be tested for normality.
    print_flag (bool): If it is True the result could be printed.
    alpha (float): Level of confidence.

    Returns:
    None / float: p-value.
    """
    h, p_value = kruskal(*groups)
    print('H:', h)
    print('p-value:', p_value)
    if print_flag:
        make_decision(p_value, alpha)
        return
    return p_value
