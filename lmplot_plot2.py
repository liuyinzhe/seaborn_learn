import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gzip
import re,os


stat_df = pd.read_csv('rebuild.txt',sep='\t',compression='infer',on_bad_lines='warn',header=None)
stat_df.columns = ['type','sum_len','count','read_len']

g=sns.lmplot(x="read_len", y="count", hue="var_type",col="var_type", data=stat_df)
# 获得被封起来的matplotlib  figure
figure=g.figure.get_figure()
# 居然bottom 位置能正常画，top都不行
figure.suptitle("Big Suptitle",verticalalignment='bottom')
figure.savefig(fname='lmplot_plot2.png', dpi=300,bbox_inches='tight',pad_inches=0.1)
