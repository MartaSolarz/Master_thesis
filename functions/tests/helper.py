from colorama import Fore, Style
from scipy.stats import shapiro, levene
import pandas as pd


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


def create_contingency_table(df: pd.DataFrame, column1: str, column2: str) -> pd.DataFrame:
    """
    Creates a contingency table based on two variables in the DataFrame.

    Args:
    df (DataFrame): The DataFrame containing the data.
    column1 (str): Name of the first column for the contingency table.
    column2 (str): Name of the second column for the contingency table.

    Returns:
    DataFrame: Contingency table based on the two variables.
    """
    return pd.crosstab(df[column1], df[column2])


def is_sample_size_enough(tab: pd.DataFrame, samples=5) -> bool:
    """
    Checks if each group in the contingency table has at least 5 samples.

    Args:
    tab (pd.DataFrame): The contingency table.
    samples (int): Number of minimum elements in each group.

    Returns:
    bool: True if each group has at least 5 samples, False otherwise.
    """
    for column in tab.columns:
        if any(tab[column] < samples):
            return False
    return True


def check_size(groups: list[pd.Series], min_size=20):
    """
    Checks if each group in the list has at least the minimum number of elements.

    Args:
    groups (list[pd.Series]): The list of groups to be checked.
    min_size (int): The minimum number of elements required for each group. Default is 20.

    Returns:
    bool: True if each group has at least the minimum number of elements, False otherwise.
    """
    return all(len(group) >= min_size for group in groups)


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


def make_decision(p_value: float, alpha=0.05):
    """
    Makes a decision based on the p-value and the significance level alpha.

    Args:
    p_value (float): The p-value from the statistical test.
    alpha (float): The significance level for the test.

    Returns:
    None
    """
    if p_value < alpha:
        print(f"{Fore.RED}There are grounds to reject H0, accept H1.{Style.RESET_ALL}")
    else:
        print('No reason to reject H0, accept H0.')