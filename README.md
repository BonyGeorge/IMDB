# IMDB Sentiment Analysis Project

This project utilizes Natural Language Processing (NLP) techniques to classify IMDB movie reviews as either **Positive** or **Negative**.

## 🚀 Overview
The repository contains a Jupyter Notebook that demonstrates a full machine learning pipeline:
- **Data Source:** IMDB 50k Movie Reviews (Kaggle).
- **Preprocessing:** Cleaning, Tokenization, Stemming, and Lemmatization.
- **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency).
- **Model:** XGBoost Classifier.

## 🛠️ Prerequisites
Ensure you have the following Python libraries installed:
- `pandas`
- `numpy`
- `matplotlib`
- `nltk`
- `sklearn`
- `xgboost`
- `kagglehub`

## 📁 File Structure
- `IMDB_reviews.ipynb`: Main analysis notebook.
- `NLP_utils.py`: Custom utility class for text cleaning (referenced in code).
- `IMDB Dataset.csv`: The dataset file (automatically downloaded via notebook).

## 📊 Results
The model achieves an accuracy of approximately **89.07%** on the evaluation set using optimized XGBoost parameters.

## 🔧 How to Use
1. Clone the repository.
2. Run `IMDB_reviews.ipynb` in a Jupyter environment.
3. The notebook will automatically download the dataset from Kaggle via `kagglehub`.