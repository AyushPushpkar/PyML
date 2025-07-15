import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
}

df = pd.DataFrame(data)

sns.set_style("darkgrid")
# Create line plot
sns.lineplot(data=df, x='x', y='y' , err_style= "band") 
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
