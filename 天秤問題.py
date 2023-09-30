# [天秤問題](https://signate.jp/competitions/130)

# + active=""
# 学習用データ（train.tsv)、評価用データ（test.tsv）
# カラム	ヘッダ名称	データ型	説明
# 0	id	int	インデックスとして使用
# 1	class	int	天秤のバランス（0=左，1=平衡，2=右）
# 2	left_weight	int	左重量
# 3	left_distance	int	左距離
# 4	right_weight	int	右重量
# 5	right_distance	float	右距離

# +
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib as plt
import csv


df_test = pd.read_csv("天秤問題 csvファイル/test.tsv", sep = "\t")
df_train = pd.read_csv("天秤問題 csvファイル/train.tsv", sep = "\t")

df_train

df_train = df_train.drop(columns = ["Unnamed: 0"])

df_train


# -
df_train.describe()


df_train[df_train["class"] == 1]
#class列が1のものを取り出す

df_train["left_moment"] = df_train["left_weight"] * df_train["left_distance"] 
df_train["right_moment"] = df_train["right_weight"] * df_train["right_distance"]
#左回りのモーメントと右回りのモーメントのカラムを作成

df_train

df_train_moment = df_train.drop(columns=[col for col in df_train.columns if col not in ['class', 'left_moment', 'right_moment']])

df_train_moment

df_test = pd.read_csv("天秤問題 csvファイル/test.tsv", sep = "\t")

df_test

df_test["class"] = None

df_test["left_moment"] = df_test["left_weight"] * df_test["left_distance"]
df_test["right_moment"] = df_test["right_weight"] * df_test["right_distance"]

df_test["0"] = 

columns_to_keep = ["Unnamed: 0","class", "left_moment", "right_moment"]
df_test_moment = df_test[columns_to_keep]

df_test_moment


# +
# if df_test_moment["left_moment"] > df_test_moment["right_moment"]:
#     df_test_moment["class"] = 0
# elif df_test_moment["left_moment"] < df_test_moment["right_moment"]:
#     df_test_moment["class"] = 2
# elif df_test_moment["left_moment"] == df_test_moment["right_moment"]:
#     df_test_moment["class"] = 1

# +
def classify_moment(row):
    if row["left_moment"] > row["right_moment"]:
        return 0
    elif row["left_moment"] < row["right_moment"]:
        return 2
    elif row["left_moment"] == row["right_moment"]:
        return 1

df_test_moment.loc[:,"class"] = df_test_moment.apply(classify_moment, axis =1)
# -

df_test_moment["0"] = df_test_moment["Unnamed: 0"]

df_finish = df_test_moment.reindex(columns = ["0", "class"])

df_finish

df_finish["1"] = df_finish["class"]

df_finish

df_finish = df_finish.drop(columns = ["class"])

df_finish

df_finish.to_csv("submit2.csv", index = False)

df_finish.to_csv("submit.csv", header = None, index = None)




