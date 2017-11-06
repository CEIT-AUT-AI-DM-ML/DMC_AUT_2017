import csv
import math
def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
with open('names3.csv', 'rb') as csvfile:
    with open ('c0.csv', 'w') as c0:
        with open ('c1.csv', 'w') as c1:
            with open ('c2.csv', 'w') as c2:
                with open ('c3.csv', 'w') as c3:
                    with open ('c4.csv', 'w') as c4:
                        with open ('c5.csv', 'w') as c5:
                            with open ('c6.csv', 'w') as c6:
                                with open ('c7.csv', 'w') as c7:
                                    with open ('c8.csv', 'w') as c8:

                                        ans = 0
                                        sum = 0.0
                                        sum2 = 0.0
                                        spamreader = csv.reader (csvfile, delimiter=',', quotechar='|')

                                        fieldnames = ['id', 'avg1', 'avg2', 'avg3', 'avg4', 'avg5']

                                        writer0 = csv.DictWriter (c0, fieldnames=fieldnames)
                                        writer1 = csv.DictWriter (c1, fieldnames=fieldnames)
                                        writer2 = csv.DictWriter (c2, fieldnames=fieldnames)
                                        writer3 = csv.DictWriter (c3, fieldnames=fieldnames)
                                        writer4 = csv.DictWriter (c4, fieldnames=fieldnames)
                                        writer5 = csv.DictWriter (c5, fieldnames=fieldnames)
                                        writer6 = csv.DictWriter (c6, fieldnames=fieldnames)
                                        writer7 = csv.DictWriter (c7, fieldnames=fieldnames)
                                        writer8 = csv.DictWriter (c8, fieldnames=fieldnames)


                                        writer0.writeheader ()
                                        writer1.writeheader ()
                                        writer2.writeheader ()
                                        writer3.writeheader ()
                                        writer4.writeheader ()
                                        writer5.writeheader ()
                                        writer6.writeheader ()
                                        writer7.writeheader ()
                                        writer8.writeheader ()


                                        cnt = 0
                                        print 'hey'
                                        check = []
                                        for l in range(9):
                                            check.append(0)

                                        for row in spamreader:

                                            if(RepresentsFloat(row[0])):

                                                # x = float(row[4]) #+ float(row[3]) + float(row[2]) +float(row[1])
                                                # x /= 4
                                                # t0 = (float (row[2]) - float (row[1]))
                                                # t1 = (float (row[3]) - float (row[2]))
                                                # t2 = (float (row[4]) - float (row[3]))
                                                # t3 = (float (row[5]) - float (row[4]))
                                                t0 = (float(row[3]) - float(row[2]))
                                                t1 = (float(row[4]) - float(row[3]))
                                                t2 = (float(row[5]) - float(row[4]))
                                                t3 = (float(row[5]) - float(row[4]))

                                                id = 0

                                                f = t1


                                                if t0>0:
                                                    t0 = 1
                                                    id += 1
                                                else:
                                                    t0 = 0

                                                if t1>0:
                                                    t1 = 1
                                                    id+= 2
                                                else:
                                                    t1 = 0

                                                if t2>0:
                                                    t2 = 1
                                                    id+=4
                                                else:
                                                    t2 = 0
                                                if (abs (f) < 100 or abs(t3)<100):
                                                    id = 8

                                                check[id] += 1

                                                # #t3 = (float(row[4]) - float(row[2]))/float(row[2])
                                                # #t4 = (float(row[6]) - float(row[4]))/float(row[4])
                                                # #t5 = (float(row[8]) - float(row[6]))/float
                                                if id == 0:
                                                    writer0.writerow ({'id': float(row[0]), 'avg1': float(row[1]),
                                                                      'avg2': float(row[2]),
                                                                      'avg3': float(row[3]),
                                                                      'avg4': float(row[4]),
                                                                      'avg5': float(row[5])
                                                                      })
                                                if id == 1:
                                                    writer1.writerow ({'id': float (row[0]), 'avg1': float (row[1]),
                                                                      'avg2': float (row[2]),
                                                                      'avg3': float (row[3]),
                                                                      'avg4': float (row[4]),
                                                                      'avg5': float (row[5])
                                                                      })
                                                if id == 2:
                                                    writer2.writerow ({'id': float (row[0]), 'avg1': float (row[1]),
                                                                      'avg2': float (row[2]),
                                                                      'avg3': float (row[3]),
                                                                      'avg4': float (row[4]),
                                                                      'avg5': float (row[5])
                                                                      })

                                                if id == 3:
                                                    writer3.writerow ({'id': float (row[0]), 'avg1': float (row[1]),
                                                                      'avg2': float (row[2]),
                                                                      'avg3': float (row[3]),
                                                                      'avg4': float (row[4]),
                                                                      'avg5': float (row[5])
                                                                      })

                                                if id == 4:
                                                    writer4.writerow ({'id': float (row[0]), 'avg1': float (row[1]),
                                                                      'avg2': float (row[2]),
                                                                      'avg3': float (row[3]),
                                                                      'avg4': float (row[4]),
                                                                      'avg5': float (row[5])
                                                                      })

                                                if id == 5:
                                                    writer5.writerow ({'id': float (row[0]), 'avg1': float (row[1]),
                                                                      'avg2': float (row[2]),
                                                                      'avg3': float (row[3]),
                                                                      'avg4': float (row[4]),
                                                                      'avg5': float (row[5])
                                                                      })

                                                if id == 6:
                                                    writer6.writerow (
                                                        {'id': float (row[0]), 'avg1': float (row[1]),
                                                         'avg2': float (row[2]),
                                                         'avg3': float (row[3]),
                                                         'avg4': float (row[4]),
                                                         'avg5': float (row[5])
                                                         })

                                                if id == 7:
                                                    writer7.writerow ({'id': float (row[0]), 'avg1': float (row[1]),
                                                                      'avg2': float (row[2]),
                                                                      'avg3': float (row[3]),
                                                                      'avg4': float (row[4]),
                                                                      'avg5': float (row[5])
                                                                      })

                                                if id == 8:
                                                    writer8.writerow ({'id': float (row[0]), 'avg1': float (row[1]),
                                                                       'avg2': float (row[2]),
                                                                       'avg3': float (row[3]),
                                                                       'avg4': float (row[4]),
                                                                       'avg5': float (row[5])
                                                                       })
                                                # y = x - float(row[5])
                                                # sum += pow(y , 2.0)
                                                # cnt += 1
                                        for l in range (8):
                                            print check[l]
                                        print check[8]