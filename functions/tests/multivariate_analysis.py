import pandas as pd
from statsmodels.regression.mixed_linear_model import MixedLM
from statsmodels.stats.anova import AnovaRM
from functions.tests.helper import make_decision


def linear_mixed_effects(df: pd.DataFrame, formula: str, subject='ID', alpha=0.05, statistically_significant=[], flagPrint=False, flagPrintAll=False) -> list:
    """
    Performs linear mixed effects modeling on the provided data.

    Parameters:
    df (pd.DataFrame): DataFrame containing all the data.
    formula (str): Formula specifying the model structure.
    subject (str): Name of the column containing the identifier of the research subjects.
    alpha (float): Significance level.
    statistically_significant (list[str]): Aggregate statistically significant variables.
    flagPrint (bool): Decision about printing - True - possible to print, False - no printing at all.
    flagPrintAll (bool): If True - print all summaries, if False - print only statistically significant.

    Returns:
    list[str].

    """
    lenStarted = len(statistically_significant)
    md = MixedLM.from_formula(formula, data=df, groups=df[subject])
    mdf = md.fit()

    p_values = mdf.pvalues[1:-1]
    names = mdf.model.exog_names[1:]
    for i, p_val in enumerate(p_values):
        if p_val < alpha:
            if flagPrint:
                print('-------------------')
                print(f"Zmienna: {names[i]}, P-value: {p_val:.10f}")
                make_decision(p_val, alpha)
            flagPrintAll = True
            statistically_significant.append(f'{names[i]}')

    if flagPrintAll and flagPrint:
        print(mdf.summary())

    if lenStarted == len(statistically_significant):
        statistically_significant.append('')

    return statistically_significant


def anova(df: pd.DataFrame, depvar: str, groups: list, subject='ID', alpha=0.05):
    """
    Conducts an analysis of variance (ANOVA) for data with unequal group sizes.

    Parameters:
    df (pd.DataFrame): DataFrame containing all the data.
    depvar (str): Name of the column containing the dependent variable.
    groups (list): List of column names containing the independent variables within.
    subject (str): Name of the column containing the identifier of the research subjects.
    alpha (float): Significance level.

    Returns:
    None: Displays the ANOVA test results and the statistical decisions made.

    """
    aov = AnovaRM(depvar=depvar, within=groups, subject=subject, data=df)
    model = aov.fit()
    result = model.anova_table
    print(result)
    
    for i in range(len(result)):
        print('-------------------')
        p_val = result.iloc[i]['Pr > F']
        name = result.index[i]
        print(f"Zmienna: {name}, P-value: {p_val:.10f}")
        make_decision(p_val, alpha)
