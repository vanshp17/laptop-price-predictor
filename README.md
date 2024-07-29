![image](https://github.com/user-attachments/assets/884ea448-cdb6-46b8-a113-9ca740f2e87a)

# Laptop Price Predictor

## Overview

This project is a Streamlit web application that predicts the price of a laptop based on its specifications. The app uses a machine learning model trained on a dataset of laptop prices and their features. The goal is to provide users with an estimated price for a laptop based on inputs such as brand, type, RAM, weight, touchscreen, IPS display, screen size, screen resolution, operating system, CPU, HDD, SSD, and GPU.

## Features

- User-friendly interface to input laptop specifications
- Dynamic prediction of laptop prices
- Visualization of input fields
- Deployment using Streamlit

## Project Structure

The project contains the following files:

- `app.py`: The main Streamlit application script.
- `laptop_data.csv`: The dataset used for training the model.
- `laptop.pkl`: The processed dataset after feature engineering and preprocessing.
- `pipe.pkl`: The trained machine learning model.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Seaborn
- Matplotlib
- XGBoost

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/laptop-price-predictor.git
    cd laptop-price-predictor
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Data Preprocessing

The `ipynb` file contains the code for preprocessing the dataset and training various machine learning models. The steps involved are:

1. **Loading Data**: The dataset is loaded and inspected for missing values and duplicates.
2. **Data Cleaning**: Unnecessary columns are dropped, and data types are converted appropriately.
3. **Feature Engineering**: New features such as `Touchscreen`, `IPS`, `ppi` (pixels per inch), and `Cpu brand` are created. The `Memory` column is split into `HDD` and `SSD` capacities.
4. **Correlation Analysis**: The correlation between features and the target variable (`Price`) is analyzed.
5. **Model Training**: Various regression models are trained, including Linear Regression, Ridge, Lasso, KNN, Decision Tree, SVM, Random Forest, Extra Trees, AdaBoost, and Gradient Boosting.
6. **Model Evaluation**: Models are evaluated using metrics such as R2 Score and Mean Absolute Error (MAE). The best model is selected based on performance.

## Streamlit App

The Streamlit app allows users to input the specifications of a laptop and get a predicted price. The app layout is structured using columns for better visualization and alignment.

### Components

- **Image and Title**: Displayed at the top for better user engagement.
- **Input Fields**: Users can select or input specifications such as Brand, Type, RAM, Weight, Touchscreen, IPS, Screen Size, Screen Resolution, OS, CPU, HDD, SSD, and GPU.
- **Prediction Button**: When clicked, the app predicts and displays the estimated price of the laptop.

## Usage

1. Open the Streamlit app by running `streamlit run app.py`.
2. Input the desired specifications of the laptop.
3. Click on the "Predict" button to get the estimated price.

## Future Work

- Improve the model by including more features and using advanced algorithms.
- Enhance the user interface for better usability.
- Add more visualizations to provide insights into the dataset and predictions.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Streamlit: For the web app framework
- Scikit-learn: For machine learning libraries
