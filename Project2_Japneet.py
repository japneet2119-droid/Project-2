import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BC census 2016 data.csv")

high_rent = df[df["shelt_rent_30plus_rate"] > 50]

print("High Rent Burden Areas:")
print(high_rent[["chsa", "shelt_rent_30plus_rate"]])

plt.figure()
plt.bar(high_rent["chsa"], high_rent["shelt_rent_30plus_rate"])
plt.title("Rent Burden with CHSA > 50%", color= 'green', fontsize=20)
plt.xlabel("CHSA", color= 'green', fontsize=20)
plt.ylabel("Burden of Rent (%)", color= 'green', fontsize=20)
plt.xticks(rotation=90, color= 'purple')
plt.show

avg_region = df.groupby("pha")["shelt_rent_30plus_rate"].mean()

print("Region's Average Rent Burden:")
print(avg_region)

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange']

plt.figure(figsize=(10, 10))

explode = [0.09] * len(avg_region)

plt.pie(
    avg_region,
    colors=colors,
    explode=explode,
    labels= avg_region.index,
    autopct='%2.2f%%',
    startangle=150,
    shadow=True,
    wedgeprops={'edgecolor': 'red'}

)

plt.tight_layout()
plt.title("Burden of Rent Distributed by PHA ",
          fontsize=20,
          fontstyle='oblique',
          color= 'green'

          )

plt.show()