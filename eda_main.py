from data_loader import DataLoader
from data_visualizer import DataVisualizer

def main():
    filepath = 'yellow_tripdata.parquet'  # Replace with your actual path

    # Load data
    dataloader = DataLoader(filepath)
    data = dataloader.load()

    #create a new column for trip duration in  inutes
    data['duration'] = (data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime']).dt.total_seconds()/60
    dataloader.inspect(data)

    # Create new columns for pickup hour and day of week
    data['pickup_hour'] = data['tpep_pickup_datetime'].dt.hour
    data['pickup_day_of_week'] = data['tpep_pickup_datetime'].dt.day_name()
    print(data)

    # Clean data
    cleanData = dataloader.cleannull(data)
    dataloader.inspect(cleanData)

    # Visualize data
    datavisualizer = DataVisualizer()
    # Lineplot displaying the number of trips by pickup hour
    datavisualizer.linePlot(cleanData, 'pickup_hour')
    # Lineplot displaying the number of trips by pickup day
    datavisualizer.linePlot(cleanData, 'pickup_day_of_week')
    # Correlation matrix of numerical variables
    correlation_columns = ['trip_distance', 'fare_amount', 'tip_amount', 'total_amount', 'duration']
    correlation_matrix = cleanData[correlation_columns].corr()
    # Heatmap of the correlation matrix
    datavisualizer.heatMap(correlation_matrix)
    # Scatter plot matrix of numerical variables.
    datavisualizer.scatterPlot(cleanData, correlation_columns)
    # Seaborn countplot for PULocationID and DOLocationID. Plotting the top 15 categories by value counts.
    datavisualizer.countPlot(cleanData, 'PULocationID')
    datavisualizer.countPlot(cleanData, 'DOLocationID')
    #box plot of total amount by payment type it helps detecting outliers
    datavisualizer.boxPlot(cleanData, 'payment_type', 'total_amount')
    # Data distributions for 'fare_amount', 'trip_distance' and 'extra' using Seaborn's histplot.
    dataSample = cleanData.sample(frac=0.1, random_state=42)
    datavisualizer.histPlot(dataSample, 'fare_amount')
    datavisualizer.histPlot(dataSample, 'trip_distance')
    datavisualizer.histPlot(dataSample, 'extra') 

if __name__ == "__main__":
    main()
