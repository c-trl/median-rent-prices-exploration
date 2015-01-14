#setup
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
%matplotlib inline

psqftZRI = 'https://raw.githubusercontent.com/c-trl/median-rent-prices-exploration/master/City_ZriPerSqft_AllHomes.csv'
dpsf = pd.read_csv(psqftZRI)

#re-organizing ZRI data
df = dpsf.sort(['State', 'RegionName']).interpolate()
df = df.drop('Metro',1).drop('CountyName',1)
df = df.reset_index(level=1).drop('index',1)
df.rename(columns={'RegionName':'Region'}, inplace=True)
df['Location'] = df.Region.map(str) + ", " + df.State
df = df.drop('Region',1,).drop('State',1)

#moving Location to 0th position in the dataframe
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

#write resulting data to a csv file for further cleaning
#df.to_csv('df.csv')

#cleaning NYC data

nydf = nyc.sort(['State', 'RegionName']).interpolate()
nydf = nydf.reset_index(level=1).drop('index',1)
nydf.rename(columns={'RegionName':'Region'}, inplace=True)
nydf['Location'] = nydf.Region.map(str) + ", " + nydf.State
nydf = nydf.drop('Region',1,).drop('State',1)

#moving Location to 0th position in the dataframe
cols = nydf.columns.tolist()
cols = cols[-1:] + cols[:-1]
nydf = nydf[cols]

#write resulting data to a csv file for further cleaning
#nydf.to_csv('nydf.csv')

#open cleaned csv
df = pd.read_csv('https://raw.githubusercontent.com/c-trl/median-rent-prices-exploration/master/df.csv')
nydf = pd.read_csv('https://raw.githubusercontent.com/c-trl/median-rent-prices-exploration/master/nydf.csv')
df = pd.merge(df,nydf,on='Month')
