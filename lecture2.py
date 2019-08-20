
import pandas as pd
import pandas_datareader.data as pdr
import datetime as dt
import matplotlib.pyplot as plt


start_date= dt.datetime(2010,1,1)
end_date = dt.datetime(2019,6,30)
df = pdr.DataReader("MMM","yahoo",start_date,end_date)
print(df.head())


fig1 = plt.subplot2grid((7,1),(0,0),rowspan=5,colspan=1)
fig2 = plt.subplot2grid((7,1),(5,0),rowspan=2,colspan=1,sharex=fig1)

fig1.plot(df['Adj Close'])
fig2.plot(df['Volume'])
plt.show()
