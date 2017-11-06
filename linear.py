

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

    data = []
    for i in range(8):
        url = 'c' + str(i)+'.csv'
        data.append(pd.read_csv(url, sep=','))#.drop('id', axis=1))


    #vars_data = pd.read_csv(vars_url, sep=',')#.drop('id', axis=1)#.drop('tavg5', axis=1).drop('tavg4', axis=1).drop('tavg3', axis=1).drop('tavg2', axis=1).drop('tavg1', axis=1)


# Use only one feature


# Split the data into training/testing sets
y = []
X = []

for i in range(8):
    y.append(data[i].avg5)
    X.append(data[i].drop('avg5' , axis=1).drop('id' , axis=1))

m = []
v = []

for i in range(8):
    m.append(X[i].mean().mean())
    v.append(X[i].max().max() - X[i].min().min())

    X[i] -= m[i]
    X[i] /= v[i]
    y[i] -= m[i]
    y[i] /= v[i]


# var_y = vars_data.vars5
# var_X = vars_data.drop('vars5' , axis=1)


# X_test = data.drop('avg1', axis = 1)
# var_X_test = vars_data.drop('vars1', axis=1)

# y = data.quality
# X = data.drop('quality', axis=1)
X_train = []
X_test = []
y_train = []
y_test = []

for i in range(8):
    X_traint, X_testt, y_traint, y_testt = train_test_split (X[i], y[i],
                                                         test_size=0.01,
                                                         random_state=123,
                                                         )
    X_train.append(X_traint)
    X_test.append(X_testt)
    y_train.append(y_traint)
    y_test.append(y_testt)




# Create linear regression object

regr = []

for i in range(8):

    regr.append(linear_model.LinearRegression())
    #var_regr = linear_model.LinearRegression()

#
# # Train the model using the training sets

for i in range(8):
    regr[i].fit (X_train[i], y_train[i])

# for i in range(8):
#
#     regr.append(joblib.load('linear_regressor'+str(i)+'.pkl'))
# var_regr2 = joblib.load('var_linear_regressor.pkl')


# Make predictions using the testing set

y_pred = []
for i in range(8):
    y_pred.append(regr[i].predict(X_test[i]))
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

for i in range(8):
    y_test[i] *= v[i]
    y_test[i] += m[i]
    y_pred[i] *= v[i]
    y_pred[i] += m[i]

    print math.sqrt(mean_squared_error(y_test[i], y_pred[i]))/m[i]
    joblib.dump (regr[i], 'linear_regressor'+str(i)+'.pkl')


#     with open ('out.csv', 'w') as cout:
#
#     fieldnames = ['customerId',
#                       'balanceAvg',
#                       'balanceStd'
#                       ]
#
#     writer = csv.DictWriter (cout, fieldnames=fieldnames)
#     writer.writeheader ()
# #
#     for i in range(len(y_pred)):
#         writer.writerow ({'customerId': i,
#                   'balanceAvg' : y_pred[i],
#                   'balanceStd': var_y_pred[i]
#                           })


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