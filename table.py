import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import copy


z=[['','Y1','Y2'], ['A', 6, 11], ['B', 1, 22], ['C', 25, 55], ['D', 20, 0]]
y_label= ["Chem 1","Chem 2","Chem 3","Chemi 4"]

labels =  np.array(z)

a=copy.deepcopy(z)
z_text=copy.deepcopy(z)
print a
for i in range(len(z)):
    for j in range(len(z[i])):
        if (z[i][j] >= 20 and z[i][j] <= 30):
            z[i][j] = 2
        elif (z[i][j] > 30 and z[i][j] <= 64):
            z[i][j] = 3
        elif (z[i][j] < 20 and z[i][j] >= 0):
            z[i][j] = 1
        else:
            z[i][j] = 0

print z
df = pd.DataFrame(z, columns=["Region 1","Region 2","Region 3"])


cmap = mcolors.LinearSegmentedColormap.from_list("4",['#e5e5e5','#808080','#008000','#FF0000'])

fig = plt.figure(figsize=(14,6))
fig.add_subplot(1,1,1)
ax=sns.heatmap(df,yticklabels=False,xticklabels=False,cmap=cmap,annot=labels,annot_kws={"size": 15},cbar=False,fmt='',linewidths=1,linecolor='Black')

ax.set_title('TABLE',fontsize=30)
ax.figure.savefig("table.png")
