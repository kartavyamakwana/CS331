# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z2BV5KKZwI3ZaJ6dPGGa264ICK5zD7-8
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestCentroid
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

tfidf_vectorizer = TfidfVectorizer()
X = tfidf_vectorizer.fit_transform(newsgroups.data)

X_train, X_test, y_train, y_test = train_test_split(X, newsgroups.target, test_size=0.2, random_state=42)

rocchio_classifier = NearestCentroid()
rocchio_classifier.fit(X_train, y_train)

y_pred = rocchio_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred, target_names=newsgroups.target_names))