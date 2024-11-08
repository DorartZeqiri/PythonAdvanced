# import pandas as pd
#
# import matplotlib.pyplot as plt
#
#
# df=pd.read_csv('avgIQpercountry.csv')
#
# df.drop_duplicates(keep='first', inplace=True)
# filtered=df[df["Average IQ"]>=80]
# filtered=filtered.sort_values(by=['Average IQ'], ascending=False)
# print(filtered)
#
# plt.figure(figsize=(14,8))
#
# bars=plt.bar(filtered['Continent'], filtered['Average IQ'],color="skyblue")
# plt.title("Average IQ per continent")
#
# plt.xlabel("Continent")
# plt.ylabel("Average IQ")
# plt.xticks(rotation=90, fontsize=14)
# plt.yticks(fontsize=14)
#
# plt.grid(axis="y",linestyle="--",alpha=0.8)
#
# plt.bar_label(bars, fmt="%.2f", fontsize=10, color="black")
# plt.tight_layout()
# plt.show()
#
