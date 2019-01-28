import pandas as pd
import numpy as np

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


#Feature # 4: Embarked?
#Some data cleaning required as many datapoints are missing
for data in all_data:
    data['Embarked'] = data['Embarked'].fillna('S')
print(train_data[['Embarked', 'Survived']].groupby(['Embarked'], as_index=False).mean())


#Feature # 5: Fare?
#We have to take the mean of missing datapoints
for data in all_data:
    data['Fare'] = data['Fare'].fillna(data['Fare'].median())
train_data['category_fare'] = pd.qcut(train_data['Fare'], 4)
print(train_data[['category_fare', 'Survived']].groupby(['category_fare'], as_index=False).mean())


#Feature # 6: Age?
for data in all_data:
    age_avg = data['Age'].mean()
    age_std = data['Age'].std()
    age_null = data['Age'].isnull().sum()

    random_list = np.random.randint(age_avg - age_std, age_avg + age_std, size = age_null)
    data['Age'][np.isnan(data['Age'])] = random_list
    data['Age'] = data['Age'].astype(int)

train_data['category_age'] = pd.qcut(train_data['Age'], 5)
print(train_data[['category_age', 'Survived']].groupby(['category_age'], as_index=False).mean())


#Feature # 7: Name?
def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\. ', name)
    if title_search:
        return title_search.group(1)
    return ""

for data in all_data:
    data['title'] = data['Name'].apply(get_title)

for data in all_data:
    data['title'] = data['title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'],'Rare')
    data['title'] = data['title'].replace('Mlle','Miss')
    data['title'] = data['title'].replace('Ms','Miss')
    data['title'] = data['title'].replace('Mme','Mrs')

print(pd.crosstab(train_data['title'], train_data['Sex']))
print("---------------")
print(train_data[['title', 'Survived']].groupby(['title']), as_index=False).mean()





