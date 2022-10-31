"""
df1 shows the company which strategies are available to invest in when the company wants to deploy an
energy asset this can be the deployment of an energy storage unit, upgrade of a new transmission line,
etc. on the other hand, df2 groups the investment strategies that are mutually exclusive (in other for a
two investment strategies to mutually exclusive there has to be a union of at least one investment asset
in their investment strategies, which makes it impossible to invest in both because the 3-letter code
investment asset represents an investment in the same energy asset at a specific location and same time).
"""
import pandas as pd
import numpy as np
import math


# Extract data
df = pd.read_excel('investment_code.xlsx')
pd.set_option('display.max_columns', None)
df.fillna('', inplace=True)
df['Character length'] = ''
df['Individual Investments'] = ''
df['A'] = ''
df['B'] = ''
df['C'] = ''
df['D'] = ''
df.rename(columns={'Unnamed: 0': 'Investment set (code)'}, inplace=True)

# ILLUSTRATIONS
for k in df.index:
    df.loc[k, 'Character length'] = len(df.loc[k, 'Investment set (code)'])
df.drop('LENGTH', axis=1, inplace=True)  # drops 'LENGTH' column
first_col_df = df[df.columns[0]]
for k in first_col_df:
    (k[0:3], '-', k[3:6], '-', k[6:9], '\n')  # indexes k as specified

for k in first_col_df:
    ('\nk = ', k, 'len(k) = ', len(k))
    for i in range(0, len(k), 3):
        ('i = ', i)
        (k[i:i + 3])

# APPLICATION
characters_split = []
for k in first_col_df:
    ('k = ', k)
    characters_split.append([k[i:i + 3] for i in range(0, len(k), 3)])

df['Individual Investments'] = characters_split
# print(df)

# creating a list or list
test_list = []
for k in range(4):
    # print('k = ', k)
    test_list.append([k + i for i in range(0, 6, 2)])
# print(test_list)

df.loc[0, 'Individual Investments'][0]  # captures specified location from specified cell

for k in df.index:
    # print('k = ', k)
    df.loc[k, 'A'] = df.loc[k, 'Individual Investments'][0]

    num_elements_list = len(df.loc[k, 'Individual Investments'])  # confirming the number of elements in that cell
    # print('num_elements_list = ', num_elements_list)
    if num_elements_list >= 2:
        df.loc[k, 'B'] = df.loc[k, 'Individual Investments'][1]
    else:
        df.loc[k, 'B'] = np.nan
    if num_elements_list >= 3:
        df.loc[k, 'C'] = df.loc[k, 'Individual Investments'][2]
    else:
        df.loc[k, 'C'] = np.nan
    if num_elements_list >= 4:
        df.loc[k, 'D'] = df.loc[k, 'Individual Investments'][3]
    else:
        df.loc[k, 'D'] = np.nan
# print(df)

# deleting columns
df.drop([1, 2, 3, 4], axis=1, inplace=True)
# print(df)
df_same = df.copy()

# explaining explode
test = pd.DataFrame({'red': [[4, 2, -2], 'hello', [], [10, 2]],
                     'dark': 9,
                     'black': [['1', 'c', 'b'], np.nan, [], ['r', 'd']]})
# print(test.explode('black'))  # takes the elements of every list out of the list

# APPLICATION
df = df.explode('Individual Investments')
# print(df)

# EXPLAINING GROUP-BY FUNCTION
test_df = pd.DataFrame({'red': [6, 7, 8, 11, 20, 100, 10],
                        'dark': ['ABC', 'ABC', 'DRT', 'DRT', 'MAE', 'MAE', 'MAE'],
                        'black': [['1', 'c', 'b'], np.nan, [], ['r', 'd'], 12, 120, 100]})
test_result = test_df.groupby('dark')['red'].sum()
test_result2 = test_df.groupby('dark')['red'].apply(list)  # groups the elements of test by 'dark'
# and appends the values to test-result1
# print(test_result)
# print(test_result2)

# BACK TO ORIGINAL DATASET
series1 = df.groupby('Individual Investments')[df.columns[0]].apply(list)  # this is of type series
# print(series1)

df1 = pd.DataFrame(series1)
# print(df1)

len(df1.loc['DCQ', 'Investment set (code)'])  # now a dataframe so positions can be located using 'loc'

# finding the number of elements in df1
for k in df1.index:
    df1.loc[k, 'Number of elements'] = len(df1.loc[k, df1.columns[0]])
# As originally specified, df1 will now return the number of times
# an investment is to be invested in the electricity network. These investments represented by
# a 3-letter code can be invested only once in electricity system. so for investments
# 'DCQ' a company can pick the first or second strategy not both.

# print(df1)

# GROUPING INVESTMENT STRATEGIES
games = pd.DataFrame({
    'Games': [['Football', 'Cricket', 'Basketball'], ['Football', 'Volleyball'],
              ['Swimming', 'tennis']]
})
# print(games)
'|'.join(['one', 'two', 'three'])  # joins the elements of the list with the specified separator.

test_list = []
# test_list.append()  # allows to expand the list
for t in range(9):
    test_list.append([2 + i for i in range(3)])  # creates a list and appends it to the test_list 9x
# print(test_list)
(lambda k: k * k)(25)  # this is same as function below


def example(k):
    return k * k


example(5)
# APPLICATION
games['All games'] = games.apply(lambda x: ' | '.join(x['Games']), axis=1)  # x is a row of games df and
# the (.apply) function means that the function which is defined by lambda is repeated for every row x

# print(games)
# print(games['All games'].str.contains('Football'))  # checks if the str. Football is in column games['All games']
df_same['Pattern'] = df_same.apply(lambda x: '|'.join(x['Individual Investments']), axis=1)
# print(df_same)

x = df_same.loc[1]  # grabs the specified row of specified df.
which_index = x.name  # find out which index the row belongs to
df_same.index.isin([which_index])  # returns a bool to satisfy if which_index is a sub set of df_same.index
arr = ~df_same.index.isin([which_index])  # ~ inverts the results of output line just above
arr
new_df = df_same[arr]  # returns df_same but without the first row can be seen in new_df of whose index omits 0
new_df
df_same.loc[which_index]['Pattern']  # returns the values of the column 'Pattern' that is defined as which_index
found = df_same['Pattern'].str.contains(df_same.loc[which_index]['Pattern'])
found
# df_same['Pattern'].str.contains(df_same.loc[5]['Pattern'])  # because the same investment
# appears in 2 investment strategies it therefore cannot be implemented. Making them mutually exclusive investments
# print(df_same['Pattern'].str.contains(df_same.loc[which_index]['Pattern']))
words = new_df.loc[found]['Investment set (code)']
# print(words.tolist())


# making a Function to automate process
def find_matches(y):
    which_index2 = y.name
    arr2 = ~df_same.index.isin([which_index2])
    new_df2 = df_same[arr2]

    found2 = df_same['Pattern'].str.contains(y['Pattern'])
    words2 = new_df2[found2]['Investment set (code)']
    words_list = words2.tolist()
    return words_list  # mutually exclusive investments strategies to y, as they share at least one investment with y


series_of_investments = df_same.apply(lambda y: find_matches(y), axis=1)
# print(series_of_investments)  # type is series
df2 = df_same.copy()
df2['Mutually Exclusive Investments'] = series_of_investments
df2 = df2[['Investment set (code)', 'Mutually Exclusive Investments']]
print(df2)

