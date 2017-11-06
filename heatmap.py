import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame
import seaborn as sns

dataset_url = 'c1.csv'
data2 = pd.read_csv (dataset_url, sep=',')

data = data2.sample(10)

y = data.drop('id', axis=1)
x = data.id

# Index= ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# Cols = ['A', 'B', 'C', 'D']
df = data.drop('id', axis=1)

# plt.pcolor(df)
# plt.yticks(np.arange(0.5, len(df.index), 1), df.drop('id', axis = 1))
# plt.xticks(np.arange(0.5, len(df.columns), 1), df.id)
# plt.show()

# plt.pcolor(df)
# plt.yticks(np.arange(0.5, 5, 1), df.drop('id', axis = 1))
# plt.xticks(np.arange(0.5, len(df.id), 1), df.id)
# plt.show()

for i in range(len(df)):
    df.avg1.values[i] -= 8265.988163
    df.avg1.values[i] /= 1095002955

    df.avg2.values[i] -= 8265.988163
    df.avg2.values[i] /= 1095002955

    df.avg3.values[i] -= 8265.988163
    df.avg3.values[i] /= 1095002955

    df.avg4.values[i] -= 8265.988163
    df.avg4.values[i] /= 1095002955

    df.avg5.values[i] -= 8265.988163
    df.avg5.values[i] /= 1095002955


g = sns.heatmap(df, annot=True)
#g.invert_yaxis()
plt.show()
