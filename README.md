# Exploratory Data Analysis (EDA)

This repository contains a structured and modular Python implementation of an Exploratory Data Analysis (EDA) project. It is designed to help data scientists and analysts quickly understand, clean, and visualize datasets.

## 📁 Project Structure

```
ExploratoryDataAnalysis/
│
├── eda_main.py              # Main entry point for running EDA
├── data_loader.py           # Loads and inspects raw data
├── data_visualizer.py       # Generates plots and visualizations
└── README.md                # Project overview
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/MHasso/ExploratoryDataAnalysis.git
cd ExploratoryDataAnalysis
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install directly:

```bash
pip install pandas matplotlib seaborn
```

### Running the Project

Update the CSV file path in `eda_main.py`:

```python
filepath = 'sample_data.csv'  # Replace with your actual CSV file path
```

Then run the script:

```bash
python eda_main.py
```

## 🔍 Features

- Plots histograms using Seaborn and saves them as `.png`.
- Basic data cleaning (e.g., drop missing values).
- Easy to extend with additional features like correlation analysis or feature engineering.

## 📊 Example Output

After execution, the script will:

- Display basic dataset info in the console.
- Generate plots for the dataset.
- Save the plots as an image file.

## 🛠️ Extending the Project

You can add:

- Other visualizations (e.g., box plots, pair plots) in `data_visualizer.py`.
- Exported reports or summaries to CSV or HTML.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

