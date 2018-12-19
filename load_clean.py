import pandas as pd
df = pd.read_csv('tb.csv')

# drop columns 'fu' and 'mu' since they only contain missing values and would mess up the following processing steps
df = df.drop(columns = ['fu', 'mu'])

# define row and column length
initial_rows = len(df.index)
initial_col = len(df.columns)

# melt the gender-age columns of the df
df = pd.melt(df, id_vars=['country', 'year'], var_name='variable', value_name='value')
melted_row = len(df.index)

# assert that (initial col-number - id_var_no) * rows = length of rows afterwards
assert (initial_col - 2)*initial_rows == melted_row

# the column 'variable' needs to be split into two columns 'gender' and 'age', delete column 'variable'
df['gender'] = df.variable.str[0]
df['age'] = df.variable.str[1:]
df = df.drop(columns = 'variable')

# transform age into an integer
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# transform gender into category in order to store memory
df['gender'] = df['gender'].astype('category')
print(df.info())
# the transformation seems to be correct. The columns age and gender have no missing values (which would have been
# suspicious)
