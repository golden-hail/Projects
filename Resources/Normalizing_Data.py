# Normalizing Data

from sklearn.preprocessing import MinMaxScaler

my_df = pd.DataFrame()
scale_norm = MinMaxScaler()
scale_norm.fit_transform(my_df)
scale_norm_normal = pd.DataFrame(scale_norm.fit_transform(my_df), columns = my_df.columns)
