import pandas as pd
from scipy import stats
import statsmodels.api as sm
from scipy.stats import shapiro, f_oneway, levene, kruskal
import numpy as np


def conduct_chi2test_for_many(dfs, alpha, names, dependent_variable, independent_variable):
    """
    Function to conduct chi2 test for many dataframes.
    """
    for i, df in enumerate(dfs):
        print('-----------------------------------------------')
        print(names[i + 1])
        conduct_chi2test(df, dependent_variable, independent_variable, alpha)


def conduct_chi2test(df, dependent_variable, independent_variable, alpha):
    """
    Function to conduct chi2 test.
    """
    tab = create_contingency_table_two_variables(df, dependent_variable, independent_variable)
    print(tab)
    chi2_stat, p_val, _, _ = stats.chi2_contingency(tab)
    print('Wartość statystyki chi-kwadrat:', chi2_stat)
    print('P-value:', p_val)
    make_decision(p_val, alpha)


def create_contingency_table_two_variables(df, col1, col2):
    return pd.crosstab(df[col1], df[col2])


def conduct_logistic_regression_test(df, dependent_var, independent_variables, alpha):
    """
    Function to conduct logistic regression test.
    """
    X = df[independent_variables]
    y = df[dependent_var]

    if not ((0 <= y) & (y <= 1)).all():
        y = (y - np.min(y)) / (np.max(y) - np.min(y))

    model = sm.Logit(y, X)
    result = model.fit()


    for indep_var in independent_variables:
        if indep_var == 'intercept':
            continue
        print(f'{indep_var.upper()}:')
        print('p-value:', result.pvalues[indep_var])
        make_decision(result.pvalues[indep_var], alpha)

    print(result.summary())


def conduct_posthoc_test(df, dependent_variable, independent_variable):
    """
    Conduct posthoc Tukey test.
    """
    posthoc = sm.stats.multicomp.MultiComparison(df[dependent_variable], df[independent_variable])
    result = posthoc.tukeyhsd()
    print(result)


def conduct_normality_test_for_many(dfs, names, continue_param, alpha):
    """
    Conduct test to check if the distribution is Gaussian for many dataframes.
    """
    for i, df in enumerate(dfs):
        print('-----------------------------------------------')
        print(names[i + 1])
        conduct_normality_test(df[continue_param], alpha)


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


def conduct_normality_test(col, alpha):
    """
    Conduct test to check if the distribution is Gaussian.
    """
    stats, p = shapiro(col)
    print('Stats:', stats)
    print('P-value:', p)
    if p > alpha:
        print('Dane mają rozkład normalny.')
    else:
        print('Rozkład jest różny od normalnego.')


def conduct_homogeneity_var_test(df, alpha, continue_param, category_param, is_single=False):
    """
    Conduct homogeneity variance test.
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    w, p_value = levene(*groups)
    print('W:', w)
    if is_single:
        print('p-value:', p_value)
        make_decision(p_value, alpha)
        return

    return p_value


def conduct_anova_test(df, alpha, continue_param, category_param):
    """
    Conduct ANOVA test.
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    f_value, p_value = f_oneway(*groups)
    print('F-value:', f_value)
    print('p-value:', p_value)
    make_decision(p_value, alpha)


def conduct_kruskal_wallis_test(df, alpha, continue_param, category_param):
    """
    Conduct Kruskal-Wallis test.
    """
    groups = [df[df[category_param] == i][continue_param] for i in df[category_param].unique()]
    h, p_value = kruskal(*groups)
    print('H:', h)
    print('p-value:', p_value)
    make_decision(p_value, alpha)


def make_decision(p_val, alpha):
    if p_val < alpha:
        print('Istnieją podstawy do odrzucenia H0, przyjmujemy hipotezę H1.')
    else:
        print('Brak podstaw do odrzucenia H0.')
