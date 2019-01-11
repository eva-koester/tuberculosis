import pandas as pd
import cleaning
import matplotlib.pyplot as plt
import seaborn as sns

df = cleaning.load_clean_data()
df['age'] = df['age'].replace([1], 14)
#print(df)

# sum of value per age
age = df.groupby('age')['value'].sum()
age=pd.DataFrame(age)
age=age.reset_index()
print(age)
print(age.info())

# sum of value per gender and age
age_gen = df.groupby(['gender', 'age'])['value'].sum()
age_gen=pd.DataFrame(age_gen)
age_gen = age_gen.reset_index()
print(age_gen.info())
print(age_gen)

## sum of value per gender, age, and country
age_cou = df.groupby(['age', 'country'])['value'].sum()
age_cou=pd.DataFrame(age_cou, index=None)
age_cou = age_cou.reset_index()
age_cou=age_cou.sort_values('value', ascending=False)
print(age_cou)
print(age_cou.iloc[0:2, 1])
# IN and CN have max tb values (at some age level)
IN_CN = age_cou[(age_cou['country'] == 'IN') | (age_cou['country'] == 'CN')]
print(IN_CN)

# plot age and age_gen
ax = plt.subplot(3, 1, 1)
g=sns.lineplot(x='age', y='value', data=age, ax=ax)
g.set(xlabel='age', ylabel='tuberculosis')
plt.title('tb per age')
ax = plt.subplot(3, 1, 2)
f=sns.lineplot(x='age', y='value', hue='gender', data=age_gen, ax=ax)
plt.title('tb per age and gender')
f.set(xlabel='age', ylabel='tuberculosis')
plt.tight_layout()
ax = plt.subplot(3, 1, 3)
g=sns.lineplot(x='age', y='value', hue='country', data=IN_CN, ax=ax)
g.set(xlabel='age', ylabel='tuberculosis')
plt.title('tb per age of max tb countries')
plt.show()
