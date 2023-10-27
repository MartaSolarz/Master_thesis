import numpy as np
from colorama import Fore, Style


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
        print(f"{Fore.RED}Istnieją podstawy do odrzucenia H0, przyjmujemy hipotezę H1.{Style.RESET_ALL}")
    else:
        print('Brak podstaw do odrzucenia H0.')