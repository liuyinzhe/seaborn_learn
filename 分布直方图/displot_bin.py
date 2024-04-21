import  matplotlib.pyplot as plt
import  numpy  as np
import  seaborn as sns
import pandas as pd 

# tmp = [160,165,175,180,185,190,195,200]
# heights = np.array(tmp)
# hist,bins = np.histogram(heights,bins=100)#,range=(160,200))
# print(hist)
# print(bins)
# plt.hist(hist,bins)
# plt.title("Histogram of Heights")
# plt.xlabel("Height (cm)")
# plt.ylabel("Frequency")

# plt.show()

data_frame = pd.read_csv("input.txt",sep='\t')
print(data_frame)
# Seaborn系列(三)：分布统计绘图(distribution)
# https://blog.csdn.net/hustlei/article/details/123091236

sns.displot(data=data_frame,x='signal_strength',bins=1000,kde=True,hue='group')#,bins=8,#data_frame['signal_strength']
plt.xlim(0,400) # 限制x的值为[0,20]
plt.xlabel('base singal strength')
#plt.ylabel('Value')
# plt.show()

plt.savefig(fname='hist.png', dpi=300,bbox_inches='tight',pad_inches=0.1)

