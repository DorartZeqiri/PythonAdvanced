import pandas as pd

df= pd.read_csv('weather_tokyo_data.csv')

df['temperature']= pd.to_numeric(df['temperature'], errors='coerce')
avgTemperature=df['temperature'].mean()


roundavgTemperature=round(avgTemperature,2)

print(f"This is the temperature asked on question 1:  {roundavgTemperature}")
df["day"]= pd.to.datatime(df["day"], format="%m/%d")
df["month"] = df["day"].dt.month

monthly_avg_temperature = df.groupby("month")["temperature"].mean().round 2

print(f"This is the temperature asked on question 2: {monthly_avg_temperature}")

import matplotlib.pyplot as plt

monthly_avg_temperature.plot(kind='bar', color='skyblue')

plt.title("Average Temperature")
plt.xlabel("Monthly Average Temperature ")
plt.ylabel("Temperature")
plt.show()


hottest_day= df.loc[df('temperature').idmax()]
coldest_day= df.loc[df('temperature').idmax()]

print("hottest Day:\n", hottest_day)
print("Coldest Day:\n", coldest_day)

hottest_day1=df[df('temperature')==df('temperature').max()]
print("Hottest Day1 :\n", hottest_day1)

plt.figure(figsize=)