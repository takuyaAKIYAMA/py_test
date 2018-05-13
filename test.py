'''
Created on 2018/02/17

@author: Takuya_AKIYAMA
'''
print("Hello Python!")

import numpy as np
import matplotlib.pyplot as plt
 
# 乱数を生成
x = np.random.rand(200)
y = np.random.rand(200)
 
# 散布図を描画
# plt.scatter(x, y)
# plt.show()

# plt.scatter(x, y, s=600, c="pink", alpha=0.5, linewidths="2",edgecolors="red")
# plt.show()

plt.scatter(x, y, s=600, c="yellow", marker="*", alpha=0.5, linewidths="2", edgecolors="orange")
plt.show()