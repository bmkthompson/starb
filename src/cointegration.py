import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

def engle_granger_test(series1, series2, significance=0.05):
    df = pd.concat([series1, series2], axis=1).dropna()
    y = df.iloc[:, 0]
    x = df.iloc[:, 1]

    x_with_const = sm.add_constant(x)
    model = sm.OLS(y, x_with_const).fit()
    beta = model.params[1]

    residuals = model.resid
    adf_result = adfuller(residuals)
    p_value = adf_result[1]
    is_cointegrated = p_value < significance

    return {
        'beta': beta,
        'ADF Statistic': adf_result[0],
        'p-value': p_value,
        'is_cointegrated': is_cointegrated
    }
