#Read the file
import pandas as pd
df=pd.read_excel('D:\ITM\Udemy Data Science\DataScience\DataScience\multivariateregression_sampledata1.xlsx')
df.head()

#Create a multivariate model
#

import statsmodels.api as sm
X = df[['X3', 'X4', 'X5', 'X6', 'X7']]
y = df[['X1']]
xx1 = sm.add_constant(X)
est = sm.OLS(y, xx1).fit()
est.summary()

# The table of coefficients above gives us the values to plug into an equation of form:
#    B0 + B1 * X3 + B2 * X4 + B3 * X5+ B4 * X6+ B5 * X7
