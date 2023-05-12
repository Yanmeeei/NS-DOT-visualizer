import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax1 = plt.subplots()
df_year = pd.read_csv("prof_plot_two_opt.csv")
x1_list = []
x2_list = []
for i in df_year['Bandwidth_Gbps']:
    x1_list.append(i)

line1, = ax1.plot(df_year['Bandwidth_Gbps'], df_year['Optimizer'], color=sns.xkcd_rgb["denim blue"], linestyle='-',
                  label='Optimizer performance')
p1 = ax1.scatter(df_year['Bandwidth_Gbps'], df_year['Optimizer'], color=sns.xkcd_rgb["denim blue"], marker='o', s=30,
                 label='Optimizer performance')

for i, j, d in zip(df_year['Bandwidth_Gbps'], df_year["Optimizer"], df_year["device"]):
    ax1.annotate('%s' % d, xy=(i, j), xytext=(-13, 3), textcoords='offset points', color=sns.xkcd_rgb["pale red"])

ax1.set_ylim([0, 25])
note = ax1.scatter([], [], marker='$1$', color=sns.xkcd_rgb["pale red"], label="#device needed for optimization")

ax1.set_xlabel("Bandwidth (Gbps)", fontsize=12)
ax1.set_ylabel("Optimization (%)", fontsize=12)
ax1.set_title("Faster-RCNN on Jetson-AGX", fontsize=14)

# Set colors for y-axis tags
ax1.yaxis.label.set_color(line1.get_color())

# Set colors for y-axis marks
ax1.tick_params(axis='y', colors=line1.get_color())

# Set legends
plt.legend(handles=[p1, note], loc='lower right')
plt.grid()
plt.savefig("rcnn-agx-old.png", bbox_inches='tight', dpi=100)
plt.show()
