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



