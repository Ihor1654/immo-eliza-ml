

# 🏡 Real Estate Price Prediction - Immo Eliza
![Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![Pandas](https://img.shields.io/badge/uses-Pandas-blue.svg)
![Matplotlib](https://img.shields.io/badge/uses-Matplotlib-blue.svg)
![Scikit-learn](https://img.shields.io/badge/uses-Scikit--learn-orange.svg)


## 📑 Table of Contents

1. [🔎 Project Overview](#project-overview)
2. [📊 Dataset](#dataset)
3. [🔢 Dataset Features](#dataset-features)
4. [🤖 Model](#model)
5. [🔧 Installation](#installation)
6. [🚀 Usage](#usage)
7. [📈 Performance](#performance)
8. [⚠️ Limitations](#limitations)
9. [👥 Contributors](#contributors)

## 🔎 Project Overview

This project aims to predict real estate prices in Belgium using various machine learning models. The primary objective is to provide accurate price estimates for properties based on their features like location, area, number of bedrooms, etc.
## 🧬 Project structure

```

Immo-eliza-ML/
│
├── data/
│   └── clean_data_with_mv.csv                --- data: training dataset (.csv)
│
├── utils/                    --- definition code: Classes for clean, impute & encode data
│   └── creator.py            --- Class creates and train the model
│   └── removing_missing_val.py --- Class cleans data from missing values
│   └── removing_outliers.py --- Class removes outliers
│   └── training_models.py  --- Class creates and trains models
│   └── encoding_categorical.py ---Class encodes all categorival values in Dataset
│
├── .gitignore
├── requirements.txt
├── main.py   --- execution code: preprocess data and train models.
└── README.md
```


## 📊 Dataset

The dataset used in this project contains information about real estate properties in Belgium, including details such as property type, location, living area, number of bedrooms, and more. It comprises around 15,000 houses.

## 🔢 Dataset Features

| Feature              | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| `locality_name`           | The locality where the property is located.                         | 
| `price`              | The price of the property in euros.                                 |
| `state_of_building` | The condition or state of the property (e.g., new, to renovate).    |
| `living_area`        | The living area of the property in square meters.                   |
| `number_of_rooms`           | The number of rooms in the property.                             |
| `postal_code`          | Postal code of the property                           |
| `garden`         | The garden area of the property in square meters (0 if there is no garden)        |
| `equipped_kitchen`            | Indicates the type of kitchen in the property (e.g., Installed, Hyperequipped etc.).      |
| `open_fire`          | Indicates whether the property has a fireplace (1: Yes, 0: No).     |
| `swimming_pool`       | Indicates whether the property has a swimming pool (1: Yes, 0: No). |
| `terrace_surface`        | The terrace area of the property in square meters (0 if there is no terrace)       |
| `facades`          | Number of frontage for the property.        |
| `land_area`       | The land area of the property in square meters.   |
| `type_of_property`     | Indicates type of property (House or Apartment ).              |
| `subtype_of_property`         | Indicates subtype of property (e.g Chale, Castle,Villa etc ).                    |
| `furnished`         | Indicates if the property is furnished (1: Yes, 0: No).                    |
## 🤖 Model

The project explores several machine learning models, starting with a baseline Extreme Gradient Boosting model and experimenting with other models like Linear Regression and Random Forest Regression. The final model selection is based on performance metrics such as R² score and Mean Squared Error (MSE).

## 🔧 Installation

Follow these steps to set up your project environment:

- **Clone the repository**
  `git clone git@github.com:Ihor1654/immo-eliza-ml.git`
- **Navigate to the project directory**
  `cd immo-eliza-ml`
- **Install the required dependencies**
  `pip install -r requirements.txt`

## 🚀 Usage

To train the model and make predictions, run the following scripts:

- **To preprocess the data and train the model:**
  `python main.py`

## 📈 Performance

The best-performing model (XGBoost model) achieved an R² score of 0.75 on the test set, indicating that it can explain 75% of the variance in property prices.
```

| Model           | MAE         |   RMSE         | R2    |
|                 |             |                |       |
| LinearRegressor | 66,670.13   | 93,728.26      | 0.67  |
| XGBoost         | 56,741.12   | 82,076.52      | 0.75  |
| Random Forest   | 70,506.67   | 101,496.22     | 0.62  |


```

## ⚠️ Limitations

- The model relies heavily on the quality and comprehensiveness of the input data.
- It does not account for market trends or economic conditions.
- The model's predictions are specific to Belgium and may not generalize well to other regions.

## 📂 Project background & timeline

This is the third phase of a four-phase project to create a complete ML pipeline for predicting residential property prices. This project phase took one week to complete in October 2024. For to see previous parts check my github [account](https://github.com/Ihor1654)

The project was completed as part of my 7-month AI training bootcamp at BeCode in Ghent, Belgium.


## 👥 Contributors

- [Ihor Afanasiev](https://www.linkedin.com/in/ihor-afanasiev-a50798268/)
