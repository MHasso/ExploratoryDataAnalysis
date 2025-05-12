import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
   
    def linePlot(self, data, column):
        column_counts = data[column].value_counts().sort_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=column_counts.index, y=column_counts.values, marker='o')
        plt.title(f'Line Plot of {column}')
        plt.xlabel(column)
        plt.ylabel(f"{column} count")
        filename = f"{column}.png"
        plt.savefig(filename)
        plt.close()

    def heatMap(self, correlation_matrix):
        plt.figure(figsize=(10, 5))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Heat Map')
        filename = 'Heat_Map.png'
        plt.savefig(filename)
        plt.close()

    def scatterPlot(self, data, correlation_columns):
        plt.figure(figsize=(10, 5))
        sns.pairplot(data[correlation_columns].sample(frac=0.001))
        plt.title('scatter Plot')
        filename = 'Scatter_Plot.png'
        plt.savefig(filename)
        plt.close()

    def countPlot(self, data, column):
        plt.figure(figsize=(10, 6))
        data_column = data[column].value_counts().nlargest(15).index
        top = data[data['PULocationID'].isin(data_column)]
        sns.countplot(data=top, x=f'{column}', order=data_column)
        filename = f"{column}_countPlot.png"
        plt.savefig(filename)
        plt.close()

    def boxPlot(self, data, x, y):
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=data, x=x, y=y)
        filename = "boxPlot.png"
        plt.savefig(filename)
        plt.close()
 

    def histPlot(self, data, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], bins=50, kde=True, color='blue')
        plt.xlabel(f"{column}")
        plt.title(f"Distribution of {column}")
        filename = f"{column}.png"
        plt.savefig(filename)
        plt.close()

