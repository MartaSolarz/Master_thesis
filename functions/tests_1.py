import pandas as pd
import statsmodels.api as sm
from scipy.stats import shapiro, f_oneway, levene, kruskal, ttest_ind, fisher_exact
import numpy as np
from colorama import Fore, Style
from scipy import stats
from scikit_posthocs import posthoc_nemenyi
from scipy.stats import rankdata





def normality_test(data: pd.Series) -> float:
    """
    Conducts a test to check if the distribution is Gaussian.

    Args:
    data (Series): The data to be tested for normality.
    alpha (float): The significance level for the test.

    Returns:
    float: p-value.
    """
    stats, p_value = shapiro(data)
    print('Stats:', stats)
    print('P-value:', p_value)
    return p_value


def homogeneity_var_test(df: pd.DataFrame, continue_param: str, category_param: str) -> float:
    """
    Conducts a homogeneity variance test.

    Args:
    df (DataFrame): The DataFrame containing the data.
    continue_param (str): The name of the continuous parameter.
    category_param (str): The name of the categorical parameter.

    Returns:
    float: p-value.
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    w, p_value = levene(*groups)
    print('W:', w)
    print('p-value:', p_value)

    return p_value


def equivalence_tstudent_test(data1: pd.Series, data2: pd.Series) -> bool:
    """
    Checks if two data sets are equivalence.

    Args:
    data1 (pd.Series): The first data.
    data2 (pd.Series): The second data.

    Returns:
    bool: True if one list is not more than twice as large as the other, False otherwise.
    """
    return not (len(data1) > 2 * len(data2) or len(data2) > 2 * len(data1))


def conduct_independent_t_test_from_df(df: pd.DataFrame, binary_column: str, numerical_column: str, alpha=0.05):
    """
    Conducts an independent t-test for two groups based on a binary column.

    Args:
    df (DataFrame): The DataFrame containing the data.
    binary_column (str): The name of the binary column.
    numerical_column (str): The name of the numerical column.
    alpha (float): The significance level for the test.

    Returns:
    None
    """
    data_group1 = df[df[binary_column] == 0][numerical_column]
    data_group2 = df[df[binary_column] == 1][numerical_column]
    t_stat, p_value = ttest_ind(data_group1, data_group2)
    print('T-statistic:', t_stat)
    print('p-value:', p_value)
    make_decision(p_value, alpha)


def anova_test(df: pd.DataFrame, continue_param, category_param, alpha=0.05) -> None:
    """
    Conducts an ANOVA test.

    Args:
    df (DataFrame): The DataFrame containing the data.
    continue_param (str): The name of the continuous parameter.
    category_param (str): The name of the categorical parameter.
    alpha (float): The significance level for the test.

    Returns:
    None
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    f_value, p_value = f_oneway(*groups)
    print('F-value:', f_value)
    print('p-value:', p_value)
    make_decision(p_value, alpha)


def kruskalWallis_test(df: pd.DataFrame, continue_param: str, category_param: str, alpha=0.05) -> None:
    """
    Conducts a Kruskal-Wallis test.

    Args:
    df (DataFrame): The DataFrame containing the data.
    continue_param (str): The name of the continuous parameter.
    category_param (str): The name of the categorical parameter.
    alpha (float): The significance level for the test.

    Returns:
    None
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    h, p_value = kruskal(*groups)
    print('H:', h)
    print('p-value:', p_value)
    make_decision(p_value, alpha)





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


def posthocNemenyi_test(data: list[pd.Series]) -> None:
    """
    Conducts a posthoc Nemenyi test for non-parametric data sets.

    Args:
    data (list[pd.Series]): The list of data for the test.

    Returns:
    None
    """
    ranks = [rankdata(group) for group in data]
    nemenyi_result = posthoc_nemenyi(ranks)
    print(nemenyi_result)

##################################
def conduct_chi2test_for_many(dfs, alpha, names, dependent_variable, independent_variable):
    """
    Function to conduct chi2 test for many dataframes.
    """
    for i, df in enumerate(dfs):
        print('-----------------------------------------------')
        print(names[i + 1])
        conduct_chi2test(df, dependent_variable, independent_variable, alpha)


# def conduct_chi2test(df, dependent_variable, independent_variable, alpha):
#     """
#     Function to conduct chi2 test.
#     """
#     tab = create_contingency_table_two_variables(df, dependent_variable, independent_variable)
#     print(tab)
#     chi2_stat, p_val, _, _ = stats.chi2_contingency(tab)
#     print('Wartość statystyki chi-kwadrat:', chi2_stat)
#     print('P-value:', p_val)
#     make_decision(p_val, alpha)


# def create_contingency_table_two_variables(df, col1, col2):
#     return pd.crosstab(df[col1], df[col2])


# def conduct_logistic_regression_test(df, dependent_var, independent_variables, alpha):
#     """
#     Function to conduct logistic regression test.
#     """
#     X = df[independent_variables]
#     y = df[dependent_var]
#
#     if not ((0 <= y) & (y <= 1)).all():
#         y = (y - np.min(y)) / (np.max(y) - np.min(y))
#
#     model = sm.Logit(y, X)
#     result = model.fit()
#
#
#     for indep_var in independent_variables:
#         if indep_var == 'intercept':
#             continue
#         print(f'{indep_var.upper()}:')
#         print('p-value:', result.pvalues[indep_var])
#         make_decision(result.pvalues[indep_var], alpha)
#
#     print(result.summary())


# def conduct_posthoc_test(df, dependent_variable, independent_variable):
#     """
#     Conduct posthoc Tukey test.
#     """
#     posthoc = sm.stats.multicomp.MultiComparison(df[dependent_variable], df[independent_variable])
#     result = posthoc.tukeyhsd()
#     print(result)


# def conduct_normality_test_for_many(dfs, names, continue_param, alpha):
#     """
#     Conduct test to check if the distribution is Gaussian for many dataframes.
#     """
#     for i, df in enumerate(dfs):
#         print('-----------------------------------------------')
#         print(names[i + 1])
#         conduct_normality_test(df[continue_param], alpha)


def conduct_test_for_gaussian_variables_for_many(dfs, names_gauss, dependent_var, independent_var, alpha):
    """
    For variables with Gaussian distribution.
    Check the homogeneity of variance and conduct right test: ANOVA or Kruskal-Wallis.
    """
    for i, df in enumerate(dfs):
        print('-----------------------------------------------')
        print(names_gauss[i + 1])
        p_val = conduct_homogeneity_var_test(df, alpha, dependent_var, independent_var)
        if p_val < alpha:
            print('Brak homogeniczności wariancji.')
            conduct_kruskal_wallis_test(df, alpha, dependent_var, independent_var)
        else:
            print('Homogeniczność wariancji zachowana.')
            conduct_anova_test(df, alpha, dependent_var, independent_var)


def conduct_test_for_no_gaussian_variables_for_many(dfs, names_nogauss, alpha, dependent_var, independent_var):
    """
    For variables without Gaussian distribution.
    Check the homogeneity of variance and conduct right test: ANOVA or Kruskal-Wallis.
    """
    for i, df in enumerate(dfs):
        print('-----------------------------------------------')
        print(names_nogauss[i + 1])
        conduct_kruskal_wallis_test(df, alpha, dependent_var, independent_var)


def test_based_on_normality(data1, data2, ALPHA):
    _, p_value_data1 = stats.normaltest(data1)
    _, p_value_data2 = stats.normaltest(data2)

    if p_value_data1 < ALPHA or p_value_data2 < ALPHA:
        statistic, p_value = stats.mannwhitneyu(data1, data2, alternative='two-sided')
        test_used = "U Manna-Whitneya"
    else:
        statistic, p_value = stats.ttest_ind(data1, data2)
        test_used = "t-Studenta"

    print("test_used", test_used,
         "statistic", statistic,
        "p_value", p_value
    )

    make_decision(p_value, ALPHA)

# def conduct_normality_test(col, alpha):
#     """
#     Conduct test to check if the distribution is Gaussian.
#     """
#     stats, p = shapiro(col)
#     print('Stats:', stats)
#     print('P-value:', p)
#     if p > alpha:
#         print('Dane mają rozkład normalny.')
#     else:
#         print('Rozkład jest różny od normalnego.')


# def conduct_homogeneity_var_test(df, alpha, continue_param, category_param, is_single=False):
#     """
#     Conduct homogeneity variance test.
#     """
#     groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
#     w, p_value = levene(*groups)
#     print('W:', w)
#     if is_single:
#         print('p-value:', p_value)
#         make_decision(p_value, alpha)
#         return
#
#     return p_value


# def conduct_anova_test(df, alpha, continue_param, category_param):
#     """
#     Conduct ANOVA test.
#     """
#     groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
#     f_value, p_value = f_oneway(*groups)
#     print('F-value:', f_value)
#     print('p-value:', p_value)
#     make_decision(p_value, alpha)


# def conduct_kruskal_wallis_test(df, alpha, continue_param, category_param):
#     """
#     Conduct Kruskal-Wallis test.
#     """
#     groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
#     h, p_value = kruskal(*groups)
#     print('H:', h)
#     print('p-value:', p_value)
#     make_decision(p_value, alpha)

