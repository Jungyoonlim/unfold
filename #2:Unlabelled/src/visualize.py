import matplotlib.pyplot as plt
from Kcluster_main import df, labels
import seaborn as sns 

# simple visualization for practice! 
palette = sns.color_palette('dark', n_colors=len(set(labels)))

# Create a scatter plot
sns.scatterplot(x='BeginDate', y='EndDate', hue=labels, style=labels, palette=palette, data=df)

# Set labels and title
plt.xlabel('Begin Date')
plt.ylabel('End Date')
plt.title('Artist Clusters')

# Optionally you can remove the top and right spines of the plot for a cleaner look
sns.despine()

# Show the plot
plt.show()