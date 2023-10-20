import statsmodels.api as sm
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def create_categorical_time_plot(df, categorical_column_name, name):
    """
    Create categorical time plot.
    """
    time_column_name = 'czas'
    categories = df[categorical_column_name].unique()

    plt.figure(figsize=(10, 6))
    for i, category in enumerate(categories):
        category_data = df[df[categorical_column_name] == category]
        plt.scatter(category_data[time_column_name], [i + 1] * len(category_data), label=category)

    plt.xlim([0, df[time_column_name].max()+10000])
    plt.yticks(range(1, len(categories) + 1), categories)
    plt.xlabel('czas [ms]')
    plt.ylabel(categorical_column_name)
    plt.title(f'{name} Rozkład czasu vs. {categorical_column_name}')
    plt.legend()
    plt.grid(True)
    plt.show()


def create_scatterWithregression_and_residuals_plots(df, continue_param, category_param, labelContinue, labelCategory):
    """
    Create scatter plot with linear regression and residuals plot.
    """
    X = sm.add_constant(df[continue_param])
    model = sm.OLS(df[category_param], X)
    results = model.fit()
    plt.scatter(df[continue_param], df[category_param])
    plt.plot(df[continue_param], results.fittedvalues, 'r')
    plt.xlabel(labelContinue)
    plt.ylabel(labelCategory)
    plt.title(f"{labelContinue} vs. {labelCategory}")
    plt.grid(True)
    plt.show()

    residuals = df[category_param] - results.fittedvalues
    plt.scatter(df[continue_param], residuals)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel(labelContinue)
    plt.ylabel('Reszty')
    plt.title('Wykres reszt')
    plt.grid(True)
    plt.show()


def create_scatter_logit_plot(df, col1, col2, label1, label2):
    """
    Create scatter plot.
    """
    if not ((0 <= df[col2]) & (df[col2] <= 1)).all():
        df[col2] = (df[col2] - np.min(df[col2])) / (np.max(df[col2]) - np.min(df[col2]))

    plt.scatter(df[col1], df[col2], label='Data Points')
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.title(f'{label1} vs. {label2}')

    logit_model = sm.Logit(df[col2], sm.add_constant(df[col1]))
    result = logit_model.fit(disp=0)
    x_values = np.linspace(np.min(df[col1]), np.max(df[col1]), 100)
    y_values = result.predict(sm.add_constant(x_values))
    plt.plot(x_values, y_values, color='r', label='Logistic Regression Curve')

    plt.legend()
    plt.grid(True)
    plt.show()


def create_roc_curve_and_residuals_plot(df, col1, col2, label1):
    """
    Create ROC curve plot and residuals plot.
    """

    if not ((0 <= df[col2]) & (df[col2] <= 1)).all():
        df[col2] = (df[col2] - np.min(df[col2])) / (np.max(df[col2]) - np.min(df[col2]))

    logit_model = sm.Logit(df[col2], sm.add_constant(df[col1]))
    result = logit_model.fit(disp=0)
    y_pred = result.predict(sm.add_constant(df[col1]))
    fpr, tpr, _ = roc_curve(df[col2], y_pred)

    # Plot ROC curve
    plt.plot([0, 1], [0, 1], color='r', linestyle='--')
    plt.plot(fpr, tpr, marker='.')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Plot')
    plt.grid(True)
    plt.show()

    # Calculate residuals and plot
    y_pred_binary = (y_pred > 0.5).astype(int)
    residuals = df[col2] - y_pred_binary
    plt.scatter(df[col1], residuals)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel(label1)
    plt.ylabel('Residuals')
    plt.title('Residuals Plot')
    plt.grid(True)
    plt.show()


def create_conditional_effects_plot(df, col1, col2, label1, label2):
    """
    Create conditional effects plot.
    """
    sns.lmplot(x=col1, y=col2, data=df, logistic=True, y_jitter=.03)
    plt.title('Wykres warunkowych efektów')
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.grid(True)
    plt.show()
