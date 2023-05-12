import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax1 = plt.subplots()
df_year = pd.read_csv("prof_plot_energy.csv")
x1_list = []
for i in df_year['Bandwidth_Gbps']:
    x1_list.append(i)

# b1 = ax1.bar(x1_list, df_year['Energy'], width=0.07, label='Predicted energy consumption',
#              color=sns.xkcd_rgb["denim blue"])
b0 = ax1.bar(x1_list, df_year['baseE'], width=0.07, label='Energy (base)',
             color=sns.xkcd_rgb["denim blue"])
b1 = ax1.bar(x1_list, df_year['transE'], width=0.07, label='Predicted energy (transfer)',
             bottom=df_year['baseE'], color=sns.xkcd_rgb["maize"])


ax2 = ax1.twinx()

line1, = ax2.plot(df_year['Bandwidth_Gbps'], df_year['Optimizer'], color=sns.xkcd_rgb["pale red"], linestyle='-',
                  label='Optimizer performance')
p1 = ax2.scatter(df_year['Bandwidth_Gbps'], df_year['Optimizer'], color=sns.xkcd_rgb["pale red"], marker='o', s=30,
                 label='Optimizer performance')

for i, j, d in zip(df_year['Bandwidth_Gbps'], df_year["Optimizer"], df_year["device"]):
    ax2.annotate('%s' % d, xy=(i, j), xytext=(-13, 3), textcoords='offset points', color=sns.xkcd_rgb["green"])

# ax2.set_ylim([0, 18])
# ax1.set_ylim([0, 45000])
note = ax2.scatter([], [], marker='$1$', color=sns.xkcd_rgb["green"], label="#device needed for optimization")

ax1.set_xlabel("Bandwidth (Gbps)", fontsize=12)
ax1.set_ylabel("Energy (mJ)", fontsize=12)
ax2.set_ylabel("Optimization (%)", fontsize=12)
ax1.set_title("Yolox on Jetson-AGX", fontsize=14)

# Set colors for y-axis tags
ax2.yaxis.label.set_color(line1.get_color())
ax1.yaxis.label.set_color("black")

# Set colors for y-axis marks
ax2.tick_params(axis='y', colors=line1.get_color())
ax1.tick_params(axis='y', colors="black")

# Set legends
plt.legend(handles=[p1, b0, b1, note], loc='best')
plt.grid()
plt.savefig("yolox-agx-energy.png", bbox_inches='tight', dpi=100)
plt.show()
