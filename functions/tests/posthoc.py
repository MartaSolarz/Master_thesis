import pandas as pd
import statsmodels.api as sm
from scikit_posthocs import posthoc_nemenyi
from scipy.stats import rankdata


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


def posthocNemenyi_test(df: pd.DataFrame, dependent_variable: str, independent_variable: str) -> None:
    """
    Conducts a posthoc Nemenyi test for non-parametric data sets.

    Args:
    df (DataFrame): The DataFrame containing the data.
    dependent_variable (str): The name of the dependent variable.
    independent_variable (str): The name of the independent variable.

    Returns:
    None
    """
    groups = [df[df[independent_variable] == i][dependent_variable] for i in df[independent_variable].unique()]
    ranks = [rankdata(group) for group in groups]
    nemenyi_result = posthoc_nemenyi(ranks)
    print(nemenyi_result)