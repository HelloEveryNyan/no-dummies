import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = pd.unique(data['whoAmI'])
for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int)

data = data.drop('whoAmI', axis=1)
data.head()
