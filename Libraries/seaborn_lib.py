"""
Seaborn builds on Matplotli with beautiful, high-level charts
"""

import seaborn as sns
import matplotlib as plt
import pandas as pd

tips = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()