import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score, roc_auc_score, precision_recall_fscore_support, confusion_matrix
from sklearn.preprocessing import label_binarize

def load_and_predict_new_data(file_path):
    # Load the new data
    new_data = pd.read_csv(file_path)
    
    # Load the trained model and vectorizer
    model = joblib.load('Data/Model/classical_ml_model.pkl')
    vectorizer = joblib.load('Data/Model/classical_ml_tfidf_vectorizer.pkl')
    
    # Transform the new data using the loaded vectorizer
    new_data_tfidf = vectorizer.transform(new_data['Lyrics'])
    
    # Predict sentiment
    predictions = model.predict(new_data_tfidf)
    predicted_probs = model.predict_proba(new_data_tfidf)[:, 1]
    
    return new_data, predictions, predicted_probs

def calculate_metrics(new_data, predictions, predicted_probs):
    # Mapping predictions back to numeric if necessary
    label_map = {'Negative': 0, 'Positive': 1}
    numeric_predictions = np.array([label_map[pred] for pred in predictions])

    # True labels are already assumed to be numeric based on the map you use in predictions
    true_labels = new_data['Label'].map({'Negative': 0, 'Positive': 1}).values

    # Calculate Accuracy
    accuracy = accuracy_score(true_labels, numeric_predictions)
    
    # Calculate ROC AUC
    roc_auc = roc_auc_score(true_labels, predicted_probs)
    
    # Calculate Precision, Recall, F1-Score for each class and weighted
    precision, recall, f1, _ = precision_recall_fscore_support(true_labels, numeric_predictions, average=None, labels=[0, 1])
    weighted_precision, weighted_recall, weighted_f1, _ = precision_recall_fscore_support(true_labels, numeric_predictions, average='weighted')
    
    # Calculate Confusion Matrix
    conf_matrix = confusion_matrix(true_labels, numeric_predictions)
    
    # Print Metrics
    print(f"Accuracy: {round(accuracy, 2)}")
    print(f"ROC AUC Score: {round(roc_auc, 2)}")
    print("Negative: Precision: {}, Recall: {}, F1-Score: {}".format(round(precision[0], 2), round(recall[0], 2), round(f1[0], 2)))
    print("Positive: Precision: {}, Recall: {}, F1-Score: {}".format(round(precision[1], 2), round(recall[1], 2), round(f1[1], 2)))
    print("Weighted: Precision: {}, Recall: {}, F1-Score: {}".format(round(weighted_precision, 2), round(weighted_recall, 2), round(weighted_f1, 2)))
    print(f"Confusion Matrix:\n{conf_matrix}")

# Path to the Validating dataset CSV file
file_path = 'Data/Cleaned/cleanedValidatingLabeled.csv'

# Predict new data and calculate metrics
new_data, predictions, predicted_probs = load_and_predict_new_data(file_path)
calculate_metrics(new_data, predictions, predicted_probs)
