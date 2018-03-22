import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
sns.set()

#I have given the data for four heatmaps. This is dummy input
x1=[[0, 0,5], [18, 1,20], [1, 0,13]]
x2=[[0, 0,8], [1, 1,9], [1, 0,20]]
x3=[[12, 0,8], [14, 1,9], [1, 10,20]]
x4=[[5, 0,8], [2, 1,9], [1, 6,20]]
y_label= ["a","b","c"]
df1 = pd.DataFrame(x1, columns=["A","B","C"])
df2 = pd.DataFrame(x2, columns=["A","B","C"])
df3 = pd.DataFrame(x3, columns=["A","B","C"])
df4 = pd.DataFrame(x4, columns=["A","B","C"])

frames = [df1,df2,df3,df4]

cmap = mcolors.LinearSegmentedColormap.from_list("5",['#ffffe0','#FFFF00','#FFA500','#FF0000','#800000'])
 
fig,axn = plt.subplots(2, 2, sharex=True, sharey=True,figsize=(18,8))
cbar_ax = fig.add_axes([.91, .3, .02, .4])
for i,ax in enumerate(axn.flat):
    ims = sns.heatmap(frames[i], ax=ax , yticklabels=y_label,cmap=cmap,cbar=False,vmin=0,vmax=20)
    



cbar = ims.figure.colorbar(ims.collections[0],cax=cbar_ax)
cbar.set_ticks([0, 5, 10,15, 20])
cbar.set_ticklabels(['10', '100', '1000', '10000','100000'])
cbar.set_label('Concentration')



ax.figure.savefig("heatmap.png")
