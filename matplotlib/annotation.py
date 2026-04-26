import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day": [1, 2, 3, 4,5],
    "users": [120, 150, 170, 160, 180],
    "purchases": [30, 35, 40, 38, 45]
}

df = pd.DataFrame(data)
#print(df)

plt.plot(df["day"], df["users"], linestyle='--', marker='o', color='b', label='Users', linewidth=2, markerfacecolor='red', markersize=8)
plt.xlabel("Day")
plt.ylabel("Number of Users")
plt.title("App Users over time")
plt.legend()
plt.grid(True)

plt.text(3,170,"Peak Day")
plt.show()

