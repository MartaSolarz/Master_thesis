import pandas as pd
from scipy.stats import fisher_exact, chi2_contingency, spearmanr

from functions.tests.helper import make_decision


def two_categorical_variable_test(df: pd.DataFrame, variable1: str, variable2: str, alpha=0.05):
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
    print('Chi2 test conducted...')
    p_value = chi2_test(tab)
    # if is_sample_size_enough(tab):
    #     print('Chi2 test conducted...')
    #     p_value = chi2_test(tab)
    # else:
    #     print('Spearman correlation test conducted...')
    #     p_value = spearman_test(df[dependent_variable], df[independent_variable])

    make_decision(p_value, alpha)


# def chi2_test(data: pd.DataFrame) -> float:
#     """
#     Function to conduct chi-squared test.
#
#     Args:
#     data (DataFrame): The contingency table.
#
#     Returns:
#     float: p-value.
#     """
#     chi2_stat, p_value, _, _ = chi2_contingency(data)
#     print('Chi-squared test statistic value:', chi2_stat)
#     print('P-value:', p_value)
#     return p_value




# def create_contingency_table(df: pd.DataFrame, column1: str, column2: str) -> pd.DataFrame:
#     """
#     Creates a contingency table based on two variables in the DataFrame.
#
#     Args:
#     df (DataFrame): The DataFrame containing the data.
#     column1 (str): Name of the first column for the contingency table.
#     column2 (str): Name of the second column for the contingency table.
#
#     Returns:
#     DataFrame: Contingency table based on the two variables.
#     """
#     return pd.crosstab(df[column1], df[column2])


# def is_sample_size_enough(tab: pd.DataFrame, samples=5) -> bool:
#     """
#     Checks if each group in the contingency table has at least 5 samples.
#
#     Args:
#     tab (pd.DataFrame): The contingency table.
#     samples (int): Number of minimum elements in each group.
#
#     Returns:
#     bool: True if each group has at least 5 samples, False otherwise.
#     """
#     for column in tab.columns:
#         if any(tab[column] < samples):
#             return False
#     return True

