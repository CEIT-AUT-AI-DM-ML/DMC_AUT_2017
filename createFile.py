import csv
import random

def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
with open('month_1.csv', 'rb') as csvfile:
    with open ('month_2.csv', 'rb') as csvfile2:
        with open ('month_3.csv', 'rb') as csvfile3:
            with open ('month_4.csv', 'rb') as csvfile4:
                with open ('month_5.csv', 'rb') as csvfile5:

                    with open ('names3.csv', 'rb') as name:

                        with open ('vars.csv', 'rb') as vars:
                            with open ('normalnames.csv', 'w') as normal:

                                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                                reader2 = csv.reader(csvfile2, delimiter=',', quotechar='|')
                                reader3 = csv.reader(csvfile3, delimiter=',', quotechar='|')
                                reader4 = csv.reader(csvfile4, delimiter=',', quotechar='|')
                                reader5 = csv.reader(csvfile5, delimiter=',', quotechar='|')
                                nreader = csv.reader(name, delimiter=',', quotechar='|')

                                varreader = csv.reader(vars, delimiter=',', quotechar='|')


                                arr = []
                                ammount = []
                                transaction = []
                                vars1 = []

                                arr2 = []
                                ammount2 = []
                                transaction2 = []
                                vars2 = []


                                arr3 = []
                                ammount3 = []
                                transaction3 = []
                                vars3 = []


                                arr4 = []
                                ammount4 = []
                                transaction4 = []
                                vars4 = []


                                arr5 = []
                                ammount5 = []
                                transaction5 = []
                                vars5 = []


                                cnt1 = []
                                cnt2 = []
                                cnt3 = []
                                cnt4 = []
                                cnt5 = []

                                bid = []

                                avg1 = []
                                avg2 = []
                                avg3 = []
                                avg4 = []
                                avg5 = []


                                for k in range(400000):
                                    ammount.append(0.0)
                                    ammount2.append(0.0)
                                    ammount3.append(0.0)
                                    ammount4.append(0.0)
                                    ammount5.append(0.0)
                                    bid.append(0)
                                    cnt1.append(0)
                                    cnt2.append(0)
                                    cnt3.append(0)
                                    cnt4.append (0)
                                    cnt5.append (0)

                                    vars1.append(0)
                                    vars2.append(0)
                                    vars3.append(0)
                                    vars4.append(0)
                                    vars5.append(0)

                                    avg1.append(0)
                                    avg2.append(0)
                                    avg3.append(0)
                                    avg4.append(0)
                                    avg5.append(0)



                                fieldnames = ['id', 'navg1',
                                              'navg2',
                                              'navg3',
                                              'navg4',
                                              'navg5'
                                              ]
                                writer = csv.DictWriter (normal, fieldnames=fieldnames)
                                writer.writeheader()

                                for row in nreader:

                                    if(row[0] == 'id'):
                                        continue
                                    avg1[int(row[0])] = float(row[1]) - 178175.6318

                                    avg1[int(row[0])] /= 757897779.5


                                    avg2[int(row[0])] = (float(row[2]) - 178175.6318)/757897785.2


                                    avg3[int(row[0])] = (float(row[3]) - 178175.6318)/757897785.2


                                    avg4[int(row[0])] = (float(row[4]) - 178175.6318)/757897785.2


                                    avg5[int(row[0])] = (float(row[5]) - 178175.6318)/757897785.2


                                # for row in varreader:
                                #
                                #     if (row[0] == 'id'):
                                #         continue
                                #
                                #
                                #     avg1[int (row[0])] /= (float (row[1]) + 1)
                                #
                                #     avg2[int (row[0])] /= float (row[2])
                                #
                                #     avg3[int (row[0])] /= float (row[3])
                                #
                                #     avg4[int (row[0])] /= float (row[4])
                                #
                                #     avg5[int (row[0])] /= float (row[5])



                                # for row in spamreader:
                                #     s = row[0].split ('_')
                                #     if (s[len (s) - 1] == 'customerId'):
                                #         continue
                                #
                                #     id = (int(s[len (s) - 1]))
                                #
                                #     if(bid[id] == 0):
                                #
                                #         arr.append(int(s[len (s) - 1]))
                                #         bid[id] = 1
                                #
                                #
                                #     s2 = row[8].split(' ')
                                #     s3 = row[7].split(' ')
                                #     if(RepresentsFloat(s2[0])):
                                #         ammount[id] += (float(s2[0]))
                                #         vars1[id] += pow((float(s2[0]) - avg1[id]), 2)
                                #         cnt1[id] += 1
                                #
                                #     if (RepresentsFloat (s3[0])):
                                #         transaction.append (float (s3[0]))
                                #
                                #
                                # print 1
                                #
                                #
                                # for row in reader2:
                                #     s = row[0].split ('_')
                                #     if (s[len (s) - 1] == 'customerId'):
                                #         continue
                                #
                                #     arr2.append (int(s[len (s) - 1]))
                                #     id =  (int(s[len (s) - 1]))
                                #
                                #
                                #     s2 = row[8].split (' ')
                                #     s3 = row[7].split (' ')
                                #
                                #     if (RepresentsFloat (s2[0])):
                                #         ammount2[id] += (float (s2[0]))
                                #         vars2[id] += pow((float(s2[0]) - avg2[id]), 2)
                                #
                                #         cnt2[id] += 1
                                #
                                #     if (RepresentsFloat (s3[0])):
                                #         transaction2.append (float (s3[0]))
                                #
                                # print 2
                                #
                                # for row in reader3:
                                #     s = row[0].split ('_')
                                #     if (s[len (s) - 1] == 'customerId'):
                                #         continue
                                #
                                #     arr3.append (int(s[len (s) - 1]))
                                #     id = (int(s[len (s) - 1]))
                                #
                                #
                                #     s2 = row[8].split (' ')
                                #     s3 = row[7].split (' ')
                                #
                                #     if (RepresentsFloat (s2[0])):
                                #         ammount3[id] += (float (s2[0]))
                                #         vars3[id] += pow((float(s2[0]) - avg3[id]), 2)
                                #
                                #         cnt3[id] += 1
                                #
                                #     if (RepresentsFloat (s3[0])):
                                #         transaction3.append (float (s3[0]))
                                #
                                # print 3
                                #
                                # for row in reader4:
                                #     s = row[0].split ('_')
                                #     if (s[len (s) - 1] == 'customerId'):
                                #         continue
                                #
                                #     arr4.append (int(s[len (s) - 1]))
                                #     id = (int(s[len (s) - 1]))
                                #
                                #
                                #
                                #     s2 = row[8].split (' ')
                                #     s3 = row[7].split (' ')
                                #
                                #     if (RepresentsFloat (s2[0])):
                                #         ammount4[id] += (float (s2[0]))
                                #         vars4[id] += pow((float(s2[0]) - avg4[id]), 2)
                                #
                                #         cnt4[id] += 1
                                #
                                #     if (RepresentsFloat (s3[0])):
                                #         transaction4.append (float (s3[0]))
                                # print 4
                                #
                                # for row in reader5:
                                #     s = row[0].split ('_')
                                #     if (s[len (s) - 1] == 'customerId'):
                                #         continue
                                #
                                #     arr5.append (int(s[len (s) - 1]))
                                #     id =  (int(s[len (s) - 1]))
                                #
                                #
                                #     s2 = row[8].split (' ')
                                #     s3 = row[7].split (' ')
                                #
                                #     if (RepresentsFloat (s2[0])):
                                #         ammount5[id] += (float (s2[0]))
                                #         vars5[id] += pow((float(s2[0]) - avg5[id]), 2)
                                #
                                #         cnt5[id] += 1
                                #
                                #
                                #     if (RepresentsFloat (s3[0])):
                                #         transaction5.append (float (s3[0]))
                                #
                                # print 5
                                #
                                # # for x in range (1000):
                                # #     r = random.randint(0, len(arr))
                                # for r in range(len(arr)):
                                #
                                #     id = arr[r]
                                #
                                #     sum = 0
                                #     sum2 = 0
                                #     sum3 = 0
                                #     sum4 = 0
                                #     sum5 = 0
                                #
                                #     tsum = 0
                                #     tsum2 = 0
                                #     tsum3 = 0
                                #     tsum4 = 0
                                #     tsum5 = 0
                                #
                                #     ctr = 0
                                #     ctr2 = 0
                                #     ctr3 = 0
                                #     ctr4 = 0
                                #     ctr5 = 0
                                #     # for i in range(len(arr)):
                                #     #     if(arr[i] == id):
                                #     #         sum += ammount[i]
                                #     #         ctr += 1
                                #     #
                                #     #         tsum += transaction[i]
                                #     #
                                #     #
                                #     # for i in range(len(arr2)):
                                #     #     if(arr2[i] == id):
                                #     #         sum2 += ammount2[i]
                                #     #         ctr2 += 1
                                #     #
                                #     #         tsum2 += transaction2[i]
                                #     #
                                #     # for i in range (len (arr3)):
                                #     #     if (arr3[i] == id):
                                #     #         sum3 += ammount3[i]
                                #     #         ctr3 += 1
                                #     #
                                #     #         tsum3 += transaction3[i]
                                #     #
                                #     # for i in range (len (arr4)):
                                #     #     if (arr4[i] == id):
                                #     #         sum4 += ammount4[i]
                                #     #         ctr4 += 1
                                #     #
                                #     #         tsum4 += transaction4[i]
                                #     #
                                #     # for i in range (len (arr5)):
                                #     #     if (arr5[i] == id):
                                #     #         sum5 += ammount5[i]
                                #     #         ctr5 += 1
                                #     #         tsum5 += transaction5[i]
                                #
                                #     avg = []
                                #     vvars = []
                                #     for k in range(5):
                                #         avg.append(0)
                                #         vvars.append(0)
                                #
                                #
                                #     if(cnt1[id]>0):
                                #         vvars[0] = vars1[id]/cnt1[id]
                                #     else:
                                #         vvars[0]  = 0
                                #
                                #     if (cnt2[id] > 0):
                                #         vvars[1] = vars2[id] / cnt2[id]
                                #     else:
                                #         vvars[1] = vvars[0]
                                #
                                #     if (cnt3[id] > 0):
                                #         vvars[2] = vars3[id] / cnt3[id]
                                #     else:
                                #         vvars[2] = vvars[1]
                                #
                                #     if (cnt4[id] > 0):
                                #         vvars[3] = vars4[id] / cnt4[id]
                                #     else:
                                #         vvars[3] = vvars[2]
                                #
                                #     if (cnt5[id] > 0):
                                #         vvars[4] = vars5[id] / cnt5[id]
                                #     else:
                                #         vvars[4] = vvars[3]
                                for id in range(40000):
                                    writer.writerow ({'id': id, 'navg1': avg1[id],
                                                      'navg2': avg2[id],
                                                      'navg3': avg3[id],
                                                      'navg4': avg4[id],
                                                      'navg5': avg5[id]
                                                      })
                                    # writer.writerow({'id': id, 'avg1': (sum/ctr), 'tavg1':(tsum/ctr),
                                    #                   'avg2': (sum2/ctr2) ,'tavg2': (tsum2/ctr2),
                                    #                   'avg3': (sum3 / ctr3), 'tavg3': (tsum3 / ctr3),
                                    #                   'avg4': (sum4 / ctr4), 'tavg4': (tsum4 / ctr4),
                                    #                   'avg5': (sum5 / ctr5), 'tavg5': (tsum5 / ctr5),
                                    #                 })
