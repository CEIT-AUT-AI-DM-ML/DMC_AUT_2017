import csv

import math


def RepresentsFloat(s):
     try:
        float(s)
        return True
     except ValueError:
        return False
with open('names3.csv', 'rb') as csvfile:
 with open ('cluster.csv', 'w') as cluster:

        sum = 0.0
        sum2 = 0.0
        spamreader = csv.reader (csvfile, delimiter=',', quotechar='|')

        fieldnames = ['t0', 't1', 't2']

        writer = csv.DictWriter (cluster, fieldnames=fieldnames)
        writer.writeheader ()

        for row in spamreader:

            if(RepresentsFloat(row[9])):
                t0 = (float(row[3]) - float(row[1]))/float(row[1])
                t1 = (float(row[5]) - float(row[3]))/float(row[3])
                t2 = (float(row[7]) - float(row[5]))/float(row[5])
                #t3 = (float(row[4]) - float(row[2]))/float(row[2])
                #t4 = (float(row[6]) - float(row[4]))/float(row[4])
                #t5 = (float(row[8]) - float(row[6]))/float(row[6])
                writer.writerow ({'t0': t0, 't1':t1, 't2':t2})

            else:
                print(row[9])
        print(sum / 200)
