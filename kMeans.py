import pandas as pd
import csv

import numpy as np
import matplotlib.pyplot as plt

def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


dataset_url = 'cluster.csv'
df = pd.read_csv(dataset_url, sep=',')

from sklearn.cluster import KMeans

for i in range(len(df)):
    df.t0[i] -= 8265.988163
    df.t0[i] /= 1095002955

    df.t1[i] -= 8265.988163
    df.t1[i] /= 1095002955

    df.t2[i] -= 8265.988163
    df.t2[i] /= 1095002955


n_clusters = 3
kmeans = KMeans(n_clusters)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_


with open ('g1.csv', 'w') as g1:
    with open ('g2.csv', 'w') as g2:
        with open ('g3.csv', 'w') as g3:
            with open ('g4.csv', 'w') as g4:
                with open ('names3.csv', 'rb') as csvfile:

                    spamreader = csv.reader (csvfile, delimiter=',', quotechar='|')

                    avg1 = []
                    avg2 = []
                    avg3 = []
                    avg4 = []
                    avg5 = []

                    for row in spamreader:
                        if RepresentsFloat(row[1]):
                            #print row[5]
                            avg1.append(float(row[1]))
                            avg2.append(float(row[2]))
                            avg3.append(float(row[3]))
                            avg4.append(float(row[4]))
                            avg5.append(float(row[5]))

                    fieldnames1 = ['avg1', 'avg2', 'avg3', 'avg4', 'avg5']
                    writer1 = csv.DictWriter (g1, fieldnames=fieldnames1)
                    writer1.writeheader ()

                    writer2 = csv.DictWriter (g2, fieldnames=fieldnames1)
                    writer2.writeheader ()

                    writer3 = csv.DictWriter (g3, fieldnames=fieldnames1)
                    writer3.writeheader ()

                    writer4 = csv.DictWriter (g4, fieldnames=fieldnames1)
                    writer4.writeheader ()
                    # c0 = 0
                    # c1 = 0
                    # c2 = 0
                    # c3 = 0


                    c = []
                    id = 0
                    check = []
                    for l in range(7):
                        check.append(0)

                    for i in range(n_clusters):
                        c.append(0)

                    for i in range( len(labels)) :

                        id = 0
                        if df.t0[i]==1:
                            id += 1

                        if df.t1[i]==1:
                            id += 2

                        if df.t2[i]==1:
                            id += 4

                        check[id] += 1

                        c[labels[i]] += 1
                        # if(labels[i] == 0):
                        #     writer1.writerow ({'avg1': avg1[i], 'avg2': avg2[i],
                        #                        'avg3': avg3[i], 'avg4': avg4[i], 'avg5': avg5[i]})
                        #
                        # if (labels[i] == 1):
                        #     writer2.writerow ({'avg1': avg1[i], 'avg2': avg2[i],
                        #                        'avg3': avg3[i], 'avg4': avg4[i], 'avg5': avg5[i]})
                        #
                        # if (labels[i] == 2):
                        #     writer3.writerow ({'avg1': avg1[i], 'avg2': avg2[i],
                        #                        'avg3': avg3[i], 'avg4': avg4[i], 'avg5': avg5[i]})
                        #
                        # if (labels[i] == 3):
                        #     writer4.writerow ({'avg1': avg1[i], 'avg2': avg2[i],
                        #                        'avg3': avg3[i], 'avg4': avg4[i], 'avg5': avg5[i]})

                    for i in range(8):
                        print check[i]
