

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import  math
import csv
from sklearn.externals import joblib



# Load the diabetes dataset

if __name__ == '__main__':

    vars_url = 'vars.csv'
    vars_data = pd.read_csv(vars_url, sep=',').drop('id', axis=1)#.drop('tavg5', axis=1).drop('tavg4', axis=1).drop('tavg3', axis=1).drop('tavg2', axis=1).drop('tavg1', axis=1)


# Use only one feature


# Split the data into training/testing sets

var_y = vars_data.vars5
var_X = vars_data.drop('vars5' , axis=1)

m = var_X.mean().mean()
v = var_X.max().max() - var_X.min().min()

var_y = (var_y - m)/v
var_X = (var_X - m)/v

# X_test = data.drop('avg1', axis = 1)
# var_X_test = vars_data.drop('vars1', axis=1)

# y = data.quality
# X = data.drop('quality', axis=1)

X_train, X_test, y_train, y_test = train_test_split (var_X, var_y,
                                                         test_size=0.01,
                                                         random_state=123,
                                                         )





# Create linear regression object

regr = linear_model.LinearRegression()
    #var_regr = linear_model.LinearRegression()

#
# # Train the model using the training sets

regr.fit (X_train, y_train)

# for i in range(8):
#
#     regr.append(joblib.load('linear_regressor'+str(i)+'.pkl'))
# var_regr2 = joblib.load('var_linear_regressor.pkl')


# Make predictions using the testing set

y_pred = regr.predict(X_test)

    # p = (data[i].drop('id',axis = 1).drop('avg1',axis = 1) - m[i])/v[i]
    # y_pred.append(regr[i].predict(p))

# var_y_pred = var_regr.predict(var_X_test)


# The coefficients
# print('Coefficients: \n', regr.coef_)
# # The mean squared error
# print("Mean squared error: %.2f"
#       % mean_squared_error(y_test, diabetes_y_pred))
# # Explained variance score: 1 is perfect prediction
# print('Variance score: %.2f' % r2_score(y_test, diabetes_y_pred))



# for i in range(len(y_pred)):
#     y_pred[i] *= 757897779.5
#     y_pred[i] += 174699.2248
#     print i, y_pred[i]


# print math.sqrt(mean_squared_error(y_test, y_pred))
# print math.sqrt (mean_squared_error (var_y_test, var_y_pred))

y_pred = X_test.vars4

y_test = y_test* v + m
y_pred = y_pred*v + m

print math.sqrt(mean_squared_error(y_test, y_pred))/m
joblib.dump (regr, 'var.pkl')




# for i in range(len(var_y_pred)):
#     print var_y_pred[i]

#joblib.dump (regr, 'linear_regressor.pkl')
# joblib.dump (var_regr, 'var_linear_regressor.pkl')

    # Plot outputs
# plt.scatter(X_test, y_test,  color='black')
# plt.plot(X_test, y_pred, color='blue', linewidth=3)
#
#     #plt.xticks(())
#     #plt.yticks(())
#
#
# plt.show()