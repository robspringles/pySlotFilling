import pandas as pd
import numpy as np
from random import shuffle

df = pd.read_csv('data.csv')

options = np.arange(len(df))
shuffle(options)
for index in options:
	print(df['response'][index])
	inputString = input()
	df['values'][index] = str(inputString)
	if(df['values'].isnull().sum() == 0):
		break

print(df['values'])
print('you want to play golf with {0} friends in {1} on {2}th at {3}.'.format(df['values'][2], df['values'][0], df['values'][3], df['values'][1]))
