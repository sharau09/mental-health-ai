import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load dataset
data = pd.read_csv("data.csv")

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_text = vectorizer.fit_transform(data['text'])

# Combine features
X = np.hstack((X_text.toarray(), data[['sleep','screen']].values))
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")