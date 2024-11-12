import pandas as pd
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("data/Housing.csv")

binary_columns = ['mainroad', 'guestroom', 'basement',
                  'hotwaterheating', 'airconditioning', 'prefarea']

for col in binary_columns:
    dataset[col] = dataset[col].apply(lambda x: 0 if x == 'no' else 1)

furnishing_matrix = {
    "furnished": 2,
    "semi-furnished": 1,
    "unfurnished": 0
}

dataset['furnishingstatus'] = dataset['furnishingstatus'].apply(
    lambda x: furnishing_matrix[x])

scaler = StandardScaler()
dataset.iloc[:, 0:3] = scaler.fit_transform(dataset.iloc[:, 0:3])


x = dataset.iloc[0:, 1:]
y = dataset['price'][:10]

print(x)
