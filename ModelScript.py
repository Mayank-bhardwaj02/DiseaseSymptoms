import numpy as np
import pandas as pd

df1 = pd.read_csv('part1.csv')
df2 = pd.read_csv('part2.csv')

# Concatenating both CSV files
df = pd.concat([df1, df2], ignore_index=True)

mapping_dict = {'Yes': 1, 'No': 0}

df.replace(mapping_dict, inplace=True)

def replace_all_with_range(value):
    if value == "All":
        return "0-100"
    return value

df['Age'] = df['Age'].apply(replace_all_with_range)
df['Weight'] = df['Weight'].apply(replace_all_with_range)

def midpoint_of_range(range_string):
    lower, upper = map(int, range_string.split('-'))
    return (lower + upper) / 2
df['Heart Rate'] = df['Heart Rate'].apply(midpoint_of_range)
df['Age'] = df['Age'].apply(midpoint_of_range)
df['Weight'] = df['Weight'].apply(midpoint_of_range)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Disease_Encoded']= le.fit_transform(df['Disease'])
df = df.drop('Disease', axis=1)

x = df.drop(['Disease_Encoded','Possibility'], axis=1)
y = df['Disease_Encoded']

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42 )
rf.fit(x, y)

def prediction(data):
    prediction = rf.predict(data)
    predicted_disease = le.inverse_transform(prediction)
    return predicted_disease[0]

