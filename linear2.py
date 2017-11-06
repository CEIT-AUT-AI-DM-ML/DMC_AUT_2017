

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
    for i in range(9):
        url = 'c' + str(i)+'.csv'
        data.append(pd.read_csv(url, sep=','))#.drop('id', axis=1))

    v_data = pd.read_csv('vars.csv', sep=',')


    #vars_data = pd.read_csv(vars_url, sep=',')#.drop('id', axis=1)#.drop('tavg5', axis=1).drop('tavg4', axis=1).drop('tavg3', axis=1).drop('tavg2', axis=1).drop('tavg1', axis=1)


# Use only one feature


# Split the data into training/testing sets
X = []

for i in range(8):
    X.append(data[i].drop('avg1' , axis=1).drop('id' , axis=1))

v_X = v_data.drop('vars1', axis = 1).drop('id', axis = 1)

m = []
v = []
mini = []

vm = v_X.mean().mean()
vv = v_X.max().max() - v_X.min().min()

for i in range(8):
    m.append(data[i].drop('id',axis=1).drop('avg5',axis=1).mean().mean())
    v.append(data[i].drop('id',axis=1).drop('avg5',axis=1).max().max() - data[i].drop('id',axis=1).drop('avg5',axis=1).min().min())
    mini.append(X[i].min().min())
    # X[i] -= m[i]
    # X[i] /= v[i]
    # y[i] -= m[i]
    # y[i] /= v[i]


# Create linear regression object

regr = []
vreg = joblib.load('var.pkl')

for i in range(8):

    regr.append(joblib.load('linear_regressor'+str(i)+'.pkl'))


# Make predictions using the testing set
vp = (v_data.drop('id',axis = 1).drop('vars1',axis = 1) - vm) /vv
v_y_pred = vreg.predict(vp)

y_pred = []
for i in range(8):
    #y_pred.append(regr[i].predict(X_test[i]))
    p = (data[i].drop('id',axis = 1).drop('avg1',axis = 1) - m[i])/v[i]
    y_pred.append(regr[i].predict(p))

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
    # y_test[i] *= v[i]
    # y_test[i] += m[i]
    y_pred[i] *= v[i]
    y_pred[i] += m[i]

v_y_pred =( v_y_pred * vv )+ vm

with open ('out.csv', 'w') as cout:
    with open ('v_out.csv', 'w') as vout:
        with open ('avg_out.csv', 'w') as aout:

            fieldnames3 = ['id',
                          'avg1',
                          'avg2','avg3','avg4','avg5','avg6'
                          ]
            fieldnames = ['id',
                          'balanceAvg',
                          'balanceStd'
                          ]

            fieldnames2 = ['id',
                          'v1','v2','v3','v4','v5','v6'
                          ]
            writer = csv.DictWriter (cout, fieldnames=fieldnames)
            writer.writeheader ()

            writer2 = csv.DictWriter (vout, fieldnames=fieldnames2)
            writer2.writeheader ()

            writer3 = csv.DictWriter (aout, fieldnames=fieldnames3)
            writer3.writeheader ()
            z = 0
            vz = 0
            for i in range(8):

                for j in range (len(y_pred[i])):
                    #print data[i].id[j]
                    p = y_pred[i][j]
                    if(p<0):
                        p = mini[i]
                        z += 1
                    writer3.writerow ({'id': data[i].id[j],
                                      'avg1': data[i].avg1[j],
                                      'avg2': data[i].avg2[j],
                                      'avg3': data[i].avg3[j],
                                      'avg4': data[i].avg4[j],
                                      'avg5': data[i].avg5[j],
                                      'avg6': p
                                      })


                for j in range (len (y_pred[i])):
                    # print data[i].id[j]
                    p = y_pred[i][j]
                    if (p < 0):
                        p = mini[i]
                        z += 1
                    x = data[i].id[j]

                    if(v_y_pred[int(x)]<0):
                        vz += 1
                    writer.writerow ({'id': data[i].id[j],
                                      'balanceAvg': p,
                                      'balanceStd': v_data.vars5[x]
                                      })

                    writer2.writerow ({'id': data[i].id[j],
                                      'v1': v_data.vars1[x],
                                       'v2': v_data.vars2[x],
                                       'v3': v_data.vars3[x],
                                       'v4': v_data.vars4[x],
                                       'v5': v_data.vars5[x],
                                      'v6': v_data.vars5[x]
                                      })
            for j in range (len(data[8].id)):
                i = 8
                p = data[i].avg4[j] + data[i].avg5[j]
                p /= 2
                x = data[i].id[j]

                writer.writerow ({'id': data[i].id[j],
                                  'balanceAvg': p,
                                  'balanceStd': v_data.vars5[x]
                                  })

            for j in range (len (data[8].id)):
                i = 8
                p = data[i].avg4[j] + data[i].avg5[j]
                p /= 2
                writer3.writerow ({'id': data[8].id[j],
                                  'avg1': data[i].avg1[j],
                                  'avg2': data[i].avg2[j],
                                  'avg3': data[i].avg3[j],
                                  'avg4': data[i].avg4[j],
                                  'avg5': data[i].avg5[j],
                                  'avg6': p
                                  })
            # print z

            print z
            # print math.sqrt(mean_squared_error(y_test[i], y_pred[i]))/m[i]
            # joblib.dump (regr[i], 'linear_regressor'+str(i)+'.pkl')


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