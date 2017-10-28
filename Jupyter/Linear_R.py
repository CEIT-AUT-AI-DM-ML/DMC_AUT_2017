
# coding: utf-8

# In[2]:




import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import  math
import csv
from sklearn.externals import joblib



# Load the diabetes dataset

dataset_url = 'names3.csv'
vars_url = 'vars.csv'

if __name__ == '__main__':


    data = pd.read_csv(dataset_url, sep=',').drop('id', axis=1)
    vars_data = pd.read_csv(vars_url, sep=',').drop('id', axis=1)#.drop('tavg5', axis=1).drop('tavg4', axis=1).drop('tavg3', axis=1).drop('tavg2', axis=1).drop('tavg1', axis=1)


# Use only one feature


# Split the data into training/testing sets
y = data.avg5
X = data.drop('avg5' , axis=1)

var_y = vars_data.vars5
var_X = vars_data.drop('vars5' , axis=1)

X_test = data.drop('avg1', axis = 1)
var_X_test = vars_data.drop('vars1', axis=1)


# y = data.quality
# X = data.drop('quality', axis=1)
# X_train, X_test, y_train, y_test = train_test_split(X, y,
#                                                     test_size=0.01,
#                                                     random_state=123,
#                                                     )
#
# var_X_train, var_X_test, var_y_train, var_y_test = train_test_split(var_X, var_y,
#                                                     test_size=0.01,
#                                                     random_state=123,
#                                                     )



# Create linear regression object
regr = linear_model.LinearRegression()
var_regr = linear_model.LinearRegression()

#
# # Train the model using the training sets
# regr.fit(X_train, y_train)
# var_regr.fit(var_X_train, var_y_train)


regr2 = joblib.load('linear_regressor.pkl')
var_regr2 = joblib.load('var_linear_regressor.pkl')


# Make predictions using the testing set
y_pred = regr2.predict(X_test)
var_y_pred = var_regr2.predict(var_X_test)


# The coefficients
# print('Coefficients: \n', regr.coef_)
# # The mean squared error
# print("Mean squared error: %.2f"
#       % mean_squared_error(y_test, diabetes_y_pred))
# # Explained variance score: 1 is perfect prediction
# print('Variance score: %.2f' % r2_score(y_test, diabetes_y_pred))

with open ('out.csv', 'w') as cout:
    fieldnames = ['customerId',
                  'balanceAvg',
                  'balanceStd'
                  ]

    writer = csv.DictWriter (cout, fieldnames=fieldnames)
    writer.writeheader ()
#
    for i in range(len(y_pred)):
        writer.writerow ({'customerId': i,
                  'balanceAvg' : y_pred[i],
                  'balanceStd': var_y_pred[i]
                          })

# print math.sqrt(mean_squared_error(y_test, y_pred))
# print math.sqrt (mean_squared_error (var_y_test, var_y_pred))

# joblib.dump (regr, 'linear_regressor.pkl')
# joblib.dump (var_regr, 'var_linear_regressor.pkl')

    # Plot outputs
    #plt.scatter(X_test., y_test,  color='black')
    #plt.plot(X_test, diabetes_y_pred, color='blue', linewidth=3)

    #plt.xticks(())
    #plt.yticks(())


    #plt.show()

