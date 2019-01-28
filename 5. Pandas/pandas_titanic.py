import pandas as pd

#Training (891 entries) and Testing (417 entries)
train_data = pd.read_csv('titanic/train.csv')
test_data = pd.read_csv('titanic/test.csv')
all_data = [train_data, test_data]
passenger_id = test_data['PassengerId']

#Feature # 1: Pclass
print(train_data[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean())

#Feature # 2: Sex
print(train_data[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean())

#Feature # 3: Family size
for data in all_data:
    data['family_size'] = data['SibSp'] + data['Parch'] + 1
print(train_data[['family_size', 'Survived']].groupby(['family_size'], as_index=False).mean())


#Feature # 3.1: Is alone?
for data in all_data:
    data['is_alone'] = 0
    data.loc[data['family_size'] == 1, 'is_alone'] = 1
print(train_data[['is_alone', 'Survived']].groupby(['is_alone'], as_index=False).mean())
