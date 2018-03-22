import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import copy


z=[[0, 6, 11], [18, 1, 22], [35, 25, 55], [18, 20, 0]]
y_label= ["Chem 1","Chem 2","Chem 3","Chemi 4"]

labels =  np.array(z)

a=copy.deepcopy(z)
z_text=copy.deepcopy(z)
print a
for i in range(len(z)):
    for j in range(len(z[i])):
        if (z[i][j] >= 20 and z[i][j] <= 30):
            z[i][j] = 1
        elif (z[i][j]) > 30:
            z[i][j] = 2
        elif (z[i][j]) < 20:
            z[i][j] = 0


df = pd.DataFrame(z, columns=["Region 1","Region 2","Region 3"])


cmap = mcolors.LinearSegmentedColormap.from_list("3",['#808080','#008000','#FF0000'])

fig = plt.figure(figsize=(14,6))
fig.add_subplot(1,1,1)
ax=sns.heatmap(df,yticklabels=y_label,cmap=cmap,annot=labels,annot_kws={"size": 15},cbar=False,fmt='')


ax.figure.savefig("heatmap.png")
