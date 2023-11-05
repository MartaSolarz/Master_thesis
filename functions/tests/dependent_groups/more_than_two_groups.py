import pandas as pd
from functions.tests.helper import make_decision, homogeneity_var_test, normality_test
from scipy.stats import friedmanchisquare
from statsmodels.stats.anova import AnovaRM
from scikit_posthocs import posthoc_nemenyi_friedman


def anova_or_friedman_test(groups: list[pd.Series], alpha=0.05):
    """
    Function to determine whether to conduct an ANOVA or a Friedman test based on the results of the normality test and the homogeneity of variance test for the input data groups.

    Args:
    groups (list[pd.Series]): A list of pandas Series representing the different groups to be tested.
    alpha (float): The significance level for the tests. Defaults to 0.05.

    Returns:
    None: The function prints whether to conduct an ANOVA or a Friedman test based on the test results.
    """
    if normality_test(groups, alpha) and homogeneity_var_test(groups, alpha):
        print('Należy przeprowadzić test ANOVA.')
        return

    friedman_test(groups, print_flag=True, alpha=0.05)


def anova_test(df: pd.DataFrame, depvar: str, subject: str, within: str):
    """
    Perform a repeated measures ANOVA test on the provided DataFrame.

    Args:
    df (pd.DataFrame): The input DataFrame containing the data for the ANOVA test.
    depvar (str): The name of the dependent variable column in the DataFrame.
    subject (str): The name of the column representing the subject identifier.
    within (str): The name of the column representing the within-subject factor.

    Returns:
    None: The function prints the results of the repeated measures ANOVA test.
    """
    print(AnovaRM(data=df, depvar=depvar, subject=subject, within=[within]).fit())


def friedman_test(groups: list[pd.Series], print_flag=True, alpha=0.05):
    """
    Perform the Friedman test to compare multiple related samples.

    Parameters:
    groups (list[pd.Series]): A list of pandas Series or lists representing the related samples.
    print_flag (bool): If it is True the result could be printed.
    alpha (float): The significance level, often denoted as alpha, is the probability of rejecting the null hypothesis when it is true.

    Returns:
    None / float.
    """
    if len(groups) < 3:
        raise ValueError("Friedman test requires at least three groups.")

    data = pd.DataFrame(groups).T.values
    statistic, p_value = friedmanchisquare(*data)
    print('Friedman statistic:', statistic)
    print('p-value:', p_value)
    if print_flag:
        make_decision(p_value, alpha)
        if p_value < alpha:
            posthoc_results = posthoc_nemenyi_friedman(data)
            print(posthoc_results)
        return
    return p_value