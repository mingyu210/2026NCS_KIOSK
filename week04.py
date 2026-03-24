import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
print(mpg.info())
# inplace= True  -> 원본을 바꿔라
# mpg.dropna(subset=['horsepower'], inplace=True) 원본 업데이트
mpg_lcean = mpg.dropna(subset=['horsepower']) # 사본 생성
print(mpg_lcean.info())