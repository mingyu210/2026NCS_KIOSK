import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
group_mpg = pd.DataFrame(mpg.groupby(by = 'origin'))
print(group_mpg)
print(mpg['origin'].nunique())
print(mpg.describe())
