from scipy.stats import spearmanr, pearsonr, pointbiserialr
import pandas as pd
from functions.tests.helper import homogeneity_var_test, normality_test, make_decision
import pingouin as pg


def correlation_dependent_groups_test(df: pd.DataFrame, first_var: str, second_var: str, subject: str, alpha=0.05):
    """
    Perform a correlation test for dependent groups on the provided DataFrame.

    Args:
    df (pd.DataFrame): The input DataFrame containing the data for the correlation test.
    first_var (str): The name of the first variable column in the DataFrame.
    second_var (str): The name of the second variable column in the DataFrame.
    subject (str): The name of the column representing the subject identifier.
    alpha (float): The significance level for the test. Defaults to 0.05.

    Returns:
    None: The function prints the correlation test statistic value and the p-value, along with the decision based on the significance level.
    """
    result = pg.rm_corr(data=df, x=first_var, y=second_var, subject=subject)
    p_val = result['pval']
    stat = result['r']
    print('Correlation test statistic value:', stat)
    print('P-value:', p_val)
    make_decision(p_val, alpha)


def correlation_independent_groups_test(data1: pd.Series, data2: pd.Series, alpha=0.05, biserial=False):
    """
    Function to conduct correlation test.

    Args:
    data1 (pd.Series): First set of data.
    data2 (pd.Series): First set of data.
    alpha (float): Confidence level.

    Returns:
    None.
    """
    groups = [data1, data2]
    if normality_test(groups, alpha) and homogeneity_var_test(groups, alpha):
        if biserial:
            print('Conducting Point-biserial correlation test...')
            p_val = pointbiserial_corr(data1, data2)
        else:
            print('Conducting Pearson correlation test...')
            p_val = pearson_corr(data1, data2)
    else:
        print('Conducting Spearman correlation test...')
        p_val = spearman_corr(data1, data2)

    make_decision(p_val, alpha)
    return f"P-value: {p_val:.2f}"


def pearson_corr(data1: pd.Series, data2: pd.Series) -> float:
    """
    Function to conduct Pearson correlation test.

    Args:
    data1 (pd.Series): First set of data.
    data2 (pd.Series): First set of data.

    Returns:
    float: p-value.
    """
    pearson_corr, p_value = pearsonr(data1, data2)
    print('Pearson correlation test statistic value:', pearson_corr)
    print('P-value:', p_value)
    return p_value


def spearman_corr(data1: pd.Series, data2: pd.Series, print_flag=False, alpha=0.05):
    """
    Function to conduct Spearman correlation test.

    Args:
    data1 (pd.Series): First set of data.
    data2 (pd.Series): First set of data.
    print_flag (bool): If True, result will be printed.
    alpha (float): Level of confidence.

    Returns:
    float/None.
    """
    spearman_corr, p_value = spearmanr(data1, data2)
    print('Spearman correlation test statistic value:', spearman_corr)
    print('P-value:', p_value)
    if print_flag:
        make_decision(p_value, alpha)
        return f"P-value: {p_value:.2f}"
    return p_value


def pointbiserial_corr(data1: pd.Series, data2: pd.Series) -> float:
    """
    Function to conduct Pearson correlation test.

    Args:
    data1 (pd.Series): First set of data.
    data2 (pd.Series): First set of data.

    Returns:
    float: p-value.
    """
    corr, p_value = pointbiserialr(data1, data2)
    print('Point-biserial correlation test statistic value:', corr)
    print('P-value:', p_value)
    return p_value
